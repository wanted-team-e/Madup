"""
설명:
pytest.ini파일을 만든후 아래를 추가:
[pytest]
DJANGO_SETTINGS_MODULE = config.settings

터미널에 pytest -s -v test_api.py경로를 복붙하고 실행
(test_api.py를 오른쪽 클릭하면 copypath가 있어요)
"""


from django.urls import reverse
import pytest, json
# Create your tests here.

advertiser_url = reverse('advertisers-list')
advertiser_url_detail = reverse('advertisers-detail', args = ['12412'])
pytestmark = pytest.mark.django_db


# Detail 값 get 확인
def test_detail_get(client):
    response = client.get(advertiser_url_detail)
    assert response.status_code == 200



# 데이터베이스가 비어있는지 확인
def test_zero_data_or_empty_list(client):
    response = client.get(advertiser_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []
    print(advertiser_url_detail)


# # POST method 기능 확인
def test_success_post_method(client):
    response = client.post(path=advertiser_url, 
    data={
    "advertiser_uid": "4142214",
    "phone_number": "14242142",
    "address": "house",
    "username": "dsaf"
    })
    assert response.status_code == 201

# 중복데이터 POST 확인
@pytest.mark.xfail
def test_duplicate_post_method(client):
    response = client.post(path=advertiser_url, 
    data={
    "advertiser_uid": "4142214",
    "phone_number": "14242142",
    "address": "house",
    "username": "dsaf"
    })
    assert response.status_code == 400
    assert json.loads(response.content) == {
    "advertiser_uid": [
        "advertiser with this advertiser uid already exists."
    ]
    }


# # Post method 실패 확인
def test_fail_post_noarguments(client):
    response = client.post(path=advertiser_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {
    "advertiser_uid": [
        "This field is required."
    ]
    }