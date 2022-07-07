import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from accounts.tests.factories import UserFactory
from articles.tests.factories import ArticleFactory

register(UserFactory)
register(ArticleFactory)

pytestmark = pytest.mark.django_db


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def get_user():
    return UserFactory()
