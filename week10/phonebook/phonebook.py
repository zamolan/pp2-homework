import psycopg2
import csv

def connect():
    return psycopg2.connect(
        dbname="1011",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432"
    )

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        phone VARCHAR(20)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(csv_filename):
    conn = connect()
    cur = conn.cursor()
    with open(csv_filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            username, phone = row
            cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    conn = connect()
    cur = conn.cursor()
    username = input("Enter username: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()
    cur.close()
    conn.close()

def update_user():
    conn = connect()
    cur = conn.cursor()
    name = input("Enter username for update: ")
    choice = input("What to update? (name/phone): ")
    if choice == 'name':
        new_name = input("Enter new username: ")
        cur.execute("UPDATE phonebook SET username = %s WHERE username = %s", (new_name, name))
    elif choice == 'phone':
        new_phone = input("Enter new phone: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()

def query_users():
    conn = connect()
    cur = conn.cursor()
    print("1. Show all users")
    print("2. Search with name")
    print("3. Search with phone")
    choice = input("Choice: ")
    if choice == '1':
        cur.execute("SELECT * FROM phonebook")
    elif choice == '2':
        name = input("Enter username: ")
        cur.execute("SELECT * FROM phonebook WHERE username = %s", (name,))
    elif choice == '3':
        phone = input("Enter phone: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def delete_user():
    conn = connect()
    cur = conn.cursor()
    delete_by = input("Delete with (name/phone): ")
    value = input("Enter: ")
    if delete_by == "name":
        cur.execute("DELETE FROM phonebook WHERE username = %s", (value,))
    elif delete_by == "phone":
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (value,))
    conn.commit()
    cur.close()
    conn.close()

def main():
    create_table()
    while True:
        print("\n=== PhoneBook Menu ===")
        print("1. Add from console")
        print("2. Add from CSV")
        print("3. Show/search users")
        print("4. Update data")
        print("5. Delete data")
        print("0. Exit")
        choice = input("Choice: ")
        if choice == '1':
            insert_from_console()
        elif choice == '2':
            filename = "contacts.csv"
            insert_from_csv(filename)
        elif choice == '3':
            query_users()
        elif choice == '4':
            update_user()
        elif choice == '5':
            delete_user()
        elif choice == '0':
            break
        else:
            print("Error!")

if __name__ == '__main__':
    main()