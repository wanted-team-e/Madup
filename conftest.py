import pytest

from pytest_factoryboy import register
from advertisements.tests.factories import Advertiser_Fa, Advertisement_Fa, AdvertisementInfo_Fa
from rest_framework.test import APIClient

register(Advertiser_Fa)
register(Advertisement_Fa)
register(AdvertisementInfo_Fa)

@pytest.fixture
def api_client():
    return APIClient