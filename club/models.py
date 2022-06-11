from django.db import models


class RecruitmentField(models.Model):
    class FieldType(models.TextChoices):
        Developer = '개발자'
        ProductManger = '기획자'
        Designer = '디자이너'
    name = models.CharField(
        max_length=15,
        choices=FieldType.choices
    )


class Club(models.Model):
    name = models.CharField(max_length=31)
    image = models.ImageField(upload_to='club')
    club_description = models.TextField()
    recruitment_fields = models.ManyToManyField('club.RecruitmentField')
    recruitment_personnel = models.PositiveIntegerField()
    recruitment_at = models.CharField(max_length=31)
    activity_description = models.TextField()
    activity_cost = models.PositiveIntegerField()
    activity_area = models.CharField(max_length=31)
    activity_period = models.CharField(max_length=31)
    home_url = models.URLField()

    @property
    def sns(self):
        return self.sns_set.values('link')


class SNS(models.Model):
    link = models.URLField()
    club = models.ForeignKey('club.Club', on_delete=models.CASCADE)
