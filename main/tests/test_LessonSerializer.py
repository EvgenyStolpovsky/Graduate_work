from django.test import TestCase

from main.models import Modul
from main.serliazers.lesson import LessonSerializer


class LessonSerializerTest(TestCase):

    def setUp(self):
        self.modul = Modul.objects.create(name='Test Modul', is_active=True)

    def test_lesson_serializer(self):
        # Создание нового модуля

        lesson_data = {
            'name': self.modul.id,
            'numbers': 1,
            'lesson': 'Test Lesson',
            'subject': 'Test Subject',
            'description': 'This is a test lesson'
        }

        # Сериализация тестовых данных
        serializer = LessonSerializer(data=lesson_data)

        self.assertTrue(serializer.is_valid())

        # Сохранение тестовых данных
        lesson = serializer.save()

        # Тестирование сохраненных урока
        self.assertEqual(lesson.name, self.modul)
        self.assertEqual(lesson.numbers, 1)
        self.assertEqual(lesson.lesson, 'Test Lesson')
        self.assertEqual(lesson.subject, 'Test Subject')
        self.assertEqual(lesson.description, 'This is a test lesson')

        updated_lesson_data = {
            'name': self.modul.id,
            'numbers': 2,
            'lesson': 'Updated Lesson',
            'subject': 'Updated Subject',
            'description': 'This is an updated lesson',

        }

        serializer = LessonSerializer(lesson, data=updated_lesson_data)
        self.assertTrue(serializer.is_valid())
        updated_lesson = serializer.save()

        self.assertEqual(updated_lesson.name, self.modul)
        self.assertEqual(updated_lesson.numbers, 2)
        self.assertEqual(updated_lesson.lesson, 'Updated Lesson')
        self.assertEqual(updated_lesson.subject, 'Updated Subject')
        self.assertEqual(updated_lesson.description, 'This is an updated lesson')
