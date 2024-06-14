import sqlite3
from flask import jsonify
from config import CONFIG

DATABASE_PATH = 'gift_shop.db'

def read_all():
    """Retrieve all products from the database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def read_productbyId(product_id):
    """Retrieve a single product by its ID."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product

def create(name, description, price):
    """Create a new product in the database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, description, price) VALUES (?, ?, ?)", (name, description, price))
    conn.commit()
    conn.close()

def update_productbyId(product_id, name, description, price):
    """Update an existing product."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name = ?, description = ?, price = ? WHERE id = ?", (name, description, price, product_id))
    conn.commit()
    conn.close()

def delete_productbyId(product_id):
    """Delete a product by its ID."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
