from django.db.models import Sum
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from advertisements.models import AdvertisementInfo
from .models import Advertiser
from .serializers import AdvertiserSerializer


class AdvertiserViewSet(viewsets.ModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

    @action(detail=True, methods=['get'])
    def statistics(self, request, pk):
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

            result = {
                'ctr': round(statistics['total_click'] * 100 / statistics['total_impression'], 2),
                'cpc': round(statistics['total_cost'] / statistics['total_click'], 2),
                'roas': round(statistics['total_cv'] * 100 / statistics['total_cost'], 2),
                'cvr': round(statistics['total_conversion'] * 100 / statistics['total_click'], 2),
                'cpa': round(statistics['total_cost'] / statistics['total_conversion'], 2),
            }
            results[media['media']] = result
        return Response(results, status=status.HTTP_200_OK)