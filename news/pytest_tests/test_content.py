import pytest

from news.pytest_tests.conftest import PAGINATION_ON_MAIN


@pytest.mark.django_db
def test_news_count(many_news, client, home_url):
    response = client.get(home_url)
    object_list = response.context['object_list']
    news_count = object_list.count()
    assert news_count == PAGINATION_ON_MAIN


@pytest.mark.django_db
def test_news_order(many_news, client, home_url):
    response = client.get(home_url)
    object_list = response.context['object_list']
    all_dates = [news.date for news in object_list]
    sorted_dates = sorted(all_dates, reverse=True)
    assert all_dates == sorted_dates


@pytest.mark.django_db
def test_comments_order(client, many_comments, news, detail_url):
    response = client.get(detail_url)
    news = response.context['news']
    all_comments = news.comment_set.all()
    all_timestamps = [comment.created for comment in all_comments]
    sorted_timestamps = sorted(all_timestamps)
    assert all_timestamps == sorted_timestamps


@pytest.mark.django_db
def test_anonymous_client_has_no_form(client, news, detail_url):
    response = client.get(detail_url)
    assert 'form' not in response.context


@pytest.mark.django_db
def test_authorized_client_has_form(news, author_client, detail_url):
    response = author_client.get(detail_url)
    assert 'form' in response.context
