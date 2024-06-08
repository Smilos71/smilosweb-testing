# database.py
import sqlite3

def create_db():
    conn = sqlite3.connect('forms.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS forms
                 (id INTEGER PRIMARY KEY, title TEXT, questions TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS responses
                 (id INTEGER PRIMARY KEY, form_id INTEGER, response TEXT)''')
    conn.commit()
    conn.close()

def create_form(title, questions):
    conn = sqlite3.connect('forms.db')
    c = conn.cursor()
    c.execute("INSERT INTO forms (title, questions) VALUES (?, ?)", (title, questions))
    conn.commit()
    conn.close()

def get_forms():
    conn = sqlite3.connect('forms.db')
    c = conn.cursor()
    c.execute("SELECT * FROM forms")
    forms = c.fetchall()
    conn.close()
    return forms

def get_form(form_id):
    conn = sqlite3.connect('forms.db')
    c = conn.cursor()
    c.execute("SELECT * FROM forms WHERE id=?", (form_id,))
    form = c.fetchone()
    conn.close()
    return form

def create_response(form_id, response):
    conn = sqlite3.connect('forms.db')
    c = conn.cursor()
    c.execute("INSERT INTO responses (form_id, response) VALUES (?, ?)", (form_id, response))
    conn.commit()
    conn.close()
