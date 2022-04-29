from django.db.models import Sum
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from advertisements.models import AdvertisementInfo
from .models import Advertiser
from .serializers import AdvertiserSerializer

import time

class AdvertiserViewSet(viewsets.ModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

    @action(detail=True, methods=['get'])
    def statistics(self, request, pk):

        start_time = time.time()

        # start_date, end_date
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)

        advertisements = AdvertisementInfo.objects.filter(advertisement__advertiser__advertiser_uid=pk, date__gte=start_date, date__lte=end_date)
        media_list = advertisements.values('media').distinct()
        results = {}
        for media in media_list:
            statistics = advertisements.filter(media=media['media']).aggregate(
                total_cost=Sum('cost'),
                total_impression=Sum('impression'),
                total_click=Sum('click'),
                total_conversion=Sum('conversion'),
                total_cv=Sum('cv'),
            )
            
            # zero division error 처리 부탁드려요
            result = {
                'ctr': 0 if statistics['total_impression'] == 0 else round(statistics['total_click'] * 100 / statistics['total_impression'], 2),
                'roas': 0 if statistics['total_cost'] == 0 else round(statistics['total_cv'] / statistics['total_cost'], 2),
                'cpc': 0 if statistics['total_cost'] == 0 else round(statistics['total_cost'] / statistics['total_click'], 2),
                'cvr': 0 if statistics['total_click'] == 0 else round(statistics['total_conversion'] * 100 / statistics['total_click'], 2),
                'cpa': 0 if statistics['total_conversion'] == 0 else round(statistics['total_cost'] / statistics['total_conversion'], 2),
            }

            results[media['media']] = result
        
        end_time = time.time()

        print("WorkingTime: {} sec".format(end_time-start_time))
        return Response(results, status=status.HTTP_200_OK)