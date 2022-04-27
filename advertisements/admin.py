from django.contrib import admin

from advertisements.models import Advertisements, AdvertisementsInfo, Media

admin.site.register([Advertisements, AdvertisementsInfo, Media])