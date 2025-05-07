from http import HTTPStatus
import pytest
from pytest_lazy_fixtures import lf
from pytest_django.asserts import assertRedirects

from django.urls import reverse


@pytest.mark.parametrize(
    ('name', 'args'),
    (
        ('users:login', None),
        ('users:signup', None),
        ('users:logout', None),
        ('news:detail', lf('id_for_news')),
    )
)
@pytest.mark.django_db
def test_pages_availability_for_anonymous_user(client, name, args):
    url = reverse(name, args=args)
    response = client.get(url)
    if 'logout' in url:
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    else:
        assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize(
    'parametrized_client, expected_status',
    (
        (lf('not_author_client'), HTTPStatus.NOT_FOUND),
        (lf('author_client'), HTTPStatus.OK)
    ),
)
@pytest.mark.parametrize(
    'name',
    ('news:edit', 'news:delete'),
)
def test_availability_for_comment_edit_and_delete(
    parametrized_client, expected_status, name, comment
):
    url = reverse(name, args=(comment.id,))
    response = parametrized_client.get(url)
    assert response.status_code == expected_status


@pytest.mark.parametrize(
    'name',
    ('news:edit', 'news:delete'),
)
def test_redirect_for_anonymous_client(client, name, comment):
    url = reverse(name, args=(comment.id,))
    redirect_url = f'{reverse('users:login')}?next={url}'
    response = client.get(url)
    assertRedirects(response, redirect_url)
