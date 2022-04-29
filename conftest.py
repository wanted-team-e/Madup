import pytest

from pytest_factoryboy import register
from advertisements.tests.factories import AdvertiserFa, AdvertisementFa, AdvertisementInfoFa
from rest_framework.test import APIClient

register(AdvertiserFa)
register(AdvertisementFa)
register(AdvertisementInfoFa)

@pytest.fixture
def api_client():
    return APIClient

@pytest.fixture
def api_client():
    return APIClient