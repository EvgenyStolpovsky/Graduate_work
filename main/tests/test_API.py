from rest_framework import status
from rest_framework.test import APITestCase,  APIClient

from main.models import Modul
from main.serliazers.modul import ModulSerializer


class ModulApiTestCase(APITestCase):
    """
    Тестирование запроса к API /anesthesia/.
    """

    def test_get(self):
        # Тестирование GET-запроса к API

        modul_1 = Modul.objects.create(name='test 1', is_active=True)
        modul_2 = Modul.objects.create(name='test 2', is_active=False)
        url = 'http://127.0.0.1:8000/courses/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = ModulSerializer([modul_1, modul_2], many=True).data
        self.assertEqual(response.data, serializer_data)


    def test_post(self):
        # Тестирование POST-запроса к API

        self.data = {"name": "Норийная вышка", "is_active": True}
        self.url = 'http://127.0.0.1:8000/courses/'
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_delete(self):
        # Тестирование DELETE-запроса к API

        url = 'http://127.0.0.1:8000/courses/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class LessonApiTestCase(APITestCase):

    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.client = APIClient()
        self.modul = Modul.objects.create(name='Test Modul', is_active=True)

    def test_get(self):

        url = 'http://127.0.0.1:8000/lessons/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        # Тестирование POST-запроса к API

        self.lesson = {
            'name': self.modul.id,
            'numbers': 1,
            'lesson': 'Test Lesson',
            'subject': 'Test Subject',
            'description': 'Test Description',
            'form': 'FORM ONE'
        }
        self.url = 'http://127.0.0.1:8000/lessons/create/'
        response = self.client.post(self.url, self.lesson, format='json')
        self.assertEqual(response.status_code, 201)

    def test_delete(self):
        # Тестирование DELETE-запроса к API
        self.lesson = {
            'name': self.modul.id,
            'numbers': 1,
            'lesson': 'Test Lesson',
            'subject': 'Test Subject',
            'description': 'Test Description',
            'form': 'FORM ONE'
        }

        self.url = 'http://127.0.0.1:8000/lessons/delete/'
        response = self.client.post(self.url, self.lesson, format='json')
        self.assertEqual(response.status_code, 404)


