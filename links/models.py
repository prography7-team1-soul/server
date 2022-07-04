from django.db import models


class Source(models.Model):
    class FieldType(models.TextChoices):
        website = '웹사이트'
        SNS = 'SNS'
        article = '아티클'
    name = models.CharField(
        max_length=15,
        choices=FieldType.choices
    )


class Category(models.Model):
    name = models.CharField(max_length=15)


class Link(models.Model):
    title = models.TextField()
    source = models.ManyToManyField('links.Source')
    category = models.ManyToManyField('links.Category')
    url = models.URLField()