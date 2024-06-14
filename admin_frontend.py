from flask import Flask, render_template, request, jsonify
from admin_methods import add_product, delete_product, get_products, get_product, update_product, add_to_cart, get_cart, place_order, cart
from config import CONFIG
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    logging.debug("Home page accessed.")
    return render_template('index.html')

@app.route('/products')
def products():
    logging.debug("Products page accessed.")
    return render_template('products.html')

@app.route('/cart')
def cart_page():
    logging.debug("Cart page accessed.")
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    logging.debug("Checkout page accessed.")
    return render_template('checkout.html')

@app.route('/admin', methods=['GET'])
def admin():
    logging.debug("Admin page accessed.")
    return render_template('admin.html')

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product_id = add_product(data['name'], data['price'])
    return jsonify({'id': product_id}), 201

@app.route('/api/products', methods=['GET'])
def read_products():
    products = get_products()
    return jsonify(products)

@app.route('/api/products/<int:product_id>', methods=['GET'])
def read_product(product_id):
    product = get_product(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    data = request.get_json()
    update_product(product_id, data['name'], data['price'])
    return '', 200

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    delete_product(product_id)
    return '', 204

@app.route('/api/cart', methods=['GET', 'POST'])
def api_cart():
    if request.method == 'POST':
        product_id = request.json.get('productId')
        add_to_cart(product_id)
        return jsonify({'message': 'Product added to cart'})
    else:
        cart = get_cart()
        return jsonify({'cart': cart})
    

@app.route('/api/order', methods=['POST'])
def place_order_route():
    try:
        order_data = request.get_json()
        logging.debug("Received order data: %s", order_data)
        if place_order(order_data):
            return jsonify({'success': True})
        else:
            return jsonify({'success': False}), 500
    except Exception as e:
        logging.error("Error placing order: %s", e)
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/cart/clear', methods=['POST'])
def clear_cart():
    try:
        global cart
        cart.clear()  # Clear the cart
        logging.debug("Cart cleared successfully.")
        return jsonify({'success': True})
    except Exception as e:
        logging.error("Error clearing cart: %s", e)
        return jsonify({'success': False, 'error': str(e)}), 500



if __name__ == '__main__':
    app.run(host=CONFIG["frontend"]["listen_ip"], port=CONFIG["frontend"]["port"], debug=CONFIG["frontend"]["debug"])





#@app.route('/api/cart', methods=['POST'])
#def add_to_cart_route():
    #product_id = request.json.get('productId')
    #logging.debug(f"Adding product to cart: {product_id}")
    #if add_to_cart(product_id):
        #return jsonify({'message': 'Product added to cart'}), 200
    #else:
        #logging.debug(f"Product with ID {product_id} not found")
        #return jsonify({'message': 'Product not found'}), 404

#@app.route('/api/cart', methods=['GET'])
#def get_cart_route():
    #cart = get_cart()
    #logging.debug(f"Cart contents: {cart}")
    #return jsonify(cart)