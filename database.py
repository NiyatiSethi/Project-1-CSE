# Add a new faculty
def add_faculty(name, department, qualification, experience):
    conn = get_connection()
import sqlite3

def get_connection():
    return sqlite3.connect("Project-1-CSE/faculty.db")

# Create the faculty table
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faculty (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            qualification TEXT NOT NULL,
            experience INTEGER NOT NULL
        );
    """)

    conn.commit()
    conn.close()

#------ CRUD Functions ------
def add_faculty(name, department, qualification, experience):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO faculty (name, department, qualification, experience) VALUES (?, ?, ?, ?)",
        (name, department, qualification, experience)
    )

    conn.commit()
    conn.close()


def get_all_faculty():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM faculty")
    rows = cursor.fetchall()

    conn.close()
    return rows


def update_faculty(fid, name, department, qualification, experience):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """UPDATE faculty
           SET name = ?, department = ?, qualification = ?, experience = ?
           WHERE id = ?""",
        (name, department, qualification, experience, fid)
    )

    conn.commit()
    conn.close()


def delete_faculty(fid):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM faculty WHERE id = ?", (fid,))
    conn.commit()
    conn.close()

create_table()
print("Database setup complete.")

from gui import start_app
print("Faculty Data CRUD Manager started.")
start_app()