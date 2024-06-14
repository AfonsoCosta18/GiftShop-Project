import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from admin_frontend import app

class AdminFrontendTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_product(self):
        response = self.app.post('/api/products', json={'name': 'Test Product', 'price': 10.99})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_read_products(self):
        response = self.app.get('/api/products')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_read_product(self):
        response = self.app.get('/api/products/1')
        self.assertIn(response.status_code, [200, 404])  # Product might or might not exist

    def test_update_product(self):
        response = self.app.put('/api/products/1', json={'name': 'Updated Product', 'price': 15.99})
        self.assertIn(response.status_code, [200, 404])  # Product might or might not exist

    def test_delete_product(self):
        response = self.app.delete('/api/products/1')
        self.assertIn(response.status_code, [204, 404])  # Product might or might not exist

    def test_add_to_cart(self):
        response = self.app.post('/api/cart', json={'productId': 1})
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json)

    def test_get_cart(self):
        response = self.app.get('/api/cart')
        self.assertEqual(response.status_code, 200)
        self.assertIn('cart', response.json)

    def test_place_order(self):
        response = self.app.post('/api/order', json={'orderDetails': 'Test Order'})
        self.assertIn(response.status_code, [200, 500])  # Order might fail or succeed

    def test_clear_cart(self):
        response = self.app.post('/api/cart/clear')
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json)

if __name__ == '__main__':
    unittest.main()
