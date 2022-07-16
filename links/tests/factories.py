import factory
from faker import Faker
import factory.fuzzy

from links.models import Link, Category

fake = Faker()


class Category(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = fake.text()


class LinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Link

    title = fake.text()
    description = fake.text()
    url = fake.domain_name()
    source = factory.fuzzy.FuzzyChoice(choices=['website', 'SNS', 'article'])
    category = factory.SubFactory(Category)

    @factory.post_generation
    def source(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for s in extracted:
                self.source.add(s)

