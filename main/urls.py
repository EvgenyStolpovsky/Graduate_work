from rest_framework.routers import DefaultRouter
from main.apps import MainConfig
from django.urls import path
from main.views.modul import ModulViewSet

from main.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
LessonUpdateAPIView, LessonDestroyAPIView


app_name = MainConfig.name

router = DefaultRouter()
router.register(r'courses', ModulViewSet, basename='courses')

urlpatterns = [

    # Lesson
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

] + router.urls
