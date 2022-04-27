from django.contrib import admin

# Register your models here.
from advertisements.models import Advertisements, AdvertisementsInfo, Media

admin.site.register([Advertisements, AdvertisementsInfo, Media])