from django.core.management import BaseCommand

from Regional_anesthesia.models import Modul, Lesson


class Command(BaseCommand):
    """
    Класс, который удаляет данные json из модели - Modul, Lesson.
    Для удаления данных из модели используйте команду:
    python manage.py delete_data_json
    """

    def handle(self, *args, **options):
        Modul.objects.all().delete()
        Lesson.objects.all().delete()



