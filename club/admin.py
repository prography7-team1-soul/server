from django.contrib import admin

from club.models import SNS, Club, RecruitmentField

admin.site.register([SNS, Club, RecruitmentField])