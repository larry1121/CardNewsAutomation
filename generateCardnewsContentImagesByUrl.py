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
#   File "/home/codespace/.python/current/lib/python3.10/site-packages/PIL/Image.py", line 2409, in save
#     format = EXTENSION[ext]
# KeyError: ''

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "/workspaces/CardNewsAutomation/generateCardnewsContentImagesByUrl.py", line 23, in <module>
#     generateCardnewsContentImages(test_url)
#   File "/workspaces/CardNewsAutomation/generateCardnewsContentImagesByUrl.py", line 16, in generateCardnewsContentImages
#     generateCardnewsContentImageByContent(content,ImageCount)
#   File "/workspaces/CardNewsAutomation/generateCardnewsContentImageByContent.py", line 55, in generateCardnewsContentImageByContent
#     image.save(f"{ImageCount}")
#   File "/home/codespace/.python/current/lib/python3.10/site-packages/PIL/Image.py", line 2412, in save
#     raise ValueError(msg) from e
# ValueError: unknown file extension: 