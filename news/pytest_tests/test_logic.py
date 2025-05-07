import pytest
from pytils.translit import slugify
from http import HTTPStatus
from pytest_django.asserts import assertRedirects

from django.urls import reverse

from news.models import Comment


@pytest.mark.django_db
def test_anonymous_user_cant_create_comment(
        client, detail_url, form_data
):
    client.post(detail_url, form_data)
    comments_count = Comment.objects.count()
    assert comments_count == 0


def test_user_can_create_comment(
        author_client, news, detail_url, form_data, author
):
    response = author_client.post(detail_url, form_data)
    assertRedirects(response, f'{detail_url}#comments')
    comments_count = Comment.objects.count()
    assert comments_count == 1
    comment = Comment.objects.get()
    assert comment.text == form_data['text']
    assert comment.news == news
    assert comment.author == author


def test_author_can_delete_comment(
        author_client, delete_url, detail_url
):
    response = author_client.delete(delete_url)
    assertRedirects(response, f'{detail_url}#comments')
    assert response.status_code == HTTPStatus.FOUND
    comments_count = Comment.objects.count()
    assert comments_count == 0


def test_user_cant_delete_comment_of_another_user(
    not_author_client, delete_url
):
    response = not_author_client.delete(delete_url)
    assert response.status_code == HTTPStatus.NOT_FOUND
    comments_count = Comment.objects.count()
    assert comments_count == 1


def test_author_can_edit_comment(
        author_client, edit_url, new_form_data, detail_url, comment
):
    response = author_client.post(edit_url, new_form_data)
    assertRedirects(response, f'{detail_url}#comments')
    comment.refresh_from_db()
    assert comment.text == new_form_data['text']


def test_user_cant_edit_comment_of_another_user(
        not_author_client, edit_url, new_form_data, comment, form_data
):
    response = not_author_client.post(edit_url, new_form_data)
    assert response.status_code == HTTPStatus.NOT_FOUND
    comment.refresh_from_db()
    assert comment.text == form_data['text']