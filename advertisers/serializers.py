from rest_framework import serializers

from advertisers.models import Advertiser


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = (
            'advertiser_uid',
            'phone_number',
            'address',
            'username',
        )