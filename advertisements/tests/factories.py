import factory
from faker import Faker

fake = Faker()

from advertisements.models import Advertisement, AdvertisementInfo
from advertisers.models import Advertiser


class AdvertiserFa(factory.django.DjangoModelFactory):
    class Meta:
        model = Advertiser

    advertiser_uid = fake.name()


class AdvertisementFa(factory.django.DjangoModelFactory):
    class Meta:
        model = Advertisement

    advertisement_uid = '1'
    advertiser = factory.SubFactory(AdvertiserFa)


class AdvertisementInfoFa(factory.django.DjangoModelFactory):
    class Meta:
        model = AdvertisementInfo
    
    advertisement = factory.SubFactory(AdvertisementFa)
    cost = 100
    impression = 10
    click = 3
    conversion = 1
    cv = 10000
    media = 'naver'