from django.db import models


class ChatRoom(models.Model):
    title = models.CharField(max_length=31)
    url = models.URLField()
    has_password = models.BooleanField(default=False)
    categories = models.ManyToManyField('chat_rooms.Category')

    @property
    def category_list(self):
        return self.category_set.values('name')


class Category(models.Model):
    class CategoryType(models.TextChoices):
        Developer = '개발자'
        ProductManger = '기획자'
        Designer = '디자이너'
    name = models.CharField(
        max_length=15,
        choices=CategoryType.choices
    )
