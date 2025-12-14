from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from unittest.mock import patch
from django.db import OperationalError

class AuthIntegrationTests(APITestCase):

    def setUp(self):
        # Налаштування перед кожним тестом
        self.register_url = reverse('auth_register')
        self.login_url = reverse('token_obtain_pair')
        self.user_data = {
            'username': 'integration_user',
            'email': 'test@example.com',
            'password': 'StrongPassword123!',
            'password2': 'StrongPassword123!'
        }

    def test_integration_registration_flow(self):
        # Тест реєстрації
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='integration_user').exists())

    def test_integration_login_flow(self):
        # Тест логіну
        User.objects.create_user(username='integration_user', password='StrongPassword123!')
        login_data = {
            'username': 'integration_user',
            'password': 'StrongPassword123!'
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    @patch('user_api.serializers.User.objects.create_user')
    def test_registration_with_mock_db_fail(self, mock_create_user):
        # Тест з Mock (імітація помилки бази даних)
        mock_create_user.side_effect = OperationalError("DB Connection Failed")
        try:
            self.client.post(self.register_url, self.user_data)
        except OperationalError:
            pass
        
        mock_create_user.assert_called_once()
        self.assertFalse(User.objects.filter(username='integration_user').exists())