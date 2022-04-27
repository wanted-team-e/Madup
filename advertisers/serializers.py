from rest_framework import serializers
from advertisers.models import Advertiser
from advertisements.models import 광고테이블

class Advertisements(serializers.ModelSerializer):
    class Meta:
        model = 광고테이블
        fields = '__all__'


class AdvertiserSerializers(serializers.ModelSerializer):

    advertisements = Advertisements(read_only=True, many=True)

    class Meta:
        model = Advertiser
        fields = ['__all__']