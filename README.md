# Map Change Service For Homeassistant

![HAKC)][hakc-shield]
![HACS][hacs-shield]
![Version v1.0.0][version-shield]

Default Map to NAVER Map. Map Change Service for Home Assistant #HA

## Version history
| Version | Date        | 내용              |
| :-----: | :---------: | ----------------------- |
| v1.0.0    | 2023.08.25  | First version  |


## Installation
### Manual
- HA 설치 경로 아래 custom_components에 map_change폴더 안의 전체 파일을 복사해줍니다.<br>
  `<config directory>/custom_components/map_change/`<br>
- Home-Assistant 를 재시작합니다<br>
### HACS
- HACS > Integretions > 우측상단 메뉴 > Custom repositories 선택
- 'https://github.com/miumida/map_change' 주소 입력, Category에 'integration' 선택 후, 저장
- HACS > Integretions 메뉴 선택 후, map_change 검색하여 설치


## Usage
### Custom Integration
- 구성 > 통합구성요소 > 통합구성요소 추가하기 > Map Change Service 선택 > 확인.



## Apply
- 개발자도구 > 서비스 > Map Change > map_change 실행.
- Home-Assistant 재시작, 브라우저 캐시 초기화(Ctrl + F5)


## 참고사이트
[1] 네이버 HomeAssistant 카페 | 똥찌린빤쮸님의 HA 지도 변경 방법 (빌드 없이 적용)(<https://cafe.naver.com/koreassistant/9431>)<br>

[version-shield]: https://img.shields.io/badge/version-v1.0.0-orange.svg
[hakc-shield]: https://img.shields.io/badge/HAKC-Enjoy-blue.svg
[hacs-shield]: https://img.shields.io/badge/HACS-Custom-red.svg
