from divideContentsByH2Tag import divideContentsByH2Tag
from generateCardnewsContentImageByContent import generateCardnewsContentImageByContent
from getBlogMetaInfo import getBlogMetaInfo
from remove_emoji import remove_emoji


def generateCardnewsContentImages(blog_url):
    # Step 1: Get blog content using TistoryCrawler class
    BlogMetaInfo = getBlogMetaInfo(blog_url)
    post_title = remove_emoji(str(BlogMetaInfo['title']))
    save_path = f"{post_title}"
    
    # Step 2: Divide contents by h2 tag
    dividedContents = divideContentsByH2Tag(blog_url)
    
    # Step 3: Generate Cardnews Content Images
    ImageCount = 1
    for content in dividedContents:
        
        generateCardnewsContentImageByContent(content,ImageCount,save_path)
        ImageCount = ImageCount + 1 



if __name__ == "__main__":
    test_url = "https://giftedmbti.tistory.com/184"
    generateCardnewsContentImages(test_url)


