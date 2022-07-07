import pytest
from django.urls import reverse

from articles.tests.factories import ArticleFactory

base_url = reverse('Articles-list')
detail_url = reverse('Articles-detail', kwargs={'pk': '1'})
pytestmark = pytest.mark.django_db


@pytest.fixture()
def create_article():
    article = ArticleFactory.create()
    return article


def test_list(client):
    response = client.get(base_url)
    assert response.status_code == 200


def test_detail(client, create_article):
    response = client.get(detail_url)
    assert response.status_code == 200


def test_detail_bookmark(client, create_article, get_user):
    url = detail_url + '/bookmarks'
    no_user_response = client.post(path=url)
    assert no_user_response.status_code == 403

    header = {'HTTP_uuid': get_user.uuid}
    response = client.post(path=url, **header)
    assert response.status_code == 201

