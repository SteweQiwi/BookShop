import pytest
from django.test import TestCase

# Create your tests here.
from rest_framework import status

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize('url', [
    '/bookshop/book/',
    '/bookshop/shop/',
    '/bookshop/book-sold/',
    '/bookshop/instock/',
    '/bookshop/purchase/',
    '/bookshop/seller/',
])
def test_anonymous_views(api_client, url):
    response = api_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_create_book(api_client, seller_user, book):
    api_client.force_authenticate(seller_user)
    response = api_client.post(
        '/bookshop/book/',
        {
            "name": "book1",
            "price": 2.00,
            "genre": 4,
            "author": "Ya",
            "year_published": 2020
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    response = api_client.get('/bookshop/book/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2


def test_update_book(api_client, seller_user, book):
    api_client.force_authenticate(seller_user)
    response = api_client.put(
        f'/bookshop/book/{book.pk}/',
        {
            "name": "book2",
            "price": 3.00,
            "genre": 3,
            "author": "Ya1",
            "year_published": 2021
        }
    )
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 6
    response = api_client.get('/bookshop/book/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


def test_partial_update_book(api_client, seller_user, book):
    api_client.force_authenticate(seller_user)
    response = api_client.patch(
        f'/bookshop/book/{book.pk}/',
        {
            "year_published": 2015
        }
    )
    assert response.status_code == status.HTTP_200_OK
    response = api_client.get('/bookshop/book/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
