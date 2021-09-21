from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_owner_with_succesful(self):
        """Test creating a new user is successful"""
        username = 'evertcolombia'
        author = 'evert escalante'
        password = 'changethis'
        owner = get_user_model().objects.create_user(
            username=username,
            author=author,
            password=password
        )
        self.assertEqual(owner.username, username)
        # use check_password cause password  will be hashed
        self.assertTrue(owner.check_password(password))
    
    