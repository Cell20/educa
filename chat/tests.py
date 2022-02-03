from django.test.client import Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from courses.models import Course, Subject
from django.contrib.auth.models import User
from unittest import TestCase


class CourseTest(TestCase):

    def setUp(self):
    self.client = Client()
    self.user = get_user_model().objects.create_user(
        username='test', email='test@educa.com')

    self.user1 = get_user_model().objects.create_user(
        'testuser1', password='password', email='test1@educa.com')

    self.subject = Subject.objects.create(
        title='Programming', slug='programming')
    self.course = Course.objects.create(owner=self.user, subject=self.subject,
                                        title='Django Projects', slug='django-projects', overview='xyz')
    self.course.students.add(User.objects.get(id=2))

    def test_correct(self):
        context = {'username': self.user1.username,
                   'password': self.user1.password}
        self.client.login(
            username='testuser1', password='password')

        response = self.client.get(
            reverse('chat:course_chat_room', args=[self.course.id]))
        print(response)

    # def test_redirect_if_not_logged_in(self):
        # response = self.client.get(
        # reverse('chat:course_chat_room', args=[self.course.id]))
        # print(response)
        # self.assertRedirects(response, '/accounts/login/?next=/chat/room/1/')

    '''def test_chat_room_status_code_as_logged_in(self):
        login = self.client.login(username='', password='')
        response = self.client.get()
        self.assertEqual(str(response.context['user']), 'testuser1')'''

# def test_template_used(self):
# response = self.client.get('chat/room/1/')
# self.assertTemplateUsed(response, 'room.html')
