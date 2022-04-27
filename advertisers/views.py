from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Advertiser
from .serializers import AdvertiserSerializer


class AdvertiserViewSet(viewsets.ModelViewSet):
    queryset = Advertiser.objects.all()

    def get_serializer_class(self):
        if self.action == 'advertisements':
            return AdvertiserSerializer
        else:
            return AdvertiserSerializer

    @action(detail=True, methods=['get'])
    def advertisements(self, pk):
        advertiser = Advertiser.objects.get(uid=pk)
        pass