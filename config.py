import sys
import os

# OpenAI(not yet)
OPENAI_API_KEY = 'sk-'

# IMAGE_CONSTANT
# FONT_PATH = '/Users/usere/blogimageautomation/CardNewsAutomation/THE소녀감성.ttf'
# 실행 파일이 패키징되었을 때와 그렇지 않을 때를 모두 처리
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

FONT_PATH = os.path.join(application_path, 'CardNewsAutomation', 'THE소녀감성.ttf')

IMAGE_SIZE = (1080, 1080)  # Instagram card news size
BACKGROUND_COLOR = (255, 220, 220)  # 연한 핑크색
TEXT_COLOR = (0, 0, 0)
BORDER_COLOR = (255, 255, 255)
BORDER_WIDTH = 5

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
