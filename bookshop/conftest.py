import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from .models import *


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def seller():
    return baker.make('bookshop.Seller')


@pytest.fixture
def seller_user(seller):
    return seller.user


@pytest.fixture
def book():
    return baker.make('bookshop.Book')


@pytest.fixture
def shop():
    return baker.make('bookshop.Shop')


@pytest.fixture
def book_sold():
    return baker.make('bookshop.BookSold')


@pytest.fixture
def instock():
    return baker.make('bookshop.InStock')


@pytest.fixture
def purchase():
    return baker.make('bookshop.Purchase')


@pytest.fixture
def owner():
    return baker.make(User, is_superuser=True)