from django.urls import path, include
from . import views



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



urlpatterns = [
    path('advertiser/',views.AdvertiserList.as_view()),
    path('advertiser/<int:pk>/', views.AdvertiserDetail.as_view()),
    # path('advertiser/<int:pk>/advertisements/')
]
