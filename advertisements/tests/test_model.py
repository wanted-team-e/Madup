from advertisements.models import Advertisement, AdvertisementInfo
import pytest


pytestmark = pytest.mark.django_db


# Advertiser model 확인
def test_advertiser_instance(advertiser_fa):
    
    obj = advertiser_fa.create(phone_number='123')
    print(obj)
    assert obj.phone_number == '123'


# Advertisement model 확인
def test_advertisment_instance(advertisement_fa):
    
    obj = advertisement_fa.create()
    print(obj.advertiser )
    assert obj.advertisement_uid == '1'


# AdvertisementInfo model 확인
def test_advertismentinfo_instance(advertisement_info_fa):
    
    obj = advertisement_info_fa.create()
    print(obj)
    assert obj.media == 'naver'



# Advertisements_info constraint 확인 
@pytest.mark.skip
@pytest.mark.parametrize(
    "advertisement, cost, impression, click, conversion, cv, date ,media, validity",
    [
        ('1', 100, 10, 3, 1, 1000, '1997-10-19' ,'naver', True),
        ('', '100', '10', '3', '1', '1000', '1997-10-19' ,'naver', True),
    ],
)
def test_advertismentinfo_instance(
    advertisement_info_fa, advertisement, cost, impression, click, conversion, cv, date ,media, validity
):
    obj = advertisement_info_fa(
        advertisement_id=advertisement,
        cost=cost,
        impression=impression,
        click=click,
        conversion=conversion,
        cv=cv,
        date=date,
        media=media
    )

    item = AdvertisementInfo.objects.all().count()
    assert item == validity