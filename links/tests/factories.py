import factory
from faker import Faker
import factory.fuzzy

from links.models import Link

fake = Faker()


class LinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Link

    title = fake.text()
    url = fake.domain_name()
    source = factory.fuzzy.FuzzyChoice(choices=['website', 'SNS', 'article'])

    @factory.post_generation
    def source(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for s in extracted:
                self.source.add(s)

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for c in extracted:
                self.category.add(c)
