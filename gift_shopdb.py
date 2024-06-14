import sqlite3
import logging
from config import CONFIG

# Initialize Logging
logging.basicConfig(level=logging.INFO)

DATABASE_PATH = 'gift_shop.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

def create_database():
    """Create the SQLite database and its tables."""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        c = conn.cursor()

        # Create Products table
        c.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL
                  )''')

        # Create Orders table (without user_id)
        c.execute('''CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    payment_method TEXT NOT NULL,
                    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                  )''')

        # Create Order Items table
        c.execute('''CREATE TABLE IF NOT EXISTS order_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_id INTEGER NOT NULL,
                    product_id INTEGER NOT NULL,
                    quantity INTEGER NOT NULL,
                    FOREIGN KEY (order_id) REFERENCES orders(id),
                    FOREIGN KEY (product_id) REFERENCES products(id)
                  )''')

        conn.commit()
        logging.info("Database created successfully with tables: products, orders, order_items.")
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

# Test the create_database function
if __name__ == "__main__":
    create_database()

