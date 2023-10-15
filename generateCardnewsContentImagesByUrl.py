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


# Traceback (most recent call last):
#   File "/workspaces/CardNewsAutomation/generateCardnewsContentImagesByUrl.py", line 23, in <module>
#     generateCardnewsContentImages(test_url)
#   File "/workspaces/CardNewsAutomation/generateCardnewsContentImagesByUrl.py", line 16, in generateCardnewsContentImages
#     generateCardnewsContentImageByContent(content,ImageCount)
#   File "/workspaces/CardNewsAutomation/generateCardnewsContentImageByContent.py", line 39, in generateCardnewsContentImageByContent
#     wrapped_text = wrap_text(draw, text, font, max_text_width)
#   File "/workspaces/CardNewsAutomation/generateCardnewsContentImageByContent.py", line 63, in wrap_text
#     current_line = words[0]
# IndexError: list index out of range