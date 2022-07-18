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

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=15)
    company = models.ForeignKey('articles.Company', on_delete=models.PROTECT)
    part = models.ForeignKey('articles.Part', on_delete=models.CASCADE)

    @property
    def author_name(self):
        return self.name

    @property
    def author_company(self):
        return self.company.name

    @property
    def author_part(self):
        return self.part.name

    def __str__(self):
        return self.name


class Article(models.Model):
    summary = models.TextField()
    author = models.ForeignKey('articles.Author', on_delete=models.SET_NULL, null=True)
    url = models.URLField()
    tags = models.ManyToManyField('articles.Tag', blank=True)
    image = models.ImageField(upload_to='articles')

    def __str__(self):
        return self.summary


class Company(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name
