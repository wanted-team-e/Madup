from rest_framework import serializers
from advertisers.models import Advertiser


class AdvertiserSerializers(serializers.ModelSerializer):

    class Meta:
        model = Advertiser
        fields = (
            ''
        )