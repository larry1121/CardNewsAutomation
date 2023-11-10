import os
import logging
from config import HASHTAG
from generateCardnewsBrandingImageByUrl import generateCardnewsBrandingImageByUrl
from generateCardnewsContentImagesByUrl import generateCardnewsContentImages
from generateCardnewsTitleImageByUrl import generateCardnewsTitleImageByUrl
from getBlogMetaInfo import getBlogMetaInfo
from remove_emoji import remove_emoji
from sanitize_filename import sanitize_filename
# from uploadCardnewsToInstagram import uploadCardnewsToInstagram

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_images(blog_url):
    logging.info("Starting the image generation process.")
    generateCardnewsTitleImageByUrl(blog_url)
    logging.info("Title image generated.")
    generateCardnewsContentImages(blog_url)
    logging.info("Content images generated.")
    generateCardnewsBrandingImageByUrl(blog_url)
    logging.info("Branding image generated.")
    return get_image_folder_name(blog_url)

def get_image_folder_name(blog_url):
    logging.info("Retrieving blog meta info for folder naming.")
    BlogMetaInfo = getBlogMetaInfo(blog_url)
    folder_name = sanitize_filename(remove_emoji(str(BlogMetaInfo['title'])))
    logging.info(f"Folder name created: {folder_name}")
    return folder_name

def confirm_and_display(folder_name):
    logging.info("Preparing images and caption for display.")
    photos = [f"{folder_name}/{file}" for file in sorted(os.listdir(folder_name)) if file.endswith(('.jpg', '.jpeg', '.png'))]
    caption_title = folder_name
    hashtag = HASHTAG
    caption = f"{caption_title} {hashtag}"
    
    for photo in photos:
        logging.info(f"Image ready for display: {photo}")
        
    logging.info(f"Caption suggested for display: \n{caption}")
    
    return photos, caption




if __name__ == "__main__":
    test_url = "https://giftedmbti.tistory.com/151"
    folder_name = generate_images(test_url)
    confirm_and_display(folder_name)
