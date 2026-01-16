from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Employee
from django.contrib.auth.models import User

class EmployeeAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.login(username='admin', password='admin123')
        # Sample employee
        self.employee = Employee.objects.create(
            name="John Doe",
            email="john@example.com",
            department="HR",
            role="Manager"
        )

    def test_create_employee(self):
        url = reverse('employee-list')
        data = {
            "name": "Alice",
            "email": "alice@example.com",
            "department": "Engineering",
            "role": "Developer"        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_duplicate_email(self):
        url = reverse('employee-list')
        data = {
            "name": "John Duplicate",
            "email": "john@example.com",  # existing email
            "department": "HR",
            "role": "Analyst",        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_employees(self):
        url = reverse('employee-list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_retrieve_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
