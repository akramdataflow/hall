import sqlite3

def init_db():
    connection = sqlite3.connect("data.db")  # Create a connection to the database
    cursor = connection.cursor()