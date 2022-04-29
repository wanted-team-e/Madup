from advertisements.models import Advertisement, AdvertisementInfo
import pytest


pytestmark = pytest.mark.django_db


# Advertiser model 확인
def test_advertisment_instance(advertiser_fa):
    
    obj = advertiser_fa.create(phone_number='123')
    print(obj)
    assert obj.phone_number == '123'


# Advertisement model 확인
def test_advertisment_instance(advertisement_fa):
    
    obj = advertisement_fa.create(phone_number='123')
    print(obj)
    assert obj.phone_number == '123'


# AdvertisementInfo model 확인
def test_advertisment_instance(advertiser_fa):
    
    obj = advertiser_fa.create(phone_number='123')
    print(obj)
    assert obj.phone_number == '123'



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