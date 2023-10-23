import os
from config import HASHTAG
from generateCardnewsBrandingImageByUrl import generateCardnewsBrandingImageByUrl
from generateCardnewsContentImagesByUrl import generateCardnewsContentImages
from generateCardnewsTitleImageByUrl import generateCardnewsTitleImageByUrl
from getBlogMetaInfo import getBlogMetaInfo
from remove_emoji import remove_emoji
from uploadCardnewsToInstagram import uploadCardnewsToInstagram


def cardnewsautomation(blog_url):
    generateCardnewsTitleImageByUrl(blog_url)
    generateCardnewsContentImages(blog_url)
    generateCardnewsBrandingImageByUrl(blog_url)
    

    BlogMetaInfo = getBlogMetaInfo(blog_url)



    folder_name = remove_emoji(str(BlogMetaInfo['title']))
    

    # Confirm the images and caption before uploading
    print("Generated images and caption:")
    photos = [f"{folder_name}/{file}" for file in os.listdir(folder_name) if file.endswith(('.jpg', '.jpeg', '.png'))]
    caption_title = folder_name
    hashtag = HASHTAG
    caption = caption_title + hashtag
    for photo in photos:
        print(f"Image: {photo}")
    print(f"Caption: {caption}")

    # Ask for confirmation to upload
    upload_confirmation = input("Do you want to upload these images to Instagram? (y/n): ")
    if upload_confirmation.lower() == 'y':
        uploadCardnewsToInstagram(folder_name)
        print("Images uploaded to Instagram.")
    else:
        print("Images not uploaded. Exiting...")


if __name__ == "__main__":
    test_url = "https://giftedmbti.tistory.com/176"
    cardnewsautomation(test_url)
