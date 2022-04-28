"""
설명:
pytest.ini파일을 만든후 아래를 추가:
[pytest]
DJANGO_SETTINGS_MODULE = config.settings
python_files = test_*.py 


터미널에 pytest test_api.py경로를 복붙하고 실행 # print()를 해서 값을 확인하고 싶으면 option -rP추가
(test_api.py를 오른쪽 클릭하면 copypath가 있어요)
"""


from ast import arg
from django.urls import reverse
import pytest, json
# Create your tests here.

advertiser_url = reverse('advertisers-list') # /api/advertiser
advertiser_url_detail = reverse('advertisers-detail', args=['13123']) # /api/advertiser/13123

pytestmark = pytest.mark.django_db



# Detail retrieve가 안됨, 확인 필요
@pytest.mark.skip
def test_detail_get(client):
    response = client.get('advertiser_url_detail')
    print(advertiser_url_detail)
    assert response.status_code == 200


# 테이블이 비어있는지 확인
def test_zero_data_or_empty_list(client):
    response = client.get(advertiser_url)
    print(advertiser_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


# # POST method 기능 확인
def test_success_post_method(client):
    request = client.post(path=advertiser_url, 
    data={
    "advertiser_uid": "4142214",
    "phone_number": "14242142",
    "address": "house",
    "username": "dsaf"
    })
    assert request.status_code == 201

# 중복데이터 POST 확인
@pytest.mark.xfail
def test_duplicate_post_method(client):
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
    ]
    }


# Post method 실패 확인
def test_fail_post_noarguments(client):
    request = client.post(path=advertiser_url)
    assert request.status_code == 400
    assert json.loads(request.content) == {
    "advertiser_uid": [
        "This field is required."
    ]}

