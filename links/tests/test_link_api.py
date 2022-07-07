import pytest
from django.urls import reverse

from links.tests.factories import LinkFactory

base_url = reverse('Link-list')
detail_url = reverse('Link-detail', kwargs={'pk': '1'})
pytestmark = pytest.mark.django_db


@pytest.fixture()
def create_link():
    return LinkFactory()


def test_list(client, create_link):
    response = client.get(path=base_url)
    assert response.status_code == 200


def test_detail(client, create_link):
    response = client.get(path=detail_url)
    assert response.status_code == 200


def test_detail_bookmark(client, create_link, get_user):
    url = detail_url + '/bookmarks'
    no_user_response = client.post(path=url)
    assert no_user_response.status_code == 403

    header = {'HTTP_uuid': get_user.uuid}
    response = client.post(path=url, **header)
    assert response.status_code == 201
