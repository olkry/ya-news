import pytest
from datetime import datetime, timedelta

from django.urls import reverse
from django.utils import timezone
from django.test.client import Client

from news.models import News, Comment

PAGINATION_ON_MAIN = 10


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create(username='Автор')


@pytest.fixture
def not_author(django_user_model):
    return django_user_model.objects.create(username='Не автор')


@pytest.fixture
def author_client(author):
    client = Client()
    client.force_login(author)
    return client


@pytest.fixture
def not_author_client(not_author):
    client = Client()
    client.force_login(not_author)
    return client


@pytest.fixture
def news():
    news = News.objects.create(
        title='Заголовок',
        text='Текст новости',
    )
    return news


@pytest.fixture
def comment(author, news):
    comment = Comment.objects.create(
        news=news,
        author=author,
        text='Текст комментария'
    )
    return comment


@pytest.fixture
def id_for_news(news):
    return (news.id,)


@pytest.fixture
def many_news():
    today = datetime.today()
    all_news = [
        News(
            title=f'News {index}',
            text='Jast text',
            date=today - timedelta(days=index),
        ) for index in range(PAGINATION_ON_MAIN + 6)
    ]
    return News.objects.bulk_create(all_news)


@pytest.fixture
def many_comments(news, author):
    now = timezone.now()
    for index in range(10):
        comments = Comment.objects.create(
            news=news, author=author, text=f'Tекст {index}',
        )
        comments.created = now + timedelta(days=index)
        comments.save()
    return comments


@pytest.fixture
def detail_url(news):
    return reverse('news:detail', args=(news.id,))


@pytest.fixture
def home_url(news):
    return reverse('news:home')


@pytest.fixture
def form_data(news):
    return {'text': 'Текст комментария'}


@pytest.fixture
def new_form_data(news):
    return {'text': 'Новый текст комментария'}


@pytest.fixture
def delete_url(comment):
    return reverse('news:delete', args=(comment.id,))


@pytest.fixture
def edit_url(comment):
    return reverse('news:edit', args=(comment.id,))
