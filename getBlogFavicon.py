import requests

from getBlogMetaInfo import getBlogMetaInfo

def getBlogFavicon(website_url):
    # Favicons 다운로드 URL 생성

    size=128
    favicon_url = f'https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url={website_url}&size={size}'

    try:
        # 이미지 다운로드
        response = requests.get(favicon_url)
        response.raise_for_status()  # 에러 발생 시 예외 처리
        
        # blog_name 가져오기
        BlogMetaInfo = getBlogMetaInfo(website_url)
        blog_name = BlogMetaInfo['site_name']

        # 파일로 저장
        file_name = f'{blog_name}.ico'
        with open(file_name, 'wb') as file:
            file.write(response.content)

        if file_name.endswith('.ico'):
            print(f'Favicon 다운로드 완료: {file_name}')
        else:
            print(f'Error: 올바르지 않은 파일 형식 - {file_name}')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    # 예시: 다운로드 받을 웹사이트 주소
    website_url = 'https://giftedmbti.tistory.com/'

    # 파비콘 다운로드
    getBlogFavicon(website_url)
