import os
import glob
from dotenv import load_dotenv
from instabot import Bot

cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])

# 폴더 이름 입력 받기
folder_name = input("업로드할 폴더의 이름을 입력하세요: ")  # 폴더 이름을 입력받습니다.

# load .env
load_dotenv()

username = os.environ.get('YOUR_INSTA_USERNAME')
password = os.environ.get('YOUR_INSTA_PASSWORD')

# Instabot 객체 생성
bot = Bot()

# Instagram 계정 로그인 (자신의 Instagram 계정 아이디와 비밀번호를 입력하세요)
bot.login(username=username, password=password)

# 폴더 내의 모든 이미지 파일 가져오기
photos = []
for filename in os.listdir(folder_name):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # 이미지 파일 확장자를 확인
        photos.append(os.path.join(folder_name, filename))

# 폴더 이름을 사용하여 caption_title 설정
caption_title = f"{folder_name}"  # 폴더 이름을 제목에 사용합니다.
hashtag = "  . . .     #ENFP#ISTJ#ISFJ#INFJ#INTJ#ISTP#ISFP#INFP#INTP#ESTP#ESFP#ENTP#ESTJ#ESFJ#ENFJ#ENTJ#인스타툰"

caption = caption_title + hashtag

# 사진 업로드
for photo in photos:
    bot.upload_photo(photo, caption=caption)

# 업로드 후 임시 파일 제거 (선택 사항)
for photo in photos:
    os.remove(photo + ".REMOVE_ME")
