from divideContentsByH2Tag import divideContentsByH2Tag


def generateCardnewsContentImages(blog_url):
    # Step 1: Get blog content using TistoryCrawler class
    
    
    # Step 2: Divide contents by h2 tag
    dividedContents = divideContentsByH2Tag(html_source)
    
    # Step 3: Generate Cardnews Content Images
    for content in dividedContents:
        generateCardnewsContentImageByContent(content)
