import factory

from accounts.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    uuid = 'test_uuid_01'
    fcm_token = 'fAevDULtAUO9g4bQRp97Vi:APA91bEgs3mlDWWuq-XvzPjy92q2Lb1zSXFACWUOFfVsSGUl1x8zQug6WNQfREjyJ29Xo0O9UE0000ynsZacmkAjPWNMt-AIFcYQIApzlNZAlXNOe_jl2dlC_rspUQhu3rX3xeR8IHoe'
