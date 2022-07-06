import factory
from faker import Faker

from articles.models import *

fake = Faker('ko-KR')

company_name = [
    '네이버' '카카오', '라인', '쿠팡', '우아한 형제들', '당근마켓', '토스'
]

tag_name = [
    '개발자', '디자이너', '취준', '코테', '포트폴리오', '공모전'
]


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = fake.text(ext_word_list=tag_name)


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = fake.text(ext_word_list=company_name)


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = fake.name()
    company = factory.SubFactory(CompanyFactory)


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    summary = fake.text()
    author = factory.SubFactory(AuthorFactory)
    url = fake.domain_name()
    image = fake.file_path(depth=3, category='image')

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for tag in extracted:
                self.tags.add(tag)
