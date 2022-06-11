from django.db import models


class Part(models.Model):
    class FieldType(models.TextChoices):
        Developer = '개발자'
        ProductManger = '기획자'
        Designer = '디자이너'
    name = models.CharField(
        max_length=15,
        choices=FieldType.choices
    )


class Tag(models.Model):
    name = models.CharField(max_length=7)


class Author(models.Model):
    name = models.CharField(max_length=15)
    company = models.ForeignKey('articles.Company', on_delete=models.PROTECT)
    part = models.ManyToManyField('articles.Part')


class Article(models.Model):
    summary = models.TextField()
    author = models.ForeignKey('articles.Author', on_delete=models.SET_NULL, null=True)
    url = models.URLField()
    tags = models.ManyToManyField('articles.Tag')
    image = models.ImageField(upload_to='articles')


class Company(models.Model):
    name = models.CharField(max_length=31)
