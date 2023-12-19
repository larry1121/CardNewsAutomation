import os
from PIL import Image, ImageDraw, ImageFont
from remove_emoji import remove_emoji
from sanitize_filename import sanitize_filename
from config import BRANDING_BLOG_NAME_FONT_SIZE, BRANDING_TEXT, BRANDING_TEXT_FONT_SIZE, BUNDLE_DIR_PATH, IMAGE_SIZE, FONT_PATH, BRANDING_CIRCLE_RADIUS,TEXT_COLOR, BORDER_COLOR, BORDER_WIDTH, BACKGROUND_COLOR
import config
def createBrandingCardByInfo(BlogMetaInfo):
    blog_name = BlogMetaInfo['site_name']

    # 이미지 설정
    size = IMAGE_SIZE  # 조정 가능
    background_color = BACKGROUND_COLOR
    font_path = FONT_PATH  # 원하는 폰트 파일로 변경

    # 이미지 생성
    image = Image.new("RGB", size, background_color)

    # 원 중심 계산
    center_x, center_y = size[0] // 2, size[1] // 2

    # 원 그리기
    draw = ImageDraw.Draw(image)
    radius = BRANDING_CIRCLE_RADIUS  # 조정 가능
    draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), outline="black")

    # Favicon 이미지 불러오기
    favicon_image_path = os.path.join(BUNDLE_DIR_PATH, f'{blog_name}.ico')
    favicon = Image.open(favicon_image_path)  # 파일명은 위에서 다운로드한 파일명과 일치해야 함

    # Favicon 크기 조정
    favicon = favicon.resize((radius * 2, radius * 2))

    # Circular mask 생성
    mask = Image.new("L", favicon.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0, favicon.size[0], favicon.size[1]), fill=255)

    # Favicon를 circular mask를 이용하여 이미지에 삽입
    image.paste(favicon, (center_x - radius, center_y - radius), mask)

    # 텍스트 추가
    text = BRANDING_TEXT
    font_size = BRANDING_TEXT_FONT_SIZE  # 조정 가능
    font = ImageFont.truetype(font_path, font_size)

    text_width, text_height = draw.textsize(text, font)
    text_x = (size[0] - text_width) // 2
    text_y = center_y + radius + 40  # 조정 가능
    draw.text((text_x, text_y), text, font=font, fill="black", align='center')
    
    # 텍스트 추가: 블로그 이름
    blog_name_font_size = BRANDING_BLOG_NAME_FONT_SIZE  # 조정 가능
    blog_name_font = ImageFont.truetype(font_path, blog_name_font_size)
    blog_name_width, blog_name_height = draw.textsize(blog_name, blog_name_font)
    blog_name_x = (size[0] - blog_name_width) // 2
    blog_name_y = center_y - radius - 80  # 조정 가능
    draw.text((blog_name_x, blog_name_y), blog_name, font=blog_name_font, fill="black", align='center')

    # 폴더 이름 설정
    
    folder_name = sanitize_filename(remove_emoji(str(BlogMetaInfo['title'])))
    folder_path = os.path.join(config.save_dir_path, folder_name)

    # 폴더가 없다면 폴더를 생성
    if not os.path.exists(folder_path):
      os.mkdir(folder_path)

    # 이미지 파일 이름 설정 (폴더 경로 포함)
    filename = os.path.join(folder_path, f"{blog_name}_branding_image.jpg")

    # 이미지 저장
    image.save(filename, format="JPEG")
    
    print(f"BrandingImage : {filename} 생성 완료")

if __name__ == "__main__":
    # Test with different blog names and post titles
    createBrandingCardByInfo({'site_name': 'giftedmbti', 'title': '[MBTI] INTJ는 왜 그럴까? 😎 - ㅇ나러니ㅏㅁㅇ러ㅣㅏㄴㅁ얼니암ㄹㄴ'})
