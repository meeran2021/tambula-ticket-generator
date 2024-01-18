import sqlite3
import json


def connect_database():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    return conn, cursor


def disconnect_database(conn):
    conn.commit()
    conn.close()


def create_tickets_table():
    conn, cursor = connect_database()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_data TEXT
        )
    ''')

    disconnect_database(conn)


def insert_ticket(cursor, ticket_data):
    cursor.execute('''
        INSERT INTO tickets (ticket_data) VALUES (?)
    ''', (json.dumps(ticket_data),))


def retrieve_tickets(page = 1, tickets_per_page = 1000):
    conn, cursor = connect_database()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tickets'")
    table_exists = cursor.fetchone()

    formatted_tickets = {}

    if not table_exists:
        create_tickets_table()
        disconnect_database(conn)
        return formatted_tickets

    offset = (page - 1) * tickets_per_page
    cursor.execute(f'SELECT id, ticket_data FROM tickets LIMIT ? OFFSET ?', (tickets_per_page, offset))
    tickets_data = cursor.fetchall()
    
    for ticket_id, ticket_json in tickets_data:
        formatted_tickets[str(ticket_id)] = json.loads(ticket_json)

    disconnect_database(conn)

    return formatted_tickets



def save_tickets_to_db(tickets):
    conn, cursor = connect_database()

    create_tickets_table()

    for ticket in tickets:
        insert_ticket(cursor, ticket)

    disconnect_database(conn)
