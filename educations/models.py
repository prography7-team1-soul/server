from django.db import models
from datetime import datetime
import datetime as date


class RecruitmentField(models.Model):
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


class Education(models.Model):
    name = models.CharField(max_length=31)
    image = models.ImageField(upload_to='educations')
    description = models.TextField()
    recruitment_fields = models.ManyToManyField('educations.RecruitmentField')
    recruitment_personnel = models.PositiveIntegerField()
    recruitment_at = models.CharField(max_length=31)
    education_description = models.TextField()
    education_cost = models.TextField()
    education_area = models.CharField(max_length=31)
    education_period = models.CharField(max_length=31)
    home_url = models.URLField()
    detail_image = models.ImageField(default='')

    @property
    def sns(self):
        return self.sns_set.values('link', 'image')

    @property
    def is_recruitment(self):
        today = date.datetime.today()
        recruitment_day = self.recruitment_at.split(' ')[0]
        recruitment_day = datetime.strptime(recruitment_day, "%Y-%m-%d")
        _result = (today - recruitment_day).days
        return _result < 0

    def __str__(self):
        return self.name


class SNS(models.Model):
    link = models.URLField()
    club = models.ForeignKey('educations.Education', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='educations')

    def __str__(self):
        return f'{self.club.name}교육 SNS'
