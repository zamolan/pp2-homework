import pygame
import psycopg2
import time
import random

pygame.init()

conn = psycopg2.connect(
    dbname="1011",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

def get_or_create_user(conn, username):
    cur = conn.cursor()
    cur.execute("""
        SELECT u.id, u.username, COALESCE(us.food_eaten, 0)
        FROM "user" u
        LEFT JOIN user_score us ON u.id = us.user_id
        WHERE u.username = %s
        ORDER BY us.saved_at DESC NULLS LAST
        LIMIT 1
    """, (username,))
    
    result = cur.fetchone()
    if result:
        user_id, username, food_eaten = result
        print(f"Welcome back, {username}! Food eaten in the last game: {food_eaten}")
        return user_id, 0
    else:
        cur.execute("INSERT INTO \"user\" (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        print(f"New user {username} created. Let’s start the game!")
        return user_id, 0

def save_game_state(conn, user_id, food_eaten):
    cur = conn.cursor()
    cur.execute("INSERT INTO user_score (user_id, food_eaten) VALUES (%s, %s)", (user_id, food_eaten))
    conn.commit()
    print(f"Game saved! Food eaten: {food_eaten}")

def generate_wall(snake):
    while True:
        x = random.randint(0, 55) * 10
        y = random.randint(0, 39) * 10
        wall_rect = pygame.Rect(x, y, 50, 10)
        too_close = any(pygame.Rect(*segment, 10, 10).colliderect(wall_rect.inflate(50, 50)) for segment in snake)
        if not too_close:
            return (x, y)

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

username = input("Enter your username: ")
user_id, food_eaten = get_or_create_user(conn, username)

snake = [(100, 50)]
direction = (0, 0)
food = (300, 200)
wall = None
paused = False

font = pygame.font.SysFont(None, 36)
running = True

while running:
    screen.fill((0, 0, 0))

    food_text = font.render(f"Food eaten: {food_eaten}", True, (255, 255, 255))
    screen.blit(food_text, (10, 10))

    pygame.draw.rect(screen, (255, 255, 0), (*food, 10, 10))
    
    if wall:
        pygame.draw.rect(screen, (255, 0, 0), (*wall, 50, 10))

    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, 10, 10))

    pygame.display.flip()
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: direction = (0, -10)
            elif event.key == pygame.K_DOWN: direction = (0, 10)
            elif event.key == pygame.K_LEFT: direction = (-10, 0)
            elif event.key == pygame.K_RIGHT: direction = (10, 0)
            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    print("Game paused. Press any key to continue.")
                    save_game_state(conn, user_id, food_eaten)
                while paused:
                    for e in pygame.event.get():
                        if e.type == pygame.KEYDOWN:
                            paused = False

    if not paused:
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)

        if head == food:
            food_eaten += 1
            food = (10 * ((food_eaten * 3) % 60), 10 * ((food_eaten * 7) % 40))
            wall = generate_wall(snake)
        else:
            snake.pop()

        if head in snake[1:] or head[0] < 0 or head[0] >= 600 or head[1] < 0 or head[1] >= 400:
            print(f"Game over. Food eaten: {food_eaten}")
            save_game_state(conn, user_id, food_eaten)
            time.sleep(2)
            running = False

        if wall and pygame.Rect(*head, 10, 10).colliderect(pygame.Rect(*wall, 50, 10)):
            print(f"Game over (hit the wall). Food eaten: {food_eaten}")
            save_game_state(conn, user_id, food_eaten)
            time.sleep(2)
            running = False

pygame.quit()
conn.close()
