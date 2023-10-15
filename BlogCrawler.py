from bs4 import BeautifulSoup
import requests




class BlogCrawler:
    def __init__(self, url):
        headers = {"User-Agent": "Mozilla/5.0"}
        req = requests.get(url , headers=headers)
        html_content = req.content
        self._soup = BeautifulSoup(html_content, "html.parser")
        
      

    @property
    def info(self):
        return {
            "title": self.title,
            "description": self.description,
            "image": self.image,
        }

    @property
    def title(self):
        return self._soup.find("meta", property="og:title")["content"]

    @property
    def description(self):
        return self._soup.find("meta", property="og:description")["content"]
    
    @property
    def site_name(self):
        return self._soup.find("meta", property="og:site_name")["content"]

    @property
    def image(self):
        return self._soup.find("meta", property="og:image")["content"]
    

    # 테스트 코드
if __name__ == "__main__":
    # 테스트할 Tistory 블로그 URL
    test_url = "https://bugdict.tistory.com/91"

    # 블로그 크롤러 인스턴스 생성
    crawler = BlogCrawler(test_url)


    # 블로그 글 내용 출력
    blog_content = crawler.info
    print(blog_content)