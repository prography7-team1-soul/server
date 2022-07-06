import pytest

from articles.models import Article
from articles.tests.factories import ArticleFactory

pytestmark = pytest.mark.django_db

@pytest.fixture
def article_factory():
    article_factory = ArticleFactory()
    return article_factory


def test_article_factory(article_factory):
    assert isinstance(article_factory, Article)
