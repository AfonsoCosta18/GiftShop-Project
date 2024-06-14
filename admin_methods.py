import sqlite3
import logging
from config import CONFIG
from gift_shopdb import get_db_connection

# Configure logging
logging.basicConfig(level=logging.DEBUG)

products = [
    {'id': 1, 'name': 'Personalized T-shirt'},
    {'id': 2, 'name': 'Personalized Mug'},
    {'id': 3, 'name': 'Personalized Photo Frame'},
    {'id': 4, 'name': 'Personalized Photo Album'},
]

cart = []

def add_product(name, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO products (name, price) VALUES (?, ?)",
        (name, price)
    )
    product_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return product_id

def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    
    # Fetch all rows
    rows = cursor.fetchall()
    
    # Get column names from cursor description
    column_names = [description[0] for description in cursor.description]
    
    cursor.close()
    conn.close()
    
    # Convert rows to dictionaries using column names
    products = [dict(zip(column_names, row)) for row in rows]
    logging.debug("Fetched products: %s", products)
    return products

def get_product(product_id):
    logging.debug(f"Fetching product with ID: {product_id}")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()
    if product:
        logging.debug(f"Product found: {product}")
        return dict(product)
    else:
        logging.debug(f"Product with ID {product_id} not found")
        return None

def update_product(product_id, name, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE products SET name = ?, price = ? WHERE id = ?",
        (name, price, product_id)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    cursor.close()
    conn.close()

def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart_item = next((item for item in cart if item['id'] == product_id), None)
        if cart_item:
            cart_item['quantity'] += 1
        else:
            cart.append({'id': product['id'], 'name': product['name'], 'quantity': 1})



def get_cart():
    return cart

def place_order(order_data):
    try:
        logging.debug("Processing order: %s", order_data)
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Insert into orders table
        cursor.execute(
            "INSERT INTO orders (name, address, payment_method) VALUES (?, ?, ?)",
            (order_data['name'], order_data['address'], order_data['payment-method'])
        )
        order_id = cursor.lastrowid
        
        for item in cart:
            cursor.execute(
                "INSERT INTO order_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
                (order_id, item['id'], item['quantity'])
            )
        conn.commit()
        cursor.close()
        conn.close()
        cart.clear()  # Clear the cart after processing the order
        logging.debug("Order processed and cart cleared.")
        return True
    except Exception as e:
        logging.error("Error processing order: %s", e)
        return False







def root_endpoint():
    return "Welcome to the Gift Shop API!", 200




#def add_to_cart(product_id):
    #logging.debug(f"Adding product with ID to cart: {product_id}")
    #product = get_product(product_id)
    #if product:
        #cart_item = next((item for item in cart if item['id'] == product_id), None)
        #if cart_item:
            #cart_item['quantity'] += 1
        #else:
            #cart.append({'id': product['id'], 'name': product['name'], 'price': product['price'], 'quantity': 1})
        #logging.debug(f"Product added to cart: {product}")
        #return True
    #logging.debug(f"Product not found with ID: {product_id}")
    #return False