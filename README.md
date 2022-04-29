# 매드업 기업과제

## 과제설명
주어진 데이터 셋을 요구사항 대로 서빙하기 위한 관계형 데이터베이스 테이블을 설계하고, 주어진 기능을 제공하는 REST API 서
버를 개발하세요.


### 과제 구현 세부 구성요소는 아래와 같습니다.

### 구성 요소
- **광고주(Advertiser)**
  - advertiser_uid : 광고주 고유 id값
  - username : 광고주 이름
  - phone_number : 핸드폰 번호
  - address : 주소
- **광고(Advertisement)**
  - uid : 광고 고유 id값
  - advertiser : 광고주
  - media : 광고매체
  - cost : 비용
  - impression : 노출수
  - click : 클릭수
  - conversion : 구매전환수
  - cv : 구매전환에 따른 매출액
  - date : 광고 일자

### 기능
#### advertiser 관련
**광고주 생성 : POST /api/advertiser**
- 필수 값인 주소, 이름, 핸드폰 번호를 입력받아 광고주를 생성합니다.

**광고주 정보 조회** : GET /api/advertiser/:pk
- pk 값에 해당하는 광고주의 정보를 조회합니다.

**광고주 정보 수정** : PUT /api/advertiser/:pk
- pk 값에 해당하는 광고주의 정보를 수정합니다.

**광고주 삭제** : DELETE /api/advertiser/:pk
- pk 값에 해당하는 광고주를 삭제합니다.


**광고주 미디어별 광고 통계 조회 - 기간 필터링** : GET /api/advertiser/:pk/statistics?start_date=yyyy-mm-dd&end_date=yyyy-mm-dd
- pk 값에 해당하는 광고주의 미디어별 광고 통계 정보를 파라미터로 넘어온 기간에 따라 필터링하여 조회합니다.

