from datetime import datetime
import os
import django
import csv
import sys

# system setup
os.chdir('.')
print('Current dir의 경로 : ', end=''), print(os.getcwd())  # os가 파악한 현재 경로를 표기
print('os.path.abspath(__file__)의 경로 : ', os.path.abspath(__file__))  # 현재 작업중인 파일을 포함 경로를 구체적으로 표기
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print('BASE_DIR=', end=''), print(BASE_DIR)
print('똑같나? 다르나?', BASE_DIR == os.getcwd())  # 소문자 c , 대문자 C 차이 때문인것 같네요.

sys.path.append(BASE_DIR) # sys 모듈은 파이썬을 설치할 때 함께 설치되는 라이브러리 모듈이다. sys에 대해서는 뒤에서 자세하게 다룰 것이다. 이 sys 모듈을 사용하면 파이썬 라이브러리가 설치되어 있는 디렉터리를 확인할 수 있다.

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
# python이 실행될 때 DJANGO_SETTINGS_MODULE라는 환경 변수에
# 현재 프로젝트의 settings.py 파일 경로를 등록
django.setup() # python manage.py shell 을 실행하는 것이랑 비슷한 방법이다. 즉 파이썬 파일에서도 django를 실행 시킬수 있다.

# script 한글깨짐
# import sys
# import io
#
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 시스템 환경변수-시스템 변수 추가 PYTHONIOENCODING / utf-8



from django.conf import settings
from advertisers.models import *
from advertisements.models import *

base_path = settings.DATA_ROOT_URL + settings.DATA_URL # == './data/'
csv_path = base_path + 'Madup_Wanted_Data_set.csv'
print(f'csv_path: {csv_path}')

def insert_advertiser() :
    with open(csv_path, newline = "", encoding = "utf-8") as csvfile :
        data_reader = csv.DictReader(csvfile)

        Advertiser.objects.all().delete()
        for row in data_reader:
            if row['advertiser_uid']:
                Advertiser.objects.create(advertiser_uid = row['advertiser_uid'])

    print('Advertiser DATA UPLOADED SUCCESSFULY!')

def insert_advertisement() :
    with open(csv_path, newline = "", encoding = "utf-8") as csvfile :
        data_reader = csv.DictReader(csvfile)

        Advertisement.objects.all().delete()
        for row in data_reader:
            if row['uid_filter']:
                Advertisement.objects.create(advertisement_uid = row['uid_filter'],
                                            advertiser_id = row['advertiser_filter'])

    print('Advertisement DATA UPLOADED SUCCESSFULY!')

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
