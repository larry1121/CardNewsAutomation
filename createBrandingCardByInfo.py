import os
from PIL import Image, ImageDraw, ImageFont

from config import BLOG_NAME_FONT_SIZE, BRANDING_TEXT, BRANDING_TEXT_FONT_SIZE, IMAGE_SIZE, FONT_PATH, BRANDING_CIRCLE_RADIUS,TEXT_COLOR, BORDER_COLOR, BORDER_WIDTH, BACKGROUND_COLOR

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
    favicon = Image.open(f'{blog_name}.ico')  # 파일명은 위에서 다운로드한 파일명과 일치해야 함

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
    blog_name_font_size = BLOG_NAME_FONT_SIZE  # 조정 가능
    blog_name_font = ImageFont.truetype(font_path, blog_name_font_size)
    blog_name_width, blog_name_height = draw.textsize(blog_name, blog_name_font)
    blog_name_x = (size[0] - blog_name_width) // 2
    blog_name_y = center_y - radius - 80  # 조정 가능
    draw.text((blog_name_x, blog_name_y), blog_name, font=blog_name_font, fill="black", align='center')

    # 폴더 이름 설정
    folder_name = "branding_images"

    # 폴더가 없다면 폴더를 생성
    if not os.path.exists(folder_name):
      os.mkdir(folder_name)

    # 이미지 파일 이름 설정 (폴더 경로 포함)
    filename = os.path.join(folder_name, f"{blog_name}_branding_image.png")

    # 이미지 저장
    image.save(filename, format="PNG")
    print(f"{filename} 생성 완료")

if __name__ == "__main__":
    # Test with different blog names and post titles
    test_url = "https://ham-in-dev.tistory.com/entry/setting-window-conda2"
    createBrandingCardByInfo(test_url)
