"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc


# 28. Write a test
class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

# 29. Write a test using TDD
    """
    TDD work flow as below:
        1. Write test for behaviour expected to see in code
        2. Test fails
        3. Write code so test passes

    Run the below commande:
        docker compose run -rm app sh -c 'python manage.py test'
    """

    def test_subtract_numbers(self):
        """Testing subtracting numbers."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)

    # from rest_framework import APIClient
    # def test_get_greetings(self):
    #     """ Testing getting greeting """
    #     client = APIClient()
    #     res  = client.get('/greeting/')
    #     self.assertEqual(res, "Hello!")
