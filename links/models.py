from django.db import models

from accounts.utils import TimeStampedModel


class Tag(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(default='')

    @property
    def category(self):
        return self.name

    def __str__(self):
        return self.name


class Link(TimeStampedModel):
    title = models.TextField()
    tags = models.ManyToManyField('links.Tag')
    source = models.ForeignKey('links.Source', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('links.Category', on_delete=models.PROTECT)
    url = models.URLField()

    def __str__(self):
        return self.title

    @property
    def source_name(self):
        return self.source.name
