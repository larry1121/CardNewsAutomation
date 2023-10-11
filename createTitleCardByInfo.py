from PIL import Image, ImageDraw, ImageFont
import os
from remove_emoji import remove_emoji
from config import IMAGE_SIZE, FONT_PATH,TEXT_COLOR,BORDER_COLOR,BORDER_WIDTH,BACKGROUND_COLOR


def createTitleCardByInfo(BlogMetaInfo):

    post_title = remove_emoji(str(BlogMetaInfo['title']))
    blog_name = BlogMetaInfo['site_name']

    # 이미지 크기
    size = IMAGE_SIZE
    background_color = BACKGROUND_COLOR
    font_path = FONT_PATH
    min_font_size = 40
    max_font_size = 120
    text_color = TEXT_COLOR
    border_color = BORDER_COLOR
    border_width = BORDER_WIDTH

    # 블로그 이름과 글의 제목
    blog_font_size = 60

    # 이미지 생성
    image = Image.new("RGB", size, background_color)

    # 글자 크기 계산
    font_size = max_font_size
    font = ImageFont.truetype(font_path, font_size)
    text_width, text_height = 0, 0
    while font_size > min_font_size:
        font = ImageFont.truetype(font_path, font_size)
        text_width, text_height = font.getsize(post_title)
        if text_width < 0.8 * size[0]:
            break
        font_size -= 1

    # 블로그 이름의 폰트 크기 계산
    blog_font = ImageFont.truetype(font_path, blog_font_size)

    # 이미지에 글자 쓰기
    draw = ImageDraw.Draw(image)
    text_x = (size[0] - text_width) // 2
    text_y = (size[1] - text_height) // 2 + 40
    draw.text((text_x, text_y), post_title, font=font, fill=text_color, align='center')

    blog_text_x = 10
    blog_text_y = 10
    draw.text((blog_text_x, blog_text_y), blog_name, font=blog_font, fill=text_color)

    # 테두리 그리기
    draw.rectangle((0, 0, size[0] - 1, size[1] - 1), outline=border_color, width=border_width)

    # 이미지 저장 (as JPG)
    if not os.path.exists("images"):
        os.makedirs("images")
    filename = os.path.join("images", f"{post_title}.jpg")  # Save as JPG format
    image.save(filename, format="JPEG")
    print(f"{post_title}.jpg 완성")



if __name__ == "__main__":
    # Test with different blog names and post titles
    createTitleCardByInfo({'site_name': 'giftedmbti', 'title': '[MBTI] INTJ는 왜 그럴까? 😎'})
