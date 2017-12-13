import unittest
import os
import json
from app import create_app, db

class ShoppinglistTestCase(unittest.TestCase):
    """This class represents the shoppinglist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.shoppinglist = {'name': 'lets create shoppping list'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_shoppinglist_creation(self):
        """Test API can create a shoppinglist (POST request)"""
        res = self.client().post('/shoppinglists/', data=self.shoppinglist)
        self.assertEqual(res.status_code, 201)
        self.assertIn('shoppinglist created!', str(res.data))

    def test_api_can_get_all_shoppinglists(self):
        """Test API can get a shoppinglist (GET request)."""
        res = self.client().post('/shoppinglists/', data=self.shopppinglist)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/shoppinglists/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('lets get all shoppinglist', str(res.data))
   

    def test_shoppinglist_deletion(self):
        """Test API can delete an existing shoppinglist. (DELETE request)."""
        rv = self.client().post(
            '/shoppinglists/',
            data={'name': 'flour,meat,carrots'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/shoppinglists/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/shoppinglists/1')
        self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

    