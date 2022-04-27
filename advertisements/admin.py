from django.contrib import admin

from advertisements.models import Advertisements, AdvertisementsInfo

admin.site.register([Advertisements, AdvertisementsInfo])