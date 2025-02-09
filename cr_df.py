import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("data.db")
cursor = conn.cursor()


# Create reservations table
cursor.execute("""
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cos_name TEXT NOT NULL,
    cos_phone INTEGER NOT NULL,
    hall TEXT NOT NULL,
    date DATE NOT NULL,
    datetime DATETIME NOT NULL,
    services TEXT NOT NULL,
    deposit INTEGER NOT NULL,
    remaining_amount INTEGER NOT NULL
);
""")

# Create hall table
cursor.execute("""
CREATE TABLE IF NOT EXISTS hall (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hall_num INTEGER NOT NULL,
    tabels INTEGER NOT NULL,
    FOREIGN KEY (hall_num) REFERENCES reservations(hall)
);
""")

# Create services table
cursor.execute("""
CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    food INTEGER NOT NULL CHECK (food IN (0, 1)),
    refreshments INTEGER NOT NULL CHECK (refreshments IN (0, 1)),
    photography INTEGER NOT NULL CHECK (photography IN (0, 1)),
    others TEXT NOT NULL
);
""")

# Create purchases table
cursor.execute("""
CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mat TEXT NOT NULL,
    price INTEGER NOT NULL,
    date DATE NOT NULL
);
""")

# Create salaries table
cursor.execute("""
CREATE TABLE IF NOT EXISTS salaries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employ TEXT NOT NULL,
    em_phone INTEGER NOT NULL
    wage INTEGER NOT NULL      
);
""")

# Create emploies table
cursor.execute("""
CREATE TABLE IF NOT EXISTS emploies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone INTEGER NOT NULL,
    FOREIGN KEY (phone) REFERENCES salaries(em_phone),
    FOREIGN KEY (name) REFERENCES salaries(employ)
);
""")

# Commit changes and close connection
conn.commit()
conn.close()

print("SQLite database and tables created successfully!")
