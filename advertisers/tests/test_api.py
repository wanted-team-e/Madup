
from django.urls import reverse
import pytest, json

from advertisers.models import Advertiser
from advertisements.models import Advertisement, AdvertisementInfo
# Create your tests here.

advertiser_url = reverse('advertisers-list') # /api/advertiser

pytestmark = pytest.mark.django_db


#작성자: 김채욱


class Test_view_api():

    @pytest.fixture
    def set_advertiser(self, client):
        Advertiser.objects.create(
            advertiser_uid= "13123",
            phone_number= "1",
            address= "1",
            username= "1"
        )
        self.data = {
            "advertiser_uid": "13123",
            "phone_number": "13123",
            "address": "13123",
            "username": "13123"       
        }
        

    # POST /api/advertiser
    def test_advertiser_get_post(self,client, set_advertiser):
        
        client.post(
            path=advertiser_url, 
            data=self.data
            )

        obj = Advertiser.objects.get(advertiser_uid='13123')
        print(obj)
        assert obj.advertiser_uid == '13123'


    # GET /api/advertiser/:pk
    def test_advertiser_detail_get(self,client,set_advertiser):

        advertiser_url_detail = reverse('advertisers-detail', kwargs={'pk':'13123'})

        response = client.get(advertiser_url_detail)

        print(response.content)
        assert response.status_code == 200
        assert json.loads(response.content) == {
            "advertiser_uid": "13123",
            "phone_number": "1",
            "address": "1",
            "username": "1"
        }


    # PATCH /api/advertiser/:pk
    def test_advertiser_detail_patch(self,client, set_advertiser):

        advertiser_url_detail = reverse('advertisers-detail', kwargs={'pk':'13123'})

        req = client.patch(path=advertiser_url_detail, data={
            "advertiser_uid": "13123",
            "phone_number": "13123",
            "address": "13123",
            "username": "777"
        }, content_type='application/json')


        response = client.get(advertiser_url_detail)
        print(req)
        assert response.status_code == 200
        assert json.loads(response.content) == {
            "advertiser_uid": "13123",
            "phone_number": "13123",
            "address": "13123",
            "username": "777"
        }




    # PUT /api/advertiser/:pk
    def test_advertiser_detail_put(self,client,set_advertiser):

        advertiser_url_detail = reverse('advertisers-detail', kwargs={'pk':'13123'})

        req = client.put(path=advertiser_url_detail, data={
            "advertiser_uid": "13123",
            "phone_number": "777",
            "address": "777",
            "username": "777"
        }, content_type='application/json')
        
        advertiser_url_detail = reverse('advertisers-detail', kwargs={'pk':'13123'})

        response = client.get(advertiser_url_detail)
        
        assert response.status_code == 200
        assert json.loads(response.content) == {
            "advertiser_uid": "13123",
            "phone_number": "777",
            "address": "777",
            "username": "777"
        }


    # DELETE /api/advertiser/:pk
    def test_advertiser_detail_delete(self,client,set_advertiser):

        advertiser_url_detail = reverse('advertisers-detail', kwargs={'pk':'13123'})

        req = client.delete(advertiser_url_detail)

        assert req.status_code == 204


    # GET /api/advertiser/pk/statistics
    def test_advertiser_detail_statistics(self,client):
        
        obj = Advertiser.objects.create(
            advertiser_uid= "1",
            phone_number= "1",
            address= "1",
            username= "1"
        )

        obj1 = Advertisement.objects.create(
            advertisement_uid='1',
            advertiser=obj
        )

        obj2 = Advertisement.objects.create(
            advertisement_uid='2',
            advertiser=obj
        )

        info1 = AdvertisementInfo.objects.create(
            advertisement=obj1,
            cost=100,
            impression=10,
            click=3,
            conversion=1,
            cv=1000,
            date='2019-01-01',
            media='naver'
        )

        info2 = AdvertisementInfo.objects.create(
            advertisement=obj2,
            cost=100,
            impression=10,
            click=3,
            conversion=1,
            cv=1000,
            date='2019-01-02',
            media='naver'
        )

        res = client.get(path='http://127.0.0.1:8000/api/advertiser/1/statistics')
        print(res)
        assert res.status_code == 200




    # GET /api/advertiser/pk/statics/?start_date=yyyy-mm-dd&end_date=yyyy-mm-dd
    def test_advertiser_detail_time(self,client):
        
        obj = Advertiser.objects.create(
            advertiser_uid= "1",
            phone_number= "1",
            address= "1",
            username= "1"
        )

        obj1 = Advertisement.objects.create(
            advertisement_uid='1',
            advertiser=obj
        )

        obj2 = Advertisement.objects.create(
            advertisement_uid='2',
            advertiser=obj
        )

        info1 = AdvertisementInfo.objects.create(
            advertisement=obj1,
            cost=100,
            impression=10,
            click=3,
            conversion=1,
            cv=1000,
            date='2019-01-01',
            media='naver'
        )

        info2 = AdvertisementInfo.objects.create(
            advertisement=obj2,
            cost=100,
            impression=10,
            click=3,
            conversion=1,
            cv=1000,
            date='2019-01-02',
            media='naver'
        )

        res = client.get(path='http://127.0.0.1:8000/api/advertiser/1/statistics?start_date=2019-01-01&end_date=2019-01-02')
        print(res)
        assert res.status_code == 200




    # Post 중복 데이터 방지
    def test_duplicate_post_method(self,client,set_advertiser):
        
        request = client.post(path=advertiser_url, 
        data={
            "advertiser_uid": "13123",
            "phone_number": "1",
            "address": "1",
            "username": "1"
        })

        assert request.status_code == 400
        assert json.loads(request.content) == {
        "advertiser_uid": [
            "advertiser with this advertiser uid already exists."
        ]}


