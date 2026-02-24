import sqlite3
from pprint import pprint


def create_tables(conn):
    conn.execute("DROP TABLE IF EXISTS students")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        location TEXT
    )
    """)

def add_student(conn, name, age, location):
    print(f"{name=}, {age=}, {location=}")
    conn.execute("""
    INSERT INTO students(name, age, location) VALUES 
    (?, ?, ?)
    """,
    (name, age, location)
    )

    # conn.execute(f"""
    # INSERT INTO students(name, age, location) VALUES
    # ({name}, {age}, {location})
    # """) # не делать - SQL injection
    conn.commit()

def delete_student(conn, student_id):
    conn.execute("""
    DELETE FROM students WHERE student_id = ?
    """, (student_id,))
    conn.commit()

def delete_student_by_name(conn, name):
    conn.execute("""
    DELETE FROM students WHERE name = ?
    """, (name,))
    conn.commit()

def get_all_students(conn):
    result = conn.execute("""
        SELECT location, name, age FROM students 
        ORDER BY age LIMIT 10
    """)
    return result.fetchall()

def get_students_by_name(conn, name):
    result = conn.execute("SELECT * FROM students WHERE name = ?", (name,))
    return result.fetchall()

def get_students_by_id(conn, student_id):
    result = conn.execute("""
    SELECT * FROM students WHERE student_id = ?
    """, (student_id,))
    return result.fetchall()

def change_student(conn, student_id, user_name, age, location):
    conn.execute("""
    UPDATE students 
    SET name = ?, age = ?, location = ? 
    WHERE student_id = ?
    """, (user_name, age, location, student_id))
    conn.commit()

if __name__ == "__main__":
    connection = sqlite3.connect("database.db")
    create_tables(conn=connection)
    add_student(conn=connection, name="Igor", age=35, location="Karakol")
    add_student(conn=connection, name="Kurmanbek", age=20, location="Bishkek")
    add_student(conn=connection, name="Almaz", age=20, location="Bishkek")
    add_student(conn=connection, name="Almaz", age=25, location="Bishkek")

    print("====== select =====")
    all_students = get_all_students(conn=connection)
    pprint(all_students)
    print("----")
    pprint(get_students_by_name(conn=connection, name="Almaz"))
    print("----")
    pprint(get_students_by_id(conn=connection, student_id=1))
    print("===================")

    print("====== update =====")
    change_student(
        conn=connection,
        user_name="Ilya",
        age=25,
        location="Karakol",
        student_id=1,
    )
    pprint(get_students_by_id(conn=connection, student_id=1))
    print("==================")

    delete_student(conn=connection, student_id=1)
    delete_student_by_name(conn=connection, name="Almaz")

    connection.close()
