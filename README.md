## CardNewsAutomation

#### 1. 프로젝트 설명
CardNewsAutomation은 블로그 포스트를 입력으로 받아 카드뉴스 형태의 이미지를 자동으로 생성하는 Python 프로그램입니다. 블로그의 제목, 내용, 그리고 브랜딩 정보를 포함한 여러 개의 이미지 카드를 생성합니다. 폰트의 크기는 html태그에 따라 달라집니다.

현재 지원 블로그 : 티스토리

#### 2. 사용 기술
- Python 3
- BeautifulSoup
- Requests
- Pillow

#### 3. 설치 방법
1. 이 GitHub 레포지토리를 클론합니다.
2. 필요한 Python 라이브러리를 설치합니다.

   ```
   pip install -r requirements.txt
   ```

#### 4. 사용 방법
1. `config.py` 파일에서 필요한 설정을 변경합니다. 예를 들어, 폰트 경로, 이미지 크기 등을 설정할 수 있습니다.
2. `main.py` 파일을 실행합니다.

   ```
   python main.py
   ```
3. 실행 시 블로그 URL을 입력으로 제공합니다.

#### 5. 코드 구조
- `main.py`: 프로그램의 실행점입니다. 카드뉴스 생성을 위한 여러 함수를 호출합니다.
- `BlogCrawler.py`: 블로그의 HTML을 크롤링합니다.
- `TistoryCrawler.py`: 티스토리 블로그에 특화된 크롤링을 수행합니다.
- `generateCardnews*.py`: 각각의 이미지 카드 (제목, 내용, 브랜딩)를 생성합니다.

#### 6. 설정 변경 방법
`config.py` 파일에서 다양한 설정을 변경할 수 있습니다. 이 파일에는 다음과 같은 설정이 포함되어 있습니다:
- OpenAI API 키
- 폰트 경로
- 이미지 크기
- 배경색
- 텍스트 색상

#### 7. 라이센스 및 저작권 정보
이 프로그램은 MIT 라이센스 하에 배포됩니다.

#### 8. 개발자 정보
- GitHub: https://github.com/larry1121
- 이메일: ghy200000@gmail.com
