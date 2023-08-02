from PIL import Image, ImageDraw, ImageFont
import os

# 이미지 크기
size = (500, 500)

# 배경 색상
background_color = (255, 220, 220)  # 연한 핑크색

# 글꼴 경로와 최소/최대 글씨 크기
font_path = "PATH_OF_THE소녀감성.ttf"
min_font_size = 20
max_font_size = 60

# 블로그 이름과 글의 제목
blog_name = "블로그_이름"
post_title = "포스트_제목"

# 글씨 색상
text_color = (0, 0, 0)

# 테두리 선 색깔과 두께
border_color = (255, 255, 255)
border_width = 5

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
blog_font_size = 30
blog_font = ImageFont.truetype(font_path, blog_font_size)

# 이미지에 글자 쓰기
draw = ImageDraw.Draw(image)
text_x = (size[0] - text_width) // 2
text_y = (size[1] - text_height) // 2 + 40  # 포스트 제목을 하단으로 내리기 위해 y 좌표 조정
draw.text((text_x, text_y), post_title, font=font, fill=text_color, align='center')

blog_text_x = 10
blog_text_y = 10
draw.text((blog_text_x, blog_text_y), blog_name, font=blog_font, fill=text_color)

# 테두리 그리기
draw.rectangle((0, 0, size[0] - 1, size[1] - 1), outline=border_color, width=border_width)

# 이미지 저장
if not os.path.exists("images"):
    os.makedirs("images")
filename = os.path.join("images", f"{post_title}.webp")  # Save as WebP format
image.save(filename, format="WEBP")
print(f"{post_title}.webp 완성")
