from rest_framework import serializers

from advertisements.models import AdvertisementsInfo
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
        model = AdvertisementsInfo
        fields = (
            ''
        )
