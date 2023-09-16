from rest_framework import generics

from main.models import Lesson
from main.serliazers.lesson import LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Отвечает за создание сущности в модели Lesson.
    """
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """
    Отвечает за получение списка сущностей в модели Lesson.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Отвечает за получение одной сущности в модели Lesson.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Отвечает за обновление сущности в модели Lesson.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Отвечает за удаление сущности в модели Lesson.
    """
    queryset = Lesson.objects.all
