# db.py
import sqlite3

DB_NAME = "address.db"

def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            address TEXT
        )
    """)
    conn.commit()
    conn.close()


def add_contact(name, phone, email, address):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO contacts (name, phone, email, address)
        VALUES (?, ?, ?, ?)
    """, (name, phone, email, address))
    conn.commit()
    conn.close()


def get_all_contacts():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts ORDER BY id DESC")
    data = cur.fetchall()
    conn.close()
    return data


def search_contacts(keyword):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM contacts
        WHERE name LIKE ? OR phone LIKE ? OR email LIKE ? 
    """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
    data = cur.fetchall()
    conn.close()
    return data


def update_contact(cid, name, phone, email, address):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE contacts
        SET name=?, phone=?, email=?, address=?
        WHERE id=?
    """, (name, phone, email, address, cid))
    conn.commit()
    conn.close()


def delete_contact(cid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE id=?", (cid,))
    conn.commit()
    conn.close()
