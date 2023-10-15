import re

from BlogCrawler import BlogCrawler


class TistoryCrawler(BlogCrawler):
    def __init__(self, url):
        BlogCrawler.__init__(self, url)

    @property
    def content(self):
        selected_elements = [
            self._soup.select_one("article"),
        ]

        for element in selected_elements:
            if element:
                # Use regular expression to remove content before the specified class
                element_html = str(element)
                start_index = element_html.find('tt_article_useless_p_margin contents_style')
                # end_index = element_html.find('revenue_unit_wrap')
                end_index = element_html.find('container_postbtn #post_button_group')
                is_index_valid = start_index != -1 and end_index != -1

                if is_index_valid :
                    cleaned_html = element_html[start_index:end_index]
                    # Use regular expression to remove HTML tags
                    # clean_text = re.sub('<.*?>', '', cleaned_html)
                    return cleaned_html
                
        return ""

# 테스트 코드
if __name__ == "__main__":
    # 테스트할 Tistory 블로그 URL
    test_url = "https://giftedmbti.tistory.com/184"

    # 블로그 크롤러 인스턴스 생성
    crawler = TistoryCrawler(test_url)

    # 블로그 글 내용 출력
    blog_content = crawler.content
    print(blog_content)