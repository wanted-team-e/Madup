from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertiserViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'advertiser', AdvertiserViewSet, basename='advertisers')
urlpatterns = [
    path('', include(router.urls)),
]
