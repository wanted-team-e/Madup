from rest_framework import serializers

from advertisements.models import AdvertisementInfo
from advertisers.models import Advertiser


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = (
            'id',
            'email',
            'phone_number',
            'address',
            'name',
        )

class RelatedAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementInfo
        fields = (
            ''
        )
