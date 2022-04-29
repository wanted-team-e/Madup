"""
설명:
pytest.ini파일을 만든후 아래를 추가:
[pytest]
DJANGO_SETTINGS_MODULE = config.settings
python_files = test_*.py 


터미널에 pytest test_api.py경로를 복붙하고 실행 # print()를 해서 값을 확인하고 싶으면 option -rP추가
(test_api.py를 오른쪽 클릭하면 copypath가 있어요)
"""


from django.urls import reverse
import pytest, json

from ..models import Advertiser
# Create your tests here.

advertiser_url = reverse('advertisers-list') # /api/advertiser

pytestmark = pytest.mark.django_db

"""
작성자: 김채욱 - 테스트 코드 작성
"""


# POST /api/advertiser
def test_advertiser_get_post():

    Advertiser.objects.create(
        advertiser_uid= "13123",
        phone_number= "1231312",
        address= "sdfsdf",
        username= "1"
    )

    obj = Advertiser.objects.get(advertiser_uid='13123')
    print(obj)
    assert obj.advertiser_uid == '13123'


# GET /api/advertiser/:pk
def test_advertiser_detail_get(client):
    client.post(path=advertiser_url, data={
        "advertiser_uid": "13123",
        "phone_number": "13123",
        "address": "13123",
        "username": "13123"
    })
    
    advertiser_url_detail = reverse('advertisers-detail', kwargs={'pk':'13123'})

    response = client.get(advertiser_url_detail)

    print(response.content)
    assert response.status_code == 200
    assert json.loads(response.content) == {
        "advertiser_uid": "13123",
        "phone_number": "13123",
        "address": "13123",
        "username": "13123"
    }


# PATCH /api/advertiser/:pk
def test_advertiser_detail_patch(client):
    client.post(path=advertiser_url, data={
        "advertiser_uid": "13123",
        "phone_number": "13123",
        "address": "13123",
        "username": "13123"
    })

    advertiser_url_detail = reverse('advertisers-detail', kwargs={'pk':'13123'})

    req = client.patch(path=advertiser_url_detail, data={
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
def test_advertiser_detail_put(client):
    client.post(path=advertiser_url, data={
        "advertiser_uid": "13123",
        "phone_number": "13123",
        "address": "13123",
        "username": "13123"
    })

    advertiser_url_detail = reverse('advertisers-detail', kwargs={'pk':'13123'})

    req = client.patch(path=advertiser_url_detail, data={
        "advertiser_uid": "777",
        "phone_number": "777",
        "address": "777",
        "username": "777"
    }, content_type='application/json')
    
    advertiser_url_detail = reverse('advertisers-detail', kwargs={'pk':'777'})

    response = client.get(advertiser_url_detail)
    
    assert response.status_code == 200
    assert json.loads(response.content) == {
        "advertiser_uid": "777",
        "phone_number": "777",
        "address": "777",
        "username": "777"
    }


# DELETE /api/advertiser/:pk
def test_advertiser_detail_delete(client):
    client.post(path=advertiser_url, data={
        "advertiser_uid": "13123",
        "phone_number": "13123",
        "address": "13123",
        "username": "13123"
    })

    advertiser_url_detail = reverse('advertisers-detail', kwargs={'pk':'13123'})

    req = client.delete(advertiser_url_detail)

    assert req.status_code == 204




# Post 중복 데이터 방지
@pytest.mark.xfail
def test_duplicate_post_method(client):
    client.post(path=advertiser_url, 
    data={
        "advertiser_uid": "4142214",
        "phone_number": "14242142",
        "address": "house",
        "username": "dsaf"
    })

    request = client.post(path=advertiser_url, 
    data={
        "advertiser_uid": "4142214",
        "phone_number": "14242142",
        "address": "house",
        "username": "dsaf"
    })

    assert request.status_code == 400
    assert json.loads(request.content) == {
    "advertiser_uid": [
        "advertiser with this advertiser uid already exists."
    ]}


# Post pk 확인
def test_fail_post_noarguments(client):
    request = client.post(path=advertiser_url, 
        data={
            "advertiser_uid": "",
            "phone_number": "14242142",
            "address": "house",
            "username": "dsaf"
    })


    assert request.status_code == 400
    assert json.loads(request.content) == {
    "advertiser_uid": [
        "This field is required."
    ]}

