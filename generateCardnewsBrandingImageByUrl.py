

#generateCardnewsBrandingImage 함수는 카드뉴스의 브랜딩 이미지 카드를 만드는 함수로 아래와 같이 동작함.

# getBlogMetaInfo로 BlogMetaInfo 가져오기
# blog_name = BlogMetaInfo['site_name'] 로 blog_name을 윗부분에 작성하기
# 가운데에 원만들고 getBlogFavicon으로 다운로드한 파일을 원안에 넣기
# 아래부분에 팔로우 유도 문구 넣기

#매일 MBTI 연애 팁을 올립니다.
#팔로우 하시고 매일 연애 팁 받아보세요.

from createBrandingCardByInfo import createBrandingCardByInfo
from getBlogFavicon import getBlogFavicon
from getBlogMetaInfo import getBlogMetaInfo

def generateCardnewsBrandingImageByUrl(blog_url):
    # 블로그 메타 정보 가져오기
    BlogMetaInfo = getBlogMetaInfo(blog_url)
    
    # Favicon 다운로드 및 저장
    getBlogFavicon(blog_url)

    createBrandingCardByInfo(BlogMetaInfo)

    

if __name__ == "__main__":
    blog_url = "https://giftedmbti.tistory.com/184"  # 실제 블로그 URL로 변경
    generateCardnewsBrandingImageByUrl(blog_url)