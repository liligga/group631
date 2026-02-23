import sqlite3


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
    conn.commit()


if __name__ == "__main__":
    connection = sqlite3.connect("database.db")
    create_tables(conn=connection)
    add_student(conn=connection, name="Igor", age=35, location="Karakol")
    add_student(conn=connection, name="Kurmanbek", age=20, location="Bishkek")


    connection.close()
