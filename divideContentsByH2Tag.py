from bs4 import BeautifulSoup

from crawler.TistoryCrawler import TistoryCrawler



def divideContentsByH2Tag(blog_url):

    crawler = TistoryCrawler(blog_url)
    html_source = crawler.content

    dividedContents = []
    soup = BeautifulSoup(html_source, 'html.parser')
    content_div = soup.find('div', {'class': 'tt_article_useless_p_margin contents_style'})
    
    # Start dividing content
    temp_content = ""
    for tag in content_div:
        if tag.name == 'h2':
            # Save the previous content if exists
            if temp_content:
                dividedContents.append(temp_content)
                temp_content = ""
            temp_content += str(tag)
        elif tag.name == 'a':
            temp_content += str(tag)
            dividedContents.append(temp_content)
            temp_content = ""
        else:
            temp_content += str(tag)

    # Save the last piece of content if exists
    if temp_content:
        dividedContents.append(temp_content)
        
    return dividedContents

if __name__ == "__main__":

    test_url = "https://giftedmbti.tistory.com/184"
    dividedContents = divideContentsByH2Tag(test_url)
    print(dividedContents)

