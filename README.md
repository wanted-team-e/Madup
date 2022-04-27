# 매드업 기업과제

## 과제설명
주어진 데이터 셋을 요구사항 대로 서빙하기 위한 관계형 데이터베이스 테이블을 설계하고, 주어진 기능을 제공하는 REST API 서
버를 개발하세요.


###과제 구현 세부 구성요소는 아래와 같습니다.

### 구성 요소
- **광고주(Advertiser)**
  - email : 이메일
  - password : 비밀번호
  - phone_number : 핸드폰 번호
  - address : 주소
- **광고(Advertisement)**
  - uid : 광고 고유값
  - advertiser : 광고주
  - media : 광고매체
  - cost : 비용
  - impression : 노출수
  - click : 클릭수
  - conversion : 구매전환수
  - cv : 구매전환에 따른 매출액

    @property
  - CTR : 광고 노출 대비 클릭률
  - ROAS : 광고비 대비 매출액
  - CPC : 클릭 당 광고비
  - CVR : 클릭 대비 전환율
  - CPA : 전환 당 광고비

### 기능
#### advertiser 관련
**광고주 회원가입 : POST /api/advertiser**
- 필수 값인 이메일, 주소, 이름, 핸드폰 번호를 입력받아 광고주를 생성합니다.

**광고주 정보 조회** : GET /api/advertiser/:pk
- pk 값에 해당하는 광고주의 정보를 조회합니다.

**광고주 정보 수정** : PUT /api/advertiser/:pk
- pk 값에 해당하는 광고주의 정보를 수정합니다.

**광고주 삭제** : DELETE /api/advertiser/:pk
- pk 값에 해당하는 광고주를 삭제합니다.

**광고주 광고 정보 조회** : GET /api/advertiser/:pk/advertisements
- pk 값에 해당하는 광고주의 광고 정보를 조회합니다.

#### advertisement 관련
**광고 매체 별 조회** : GET /api/advertisement?media = ~~
- 파라미터 media 값이 없으면 전체 매체별 광고 성과 조회
- 파라미터 media 값이 있으면 매체별 광고 성과 조회 (ex. ?media=name)