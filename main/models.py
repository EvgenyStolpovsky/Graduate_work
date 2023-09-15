from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Modul(models.Model):

    name = models.CharField(max_length=200, verbose_name='Название Общеобразовательного модуля')
    is_active = models.BooleanField(default=True, verbose_name='активный')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Добавить Модуль'
        verbose_name_plural = 'Модули'
        ordering = ('name',)


class Lesson(models.Model):
    """
    Класс описывающее - Занятие.
    """

    FORM = [
        ('FORM ONE', 'Обзорная лекция.'),
        ('FORM TWO', 'Лекция.'),
        ('FORM THREE', 'Практикум.'),
        ('FORM FOUR', 'Консультация.'),
        ('FORM FIVE', 'Беседа.'),
        ('FORM SIX', 'Круглый стол.'),
    ]


    name = models.ForeignKey(Modul, on_delete=models.CASCADE, verbose_name='Название общего курса')
    numbers = models.PositiveSmallIntegerField(verbose_name='Порядковый номер')
    lesson = models.CharField(max_length=200, verbose_name='Название занятия')
    subject = models.CharField(max_length=200, verbose_name='Тема')
    description = models.TextField(verbose_name='Описание')
    form = models.CharField(max_length=20, choices=FORM, verbose_name='Форма проведения', **NULLABLE)
    image = models.ImageField(upload_to='lesson/', verbose_name='Изображение', **NULLABLE)

    class Meta:
        verbose_name = 'Добавить занятие'
        verbose_name_plural = 'Занятия'
        ordering = ('lesson',)

    def __str__(self):
        return f'{self.numbers} - {self.lesson} - {self.subject} - {self.form}'
