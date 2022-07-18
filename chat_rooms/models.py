from django.db import models


class ChatRoom(models.Model):
    title = models.CharField(max_length=31)
    url = models.URLField()
    has_password = models.BooleanField(default=False)
    category = models.ForeignKey('chat_rooms.Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='chat_room')

    def __str__(self):
        return self.title


class Category(models.Model):
    class CategoryType(models.TextChoices):
        Developer = '개발자'
        ProductManger = '기획자'
        Designer = '디자이너'
    name = models.CharField(
        max_length=15,
        choices=CategoryType.choices
    )
    description = models.TextField(default='')

    @property
    def category(self):
        return self.name

    def __str__(self):
        return self.name
