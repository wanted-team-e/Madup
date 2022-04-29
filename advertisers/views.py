from django.db.models import Sum
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
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

        if start_date and end_date:
            try:
                advertisements = AdvertisementInfo.objects.filter(advertisement__advertiser__advertiser_uid=pk,
                                                                  date__gte=start_date, date__lte=end_date)
            except ValueError:
                return Response({'error_message': "기간은 'start_date=yyyy-mm-dd&end_date=yyyy-mm-dd' 형식으로 요청 가능합니다."},
                                status=status.HTTP_400_BAD_REQUEST)

        if not(start_date and end_date):
            advertisements = AdvertisementInfo.objects.filter(advertisement__advertiser__advertiser_uid=pk)

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
                'ctr': 0.0 if statistics['total_impression'] == 0 else round(statistics['total_click'] * 100 / statistics['total_impression'], 2),
                'roas': 0.0 if statistics['total_cost'] == 0 else round(statistics['total_cv'] / statistics['total_cost'], 2),
                'cpc': 0.0 if statistics['total_cost'] == 0 else round(statistics['total_cost'] / statistics['total_click'], 2),
                'cvr': 0.0 if statistics['total_click'] == 0 else round(statistics['total_conversion'] * 100 / statistics['total_click'], 2),
                'cpa': 0.0 if statistics['total_conversion'] == 0 else round(statistics['total_cost'] / statistics['total_conversion'], 2),
            }

            results[media['media']] = result
        return Response(results, status=status.HTTP_200_OK)

@api_view(['GET'])
def ping_pong(request):
    return Response({'server':'on'}, status=status.HTTP_200_OK)