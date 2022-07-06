import pytest
from django.urls import reverse

from articles.tests.factories import ArticleFactory

base_url = reverse('Articles-list')
pytestmark = pytest.mark.django_db


@pytest.fixture()
def create_article():
    article = ArticleFactory.create()
    return article


def test_list(client):
    response = client.get(base_url)
    assert response.status_code == 200


def test_detail(client, create_article):
    detail_url = reverse('Articles-detail', kwargs={'pk': '1'})
    response = client.get(detail_url)
    assert response.status_code == 200


