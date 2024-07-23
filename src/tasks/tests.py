from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        Task.objects.create(title='Test Task 1', priority=1, completed=False, user=self.user)
        Task.objects.create(title='Test Task 2', priority=2, completed=True, user=self.user)
        Task.objects.create(title='Test Task 3', priority=3, completed=False, user=self.user)

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task 1')
        self.assertContains(response, 'Test Task 2')
        self.assertContains(response, 'Test Task 3')

    def test_task_filter_priority(self):
        response = self.client.get(reverse('task_list') + '?priority=1')
        self.assertContains(response, 'Test Task 1')
        self.assertNotContains(response, 'Test Task 2')
        self.assertNotContains(response, 'Test Task 3')

    def test_task_filter_completed(self):
        response = self.client.get(reverse('task_list') + '?completed=True')
        self.assertNotContains(response, 'Test Task 1')
        self.assertContains(response, 'Test Task 2')
        self.assertNotContains(response, 'Test Task 3')

    def test_task_create(self):
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'Task description',
            'priority': 2,
            'completed': False
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Task.objects.filter(title='New Task').exists())