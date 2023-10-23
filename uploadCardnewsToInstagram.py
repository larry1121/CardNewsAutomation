import os
import glob
from dotenv import load_dotenv
from instabot import Bot

from config import HASHTAG

def uploadCardnewsToInstagram(folder_name):
    # Delete existing cookie files
    cookie_del = glob.glob("config/*cookie.json")
    if cookie_del:
        os.remove(cookie_del[0])

    # Load .env
    load_dotenv()
    username = os.environ.get('YOUR_INSTA_USERNAME')
    password = os.environ.get('YOUR_INSTA_PASSWORD')

    # Create an Instabot instance
    bot = Bot()

    # Instagram account login
    bot.login(username=username, password=password)

    # Get a list of image files in the specified folder
    photos = []
    for filename in os.listdir(folder_name):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            photos.append(os.path.join(folder_name, filename))

    # Set the caption based on the folder name and hashtag
    caption_title = f"{folder_name}"
    hashtag = HASHTAG
    caption = caption_title + hashtag

    # Upload photos
    for photo in photos:
        bot.upload_photo(photo, caption=caption)

    # Remove temporary files after upload (optional)
    for photo in photos:
        os.remove(photo + ".REMOVE_ME")

# Test code
if __name__ == "__main__":
    folder_name = input("Enter the name of the folder to upload: ")
    uploadCardnewsToInstagram(folder_name)
