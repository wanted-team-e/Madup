import pytest

from pytest_factoryboy import register
from advertisements.tests.factories import Advertiser_Fa, Advertisement_Fa, AdvertisementInfo_Fa


register(Advertiser_Fa)
register(Advertisement_Fa)
register(AdvertisementInfo_Fa)

