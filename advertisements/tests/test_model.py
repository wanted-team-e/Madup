from django.urls import reverse
from advertisements.models import Advertisement, AdvertisementInfo
import pytest



# advertisement_url = reverse('')
pytestmark = pytest.mark.django_db


# Advertisements model 확인
def test_advertisment_instance(client, Advertisement_Fa):

    data = Advertisement_Fa
    
    obj = Advertisement.objects.create(advertisement_uid='entry', advertiser=data)
    assert obj.advertisement_uid == 'entry'


# Advertisements_info constraint 확인 
@pytest.mark.parametrize(
    "advertisement, cost, impression, click, conversion, cv, media, validity",
    [
        ('1', 100, 10, 3, 1, 1000, 'naver', True),
        ('', 100, 10, 3, 1, 1000, 'naver', False),
        ('1', '', 10, 3, 1, 1000, 'naver', True),
        ('1', 100, '', 3, 1, 1000, 'naver', True),
        ('1', 100, 10, '', 1, 1000, 'naver', True),
        ('1', 100, 10, 3, '', 1000, 'naver', True),
        ('1', 100, 10, 3, 1, '', 'naver', True),
        ('1', 100, 10, 3, 1, 1000, '', True),
    ],
)
def test_advertismentinfo_instance(
    AdvertisementInfo_Fa, advertisement ,cost, impression, click, conversion, cv, media, validity
):
    test = AdvertisementInfo_Fa(
        advertisement=advertisement,
        cost=cost,
        impression=impression,
        click=click,
        conversion=conversion,
        cv=cv,
        media=media
    )

    item = AdvertisementInfo.objects.all().count()
    print(item)
    assert item == validity