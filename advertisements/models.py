from django.db import models
from django.http import RawPostDataException

class Advertisement(models.Model):
    advertisement_uid = models.CharField(max_length=65, unique=True)
    advertiser = models.ForeignKey('advertisers.Advertiser', on_delete=models.CASCADE)

    def __str__(self):
        return self.uid

class AdvertisementInfo(models.Model):
    advertisement = models.ForeignKey('advertisements.Advertisement', on_delete=models.CASCADE)
    cost = models.PositiveIntegerField(default=0)
    impression = models.PositiveIntegerField(default=0)
    click = models.PositiveIntegerField(default=0)
    conversion = models.PositiveIntegerField(default=0)
    cv = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class MediaType(models.TextChoices):
        NAVER = 'naver'
        KAKAO = 'kakao'
        GOOGLE = 'google'
        FACEBOOK = 'facebook'
    media = models.CharField(
        max_length=15,
        choices=MediaType.choices
    )

    @property
    def CTR(self):
        return self.click * 100 / self.impression
    
    @property
    def ROAS(self):
        return self.conversion * 100 / self.cost
    
    @property
    def CPC(self):
        return self.cost / self.click
    
    @property
    def CVR(self):
        return self.conversion * 100 / self.click
    
    @property
    def CPA(self):
        return self.cost / self.conversion
