from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    """
    Команда для заполнения БД фикстурой.
    Для заполнения данными используйте команду:
    python manage.py fill

    """

    def handle(self, *args, **options):
        call_command('loaddata', 'data.json')