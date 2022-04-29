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

    def update(self, instance, validated_data):
        if validated_data['advertiser_uid'] != instance.advertiser_uid:
            raise serializers.ValidationError({'error_message':'광고주의 uid 값은 수정할수 없습니다.'})
        return super().update(instance, validated_data)