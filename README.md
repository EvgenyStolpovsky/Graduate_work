# Дипломный проект от SkyPro. 
# Django-приложение “Образовательные модули”

#### Описание.<br> Написать небольшой проект на Django и Django Rest Framework с моделью "Образовательные модули". В них есть:
- порядковый номер
- название
- описание

#### Задача. <br>При создании проекта нужно: <br>
- реализовать для модели (моделей) все методы CRUD
- Полностью покрыть автоматизированными юнит-тестами все модели, сериализаторы, виды.

#### Требуемый стэк
- Python 3.11, Docker, Django, PostgreSQL, ORM, MVT/MTV, FBV/CBV, Serliazers, Viewset/Generic, Tests, Git, Readme, PEP8, Swagger



## В проекте используется Unittest. Для подсчета покрытия используется Coverage: Total - 92%

- python manage.py test

- coverage run --source='.' manage.py test

- coverage report


## Документация проекта: 

		http://127.0.0.1:8000/swagger/