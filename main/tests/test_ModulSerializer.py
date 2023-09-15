from unittest import TestCase

from main.models import Modul
from main.serliazers.modul import ModulSerializer


class ModulSerializerTestCase(TestCase):
    """
    Тестирование сериализатора модели - Модуль.
    ModulSerializer.
    class Models/models.py
    """

    def test_modul(self):
        modul_1 = Modul.objects.create(name='test 1', is_active=True)
        modul_2 = Modul.objects.create(name='test 2', is_active=False)
        data = ModulSerializer([modul_1, modul_2], many=True).data
        expected_data = [
            {
                'id': modul_1.id,
                'name': 'test 1',
                'is_active': True
            },
            {
                'id': modul_2.id,
                'name': 'test 2',
                'is_active': False
            },
        ]
        self.assertEqual(data, expected_data)
