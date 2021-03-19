from django.test import Client, TestCase
from rest_framework.status import HTTP_200_OK


# pylint: disable=no-self-use
class TestHealth(TestCase):
    databases = '__all__'

    def test_health_check(self):
        """Test health-check"""
        client = Client()
        response = client \
            .get(path='/api/v1/health/', content_type='application/json')
        self.assertEqual(response.status_code, HTTP_200_OK, 'Check health API')
