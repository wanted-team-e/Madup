from django.db import models
# 작성자: 이형준, 강정희, 서재환, 김채욱

class Advertiser(models.Model):
    advertiser_uid = models.CharField(max_length=255, primary_key=True)
    phone_number = models.CharField(max_length=15, blank=True, default='')
    address = models.CharField(max_length=255, blank=True, default='')
    username = models.CharField(max_length=15, blank=True, default='')

    def __str__(self):
        return self.advertiser_uid