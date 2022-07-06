from django.contrib import admin
from .models import SNS, Education, RecruitmentField
# Register your models here.
admin.site.register([SNS, Education, RecruitmentField])