from django.db import models

class Advertisements(models.Model):
    uid = models.CharField(max_length=65, unique=True)
    advertiser = models.ForeignKey('advertisers.Advertiser', on_delete=models.CASCADE)

    def __str__(self):
        return self.uid

class AdvertisementsInfo(models.Model):
    advertisement = models.ForeignKey('advertisements.Advertisements', on_delete=models.CASCADE)
    media = models.ForeignKey('advertisements.Media', on_delete=models.CASCADE)
    cost = models.PositiveIntegerField()
    impression = models.PositiveIntegerField()
    click = models.PositiveIntegerField()
    conversion = models.PositiveIntegerField()
    cv = models.PositiveIntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()



class Media(models.Model):
    class MediaType(models.TextChoices):
        NAVER = 'naver'
        KAKAO = 'kakao'
        GOOGLE = 'google'
        FACEBOOK = 'facebook'

    name = models.CharField(
        max_length=15,
        choices=MediaType.choices
    )

    def __str__(self):
        return self.name