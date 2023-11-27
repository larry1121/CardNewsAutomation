# OpenAI(not yet)
OPENAI_API_KEY = 'sk-'

import os
import sys

if getattr(sys, 'frozen', False):
    # The application is frozen
    bundle_dir = sys._MEIPASS
else:
    # The application is not frozen
    # Change this bit to the path where you store your data files:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

# write ttf file name here
FONT_PATH = os.path.join(bundle_dir, 'THE소녀감성.ttf')


IMAGE_SIZE = (1080, 1080)  # Instagram card news size
BACKGROUND_COLOR = (255, 220, 220)  # 연한 핑크색
# (255, 235, 235) 더 연한 핑크색
TEXT_COLOR = (0, 0, 0) # 검은색 글씨
BORDER_COLOR = (255, 255, 255) #하얀색 경계선
BORDER_WIDTH = 15

# TITLE_CONSTANT
TITLE_BLOG_NAME_FONT_SIZE = 65

# CONTENT_CONSTANT
BASE_FONT_SIZE = 50

# BRANDING_CONSTANT
BRANDING_CIRCLE_RADIUS = 200
BRANDING_TEXT = "매일 MBTI 연애 팁을 올립니다.\n팔로우 하시고 매일 연애 팁 받아보세요."
BRANDING_TEXT_FONT_SIZE = 50
BRANDING_BLOG_NAME_FONT_SIZE = 70
HASHTAG = "      . . .        #MBTI#ENFP#ISTJ#ISFJ#INFJ#INTJ#ISTP#ISFP#INFP#INTP#ESTP#ESFP#ENTP#ESTJ#ESFJ#ENFJ#ENTJ#인스타툰"
