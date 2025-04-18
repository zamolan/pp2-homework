import psycopg2
import csv
import json

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

#    NEW

def search_by_pattern(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def insert_or_update_user(username, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)", (username, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_many_users(data):
    conn = connect()
    cur = conn.cursor()
    json_data = json.dumps(data)
    cur.execute("CALL insert_many_users(%s::json)", (json_data,))
    conn.commit()
    cur.close()
    conn.close()

def get_users_paginated(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_users_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def delete_user_proc(delete_by, value):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_user_proc(%s, %s)", (delete_by, value))
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
        #    NEW
        print("6. Insert or update ONE user (procedure)")
        print("7. Insert MANY users (procedure with JSON)")
        print("8. Search by pattern")
        print("9. Paginate users")
        print("10. Delete user (procedure)")
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
        elif choice == '6':
            username = input("Enter username: ")
            phone = input("Enter phone: ")
            insert_or_update_user(username, phone)
        elif choice == '7':
            print("Enter users as list of dicts (e.g., [{'username': 'Tom', 'phone': '87005554433'}])")
            users_str = input("Paste JSON here: ")
            try:
                users = json.loads(users_str)
                insert_many_users(users)
            except:
                print("Invalid JSON input!")
        elif choice == '8':
            pattern = input("Enter pattern (e.g., 'A%'): ")
            search_by_pattern(pattern)
        elif choice == '9':
            limit = int(input("Enter how many users to show: "))
            offset = int(input("Enter from which user to start (offset): "))
            get_users_paginated(limit, offset)
        elif choice == '10':
            delete_by = input("Delete by (name/phone): ")
            value = input("Enter value: ")
            delete_user_proc(delete_by, value)
        elif choice == '0':
            break
        else:
            print("Error!")


if __name__ == '__main__':
    main()