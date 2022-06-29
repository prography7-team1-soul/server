from django.db import models
import datetime


class SubRecruitmentField(models.Model):
    class FieldType(models.Model):
        class FieldType(models.TextChoices):



class MainRecruitmentField(models.Model):
    class FieldType(models.TextChoices):
        Developer = '개발자'
        ProductManger = '기획자'
        Designer = '디자이너'
    name = models.CharField(
        max_length=15,
        choices=FieldType.choices
    )


class Education(models.Model):
    name = models.CharField(max_length=31)
    image = models.ImageField(upload_to='club')
    description = models.TextField()
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

    @property
    def is_recruitment(self):
        today = datetime.date.today()
        recruitment_day = self.recruitment_at.split(' ')[0]
        _result = (today - recruitment_day).days
        return _result < 0

class SNS(models.Model):
    link = models.URLField()
    club = models.ForeignKey('educations.Education', on_delete=models.CASCADE)
