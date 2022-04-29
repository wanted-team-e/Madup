from datetime import datetime
import os
import django
import csv

# 작성자: 강정희

# system setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings.develop')
django.setup()

from django.conf import settings
from advertisers.models import *
from advertisements.models import *

# db upload
base_path = settings.DATA_ROOT_URL + settings.DATA_URL
csv_path = base_path + 'Madup_Wanted_Data_set.csv'

# advertiser
def insert_advertiser() :
    with open(csv_path, newline = "", encoding = "utf-8") as csvfile :
        data_reader = csv.DictReader(csvfile)

        Advertiser.objects.all().delete()
        for row in data_reader:
            if row['advertiser_uid']:
                Advertiser.objects.create(advertiser_uid = row['advertiser_uid'])

    print('Advertiser DATA UPLOADED SUCCESSFULY!')

# advertisement
def insert_advertisement() :
    with open(csv_path, newline = "", encoding = "utf-8") as csvfile :
        data_reader = csv.DictReader(csvfile)

        Advertisement.objects.all().delete()
        for row in data_reader:
            if row['uid_filter']:
                Advertisement.objects.create(advertisement_uid = row['uid_filter'],
                                             advertiser_id = row['advertiser_filter'])

    print('Advertisement DATA UPLOADED SUCCESSFULY!')

# advertisement info
def insert_advertisement_info() :
    with open(csv_path, newline = "", encoding = "utf-8") as csvfile :
        data_reader = csv.DictReader(csvfile)

        AdvertisementInfo.objects.all().delete()
        for row in data_reader:
            if row['advertiser']:
                AdvertisementInfo.objects.get_or_create(advertisement_id = row['uid'],
                                                 media = row['media'],
                                                 cost = int(row['cost']),
                                                 impression = int(row['impression']),
                                                 click = int(row['click']),
                                                 conversion = int(row['conversion']),
                                                 cv = int(row['cv']),
                                                 date=datetime.strptime(row['date'], "%Y.%m.%d"),
                                                 )


    print('AdvertisementInfo DATA UPLOADED SUCCESSFULY!')

insert_advertiser()
insert_advertisement()
insert_advertisement_info()
