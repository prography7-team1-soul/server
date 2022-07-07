import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from accounts.tests.factories import UserFactory
from articles.tests.factories import ArticleFactory
from links.tests.factories import LinkFactory

register(UserFactory)
register(ArticleFactory)
register(LinkFactory)

pytestmark = pytest.mark.django_db


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def get_user():
    return UserFactory()
