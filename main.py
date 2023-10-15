


from generateCardnewsBrandingImageByUrl import generateCardnewsBrandingImageByUrl
from generateCardnewsContentImagesByUrl import generateCardnewsContentImagesByUrl
from generateCardnewsTitleImageByUrl import generateCardnewsTitleImageByUrl


def cardnewsautomation(blog_url):
    generateCardnewsTitleImageByUrl(blog_url)
    generateCardnewsContentImagesByUrl(blog_url)
    generateCardnewsBrandingImageByUrl(blog_url)
    
