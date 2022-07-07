import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from accounts.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


def get_user_header(get_user):
    header = {'HTTP_uuid': get_user.uuid}
    return header


def test_sign_up_view(client, get_user):
    url = 'http://127.0.0.1:8000/api/users/signup'
    u_data = {'fcm_token': get_user.fcm_token}
    new_uuid = 'test_uuid_02'
    header = {'HTTP_uuid': new_uuid}
    request = client.post(path=url, data=u_data, **header)
    assert request.status_code == 200
    header2 = {'HTTP_uuid': get_user.uuid}
    request = client.post(path=url, data=u_data, **header2)
    assert request.status_code == 400


def test_user_detail_view(client, get_user):
    url = reverse('User-detail', kwargs={'pk': '1'})
    header = get_user_header(get_user)
    response = client.get(path=url, **header)
    assert response.status_code == 200


def test_user_detail_bookmark_view(client, get_user):
    url = 'http://127.0.0.1:8000/api/users/1/bookmarks'
    header = get_user_header(get_user)
    no_parameter_response = client.get(path=url, **header)
    assert no_parameter_response.status_code == 400

    no_uuid_response = client.get(path=url)
    assert no_uuid_response.status_code == 403

    not_valid_header = {'HTTP_uuid': 'no_uuid'}
    not_valid_uuid_response = client.get(path=url, **not_valid_header)
    assert not_valid_uuid_response.status_code == 403

    club_url = url + '?app=club'
    club_response = client.get(path=club_url, **header)
    assert club_response.status_code == 200

    chatroom_url = url + '?app=chatroom'
    chatroom_response = client.get(path=chatroom_url, **header)
    assert chatroom_response.status_code == 200

    article_url = url + '?app=article'
    article_response = client.get(path=article_url, **header)
    assert article_response.status_code == 200
