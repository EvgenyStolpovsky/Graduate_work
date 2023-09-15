from django.test import TestCase

from main.models import Modul


class ModulModelTest(TestCase):
    """
    Тесты для модели Modul

    """

    def setUp(self):
        self.modul = Modul.objects.create(name='Test Module', is_active=True)

    def test_modul(self):
        self.assertEqual(self.modul.name, 'Test Module')
        self.assertEqual(self.modul.is_active, True)
        self.assertEqual(str(self.modul), 'Test Module')

    def test_verbose_names(self):
        self.assertEqual(Modul._meta.verbose_name, 'Добавить Модуль')
        self.assertEqual(Modul._meta.verbose_name_plural, 'Модули')

    def test_ordering(self):
        self.assertEqual(Modul._meta.ordering, ('name',))

    def test_field_max_length(self):
        name_field = Modul._meta.get_field('name')
        self.assertEqual(name_field.max_length, 200)
