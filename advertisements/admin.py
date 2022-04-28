from django.contrib import admin

from advertisements.models import Advertisement, AdvertisementInfo

admin.site.register([Advertisement, AdvertisementInfo])