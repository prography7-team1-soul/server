import pytest
from django.urls import reverse
from faker import Faker

pytestmark = pytest.mark.django_db
base_url = reverse('search-view')
fake = Faker()


def test_search(client):
    no_parameter_response = client.get(base_url)
    assert no_parameter_response.status_code == 400

    # search_param은 있지만 app은 없는 경우
    search_param = fake.text()
    url = base_url + f'?search_param={search_param}'
    response = client.get(url)
    assert 'club_search_list' in response.data.keys()
    assert 'chatroom_search_list' in response.data.keys()
    assert 'article_search_list' in response.data.keys()
    assert 'link_search_list' in response.data.keys()
    assert response.status_code == 200

    # app = club, search_param O
    app = 'club'
    url = base_url + f'?app={app}&search_param={search_param}'
    response = client.get(url)
    assert 'club_search_list' in response.data.keys()
    assert 'link_search_list' not in response.data.keys()
    assert response.status_code == 200

    # app = article, search_param O
    app = 'article'
    url = base_url + f'?app={app}&search_param={search_param}'
    response = client.get(url)
    assert 'article_search_list' in response.data.keys()
    assert 'club_search_list' not in response.data.keys()
    assert response.status_code == 200

    # app = chatroom, search_param O
    app = 'chatroom'
    url = base_url + f'?app={app}&search_param={search_param}'
    response = client.get(url)
    assert 'chatroom_search_list' in response.data.keys()
    assert 'article_search_list' not in response.data.keys()
    assert response.status_code == 200

    # app = link, search_param O
    app = 'link'
    url = base_url + f'?app={app}&search_param={search_param}'
    response = client.get(url)
    assert 'link_search_list' in response.data.keys()
    assert 'chatroom_search_list' not in response.data.keys()
    assert response.status_code == 200

    # app = club, search_param X
    app = 'club'
    url = base_url + f'?app={app}'
    response = client.get(path=url)
    assert response.status_code == 400

    # app = article, search_param X
    app = 'article'
    url = base_url + f'?app={app}'
    response = client.get(path=url)
    assert response.status_code == 400

    # app = chatroom, search_param X
    app = 'chatroom'
    url = base_url + f'?app={app}'
    response = client.get(path=url)
    assert response.status_code == 400

    # app = link, search_param X
    app = 'link'
    url = base_url + f'?app={app}'
    response = client.get(path=url)
    assert response.status_code == 400

    # wrong app name
    app = fake.text()
    url = base_url + f'?app={app}&search_param={search_param}'
    response = client.get(url)
    assert response.status_code == 400
