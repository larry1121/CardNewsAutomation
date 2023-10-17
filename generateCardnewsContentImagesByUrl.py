from divideContentsByH2Tag import divideContentsByH2Tag
from generateCardnewsContentImageByContent import generateCardnewsContentImageByContent


def generateCardnewsContentImages(blog_url):
    # Step 1: Get blog content using TistoryCrawler class
    
    
    # Step 2: Divide contents by h2 tag
    dividedContents = divideContentsByH2Tag(blog_url)
    
    # Step 3: Generate Cardnews Content Images
    ImageCount = 1
    for content in dividedContents:
        
        generateCardnewsContentImageByContent(content,ImageCount)
        ImageCount = ImageCount + 1 



if __name__ == "__main__":
    test_url = "https://giftedmbti.tistory.com/184"
    generateCardnewsContentImages(test_url)


