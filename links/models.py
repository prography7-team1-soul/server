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

    @property
    def category(self):
        return self.name


class Link(models.Model):
    title = models.TextField()
    source = models.ManyToManyField('links.Source')
    category = models.ForeignKey('links.Category', on_delete=models.PROTECT)
    url = models.URLField()
