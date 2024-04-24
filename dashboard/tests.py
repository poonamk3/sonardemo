from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class DashboardTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='test_password')

    def test_dashboard_view(self):
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')

    def test_register_view(self):
        response = self.client.get(reverse('user_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/register.html')

    def test_login_view(self):
        response = self.client.get(reverse('user_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/login.html')
class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
    
    def test_register_view_post(self):
        # Test POST request with valid form data
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        response = self.client.post(self.register_url, form_data)
        self.assertEqual(response.status_code, 302)  # Check if the user is redirected after successful registration

        # Check if the user is created
        self.assertTrue(User.objects.filter(username='testuser').exists())

        # Test POST request with invalid form data
        invalid_form_data = {
            'username': '',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        response = self.client.post(self.register_url, invalid_form_data)
        self.assertEqual(response.status_code, 200)  # Check if the form is re-rendered with errors
        self.assertContains(response, 'This field is required.')  # Check if the error message is displayed