import factory
from faker import Faker

fake = Faker()

from advertisements.models import Advertisement, AdvertisementInfo
from advertisers.models import Advertiser


class Advertiser_Fa(factory.django.DjangoModelFactory):
    class Meta:
        model = Advertiser

    advertiser_uid = fake.name()


class Advertisement_Fa(factory.django.DjangoModelFactory):
    class Meta:
        model = Advertisement

    advertisement_uid = fake.name()
    advertiser = factory.SubFactory(Advertiser_Fa)


class AdvertisementInfo_Fa(factory.django.DjangoModelFactory):
    class Meta:
        model = AdvertisementInfo
    
    advertisement = factory.SubFactory(Advertisement_Fa)
    cost = 100
    impression = 10
    click = 3
    conversion = 1
    cv = 10000
    media = 'naver'