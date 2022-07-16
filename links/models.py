from django.db import models


class SourceField(models.Model):
    class FieldType(models.TextChoices):
        WebSite = '웹사이트'
        SNS = 'SNS'
        Article = '아티클'
    name = models.CharField(
        max_length=15,
        choices=FieldType.choices
    )


class Category(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(default='')

    @property
    def category(self):
        return self.name


class Link(models.Model):
    title = models.TextField()
    description = models.TextField()
    source = models.ManyToManyField('links.SourceField')
    category = models.ForeignKey('links.Category', on_delete=models.PROTECT)
    url = models.URLField()
