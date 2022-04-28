from rest_framework import viewsets
from .models import Advertiser
from .serializers import AdvertiserSerializer


class AdvertiserViewSet(viewsets.ModelViewSet):
    queryset = Advertiser.objects.all()

    def get_serializer_class(self):
        if self.action == 'advertisements':
            return AdvertiserSerializer
        else:
            return AdvertiserSerializer

