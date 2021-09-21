from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_succesful(self):
        """Test creating a new user is successful"""
        email = 'evertcolombia@admin.com'
        author = 'evert escalante'
        password = 'changethis'
        user = get_user_model().objects.create_user(
            email=email,
            author=author,
            password=password
        )
        self.assertEqual(user.email, email)
        # use check_password cause password  will be hashed
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized."""
        email = "evertcolombia@AMDMIN.com"
        user = get_user_model().objects.create_user(email, 'changethis')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user without email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'changethis')
    
    