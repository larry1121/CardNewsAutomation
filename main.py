


from generateCardnewsBrandingImageByUrl import generateCardnewsBrandingImageByUrl
from generateCardnewsContentImagesByUrl import generateCardnewsContentImages

from generateCardnewsTitleImageByUrl import generateCardnewsTitleImageByUrl


def cardnewsautomation(blog_url):
    generateCardnewsTitleImageByUrl(blog_url)
    generateCardnewsContentImages(blog_url)
    generateCardnewsBrandingImageByUrl(blog_url)
    

if __name__ == "__main__":
    
    test_url = "https://giftedmbti.tistory.com/184"
    cardnewsautomation(test_url)

