## CardNewsAutomation

## 1\. 프로젝트 설명

CardNewsAutomation은 블로그 포스트 url을 입력으로 받아 카드뉴스 형태의 이미지를 자동으로 생성하는 Python 프로그램입니다.

블로그의 제목, 내용, 그리고 브랜딩 정보를 포함한 여러 장의 이미지 카드를 생성합니다.

### 예시 이미지

입력한 url:  
[https://giftedmbti.tistory.com/167](https://giftedmbti.tistory.com/167)

출력된 이미지 (일부):

![MBTI  INTJ에게 이상적인 연애 _0](https://github.com/larry1121/CardNewsAutomation/assets/78005200/4bc77502-7a7e-4ec0-a01f-d3fd77671631)![MBTI  INTJ에게 이상적인 연애 _2](https://github.com/larry1121/CardNewsAutomation/assets/78005200/77989c38-6ab0-42a4-8e4e-f2efb4ea8758)![giftedmbti_branding_image](https://github.com/larry1121/CardNewsAutomation/assets/78005200/adc63a57-5a27-4568-baa7-dbebbf6b3704)

### gui 지원

이미지 미리보기,저장 폴더 변경 및 열기를 지원하는 gui 실행파일(.exe)을 지원합니다.

![gui 실행파일 스크린샷](https://github.com/larry1121/CardNewsAutomation/assets/78005200/e5054fb1-4978-4834-a16b-57fb78402684)

### 이미지 규격 및 구동방식

이미지 규격은 1080×1080, jpg로 인스타 카드뉴스에 최적화되어있으며,config에서 변경가능합니다.

폰트의 크기는 html태그에 따라 달라집니다. 현재 티스토리만을 지원합니다.

구동방식:

1.  url을 입력받아 html을 크롤링
2.  Metadata로 TitleCard와 BrandingCard 생성
3.  h2태그로 내용을 구분하여 contentsCard 생성

## 2\. 사용 라이브러리

-   Python 3
-   BeautifulSoup
-   Requests
-   Pillow
-   Tkinter
-   PyInstaller

## 3\. 설치 및 실행방법

### 1\. gui 실행파일을 사용하는 방법

-   설치방법

1.  main_gui.zip을 다운로드하고, 압축해제합니다.

    [main_gui.zip 다운로드](https://github.com/larry1121/CardNewsAutomation/raw/main/dist/main_gui.zip)

-   실행방법

1.  다운로드한 exe파일을 실행합니다.

### 2\. 파이썬 코드를 직접 실행하는 방법

-   설치방법

1.  이 GitHub 레포지토리를 클론합니다.
2.  필요한 Python 라이브러리를 설치합니다.
3.  `pip install -r requirements.txt`
4.  main.py를 실행합니다.

-   실행방법

1.  `config.py` 파일에서 필요한 설정을 변경합니다. 예를 들어, 폰트 경로, 이미지 크기 등을 설정할 수 있습니다.
2.  `main.py` 파일을 실행합니다.
3.  `python main.py`
4.  실행 시 블로그 URL을 입력으로 제공합니다.

### 5\. 코드 구조

-   `main.py`: 프로그램의 실행점입니다. 카드뉴스 생성을 위한 여러 함수를 호출합니다.
-   `main_gui.py`: main.py의 함수들로 만든 gui입니다.
-   `BlogCrawler.py`: 블로그의 HTML을 크롤링합니다.
-   `TistoryCrawler.py`: 티스토리 블로그에 특화된 크롤링을 수행합니다.
-   `generateCardnews*.py`: 각각의 이미지 카드 (제목, 내용, 브랜딩)를 생성합니다.

### 6\. 설정 변경 방법

`config.py` 파일에서 다양한 설정을 변경할 수 있습니다. 이 파일에는 다음과 같은 설정이 포함되어 있습니다:

-   폰트 경로
-   이미지 크기
-   배경색
-   텍스트 색상

### 7. 라이센스 및 저작권 정보
이 프로그램은 MIT 라이센스 하에 배포됩니다.

### 8. 개발자 정보
- GitHub: https://github.com/larry1121
- 이메일: ghy200000@gmail.com
