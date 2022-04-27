
from rest_framework.response import Response
from rest_framework import generics, mixins
from .models import Advertiser
from .serializers import AdvertiserSerializers

"""
광고주 회원가입 : POST /api/advertiser
- 필수 값인 이메일, 주소, 이름, 핸드폰 번호를 입력받아 광고주를 생성합니다.

광고주 정보 조회 : GET /api/advertiser/:pk
- pk 값에 해당하는 광고주의 정보를 조회합니다.

광고주 정보 수정 : PUT /api/advertiser/:pk
- pk 값에 해당하는 광고주의 정보를 수정합니다.

광고주 삭제 : DELETE /api/advertiser/:pk
- pk 값에 해당하는 광고주를 삭제합니다.

광고주 광고 정보 조회 : GET /api/advertiser/:pk/advertisements
- pk 값에 해당하는 광고주의 광고 정보를 조회합니다.
"""


class AdvertiserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializers

    def post(self, request):
        return self.create(request)


class AdvertiserDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializers

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
