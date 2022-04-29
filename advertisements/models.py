from django.db import models
# 작성자: 이형준, 강정희, 서재환, 김채욱
class Advertisement(models.Model):
    advertisement_uid = models.CharField(max_length=65, primary_key=True)
    advertiser = models.ForeignKey('advertisers.Advertiser', on_delete=models.CASCADE)

    def __str__(self):
        return self.advertisement_uid

    class Meta:
        indexes = [
            models.Index(fields=['advertiser']),
        ]

class AdvertisementInfo(models.Model):
    advertisement = models.ForeignKey('advertisements.Advertisement', on_delete=models.CASCADE)
    cost = models.PositiveIntegerField(default=0)
    impression = models.PositiveIntegerField(default=0)
    click = models.PositiveIntegerField(default=0)
    conversion = models.PositiveIntegerField(default=0)
    cv = models.PositiveIntegerField(default=0)
    date = models.DateField(db_index=True)

    class MediaType(models.TextChoices):
        NAVER = 'naver'
        KAKAO = 'kakao'
        GOOGLE = 'google'
        FACEBOOK = 'facebook'
    media = models.CharField(
        max_length=15,
        choices=MediaType.choices
    )

    class Meta:
        indexes = [
            models.Index(fields=['advertisement' ,'date'] ),
        ]
