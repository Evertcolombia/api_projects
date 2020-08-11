from django.test import TestCase

from app.calc import add, subtract

class CalcTests(TestCase):
    
    def test_add_numbers(self):
        """Test that two number are added together"""
        self.assertEqual(add(2, 8), 10)

    def test_subtract_number(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(11, 4), 7)