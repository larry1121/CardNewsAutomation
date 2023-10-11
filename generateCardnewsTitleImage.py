# 테스트할 Tistory 블로그 URL
from getBlogMetaInfo import getBlogMetaInfo
from createTitleCardByInfo import createTitleCardByInfo




def generateCardnewsTitleImageByBlogUrl(blog_url):
  
  
  BlogMetaInfo = getBlogMetaInfo(blog_url)

  createTitleCardByInfo(BlogMetaInfo)


if __name__ == "__main__":
    # Test with different blog names and post titles
    test_url = "https://ham-in-dev.tistory.com/entry/setting-window-conda2"
    generateCardnewsTitleImageByBlogUrl(test_url)

