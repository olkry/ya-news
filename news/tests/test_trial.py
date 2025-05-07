# from unittest import skip

# from django.test import TestCase

# # Импортируем модель, чтобы работать с ней в тестах.
# from news.models import News


# # Создаём тестовый класс с произвольным названием, наследуем его от TestCase.
# @skip(reason='TestNews')
# class TestNews(TestCase):

#     TEXT = 'Тестовый текст'
#     TITLE = 'Заголовок новости'

#     # В методе класса setUpTestData создаём тестовые объекты.
#     # Оборачиваем метод соответствующим декоратором.
#     @classmethod
#     def setUpTestData(cls):
#         # Стандартным методом Django ORM create() создаём объект класса.
#         # Присваиваем объект атрибуту класса: назовём его news.
#         cls.news = News.objects.create(
#             title=cls.TITLE,
#             text=cls.TEXT,
#         )

#     # Проверим, что объект действительно был создан.
#     def test_successful_creation(self):
#         # При помощи обычного ORM-метода посчитаем количество записей в базе.
#         news_count = News.objects.count()
#         # Сравним полученное число с единицей.
#         self.assertEqual(news_count, 1)

#     def test_title(self):
#         # Сравним свойство объекта и ожидаемое значение.
#         self.assertEqual(self.news.title, self.TITLE)


'''
class Test(TestCase):

    def test_example_success(self):
        self.assertTrue(True)  # Этот тест всегда будет проходить успешно.


class YetAnotherTest(TestCase):

    def test_example_fails(self):
        self.assertTrue(False)  # Этот тест всегда будет проваливаться.
'''

'''
# Запустить все тесты проекта.
python manage.py test

# Запустить только тесты в приложении news.
python manage.py test news

# Запустить только тесты из файла test_trial.py в приложении news.
python manage.py test news.tests.test_trial

# Запустить только тесты из класса Test
# в файле test_trial.py приложения news.  
python manage.py test news.tests.test_trial.Test

# Запустить только тест test_example_fails
# из класса YetAnotherTest в файле test_trial.py приложения news.
python manage.py test news.tests.test_trial.YetAnotherTest.test_example_fails 
'''
