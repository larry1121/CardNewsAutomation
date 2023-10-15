from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
from config import FONT_PATH, IMAGE_SIZE, BACKGROUND_COLOR, TEXT_COLOR, BORDER_COLOR, BORDER_WIDTH

def generateCardnewsContentImageByContent(html_content, output_image_path):
    # HTML 파싱
    soup = BeautifulSoup(html_content, 'html.parser')

    # 이미지 크기 및 배경 설정
    image_width, image_height = IMAGE_SIZE
    image = Image.new('RGB', (image_width, image_height), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)

    # 사용할 폰트 설정
    font_size = 40
    font = ImageFont.truetype(FONT_PATH, font_size)

    # HTML 태그에 따라 텍스트 그리기
    y_position = 50  # 시작 위치
    max_text_width = image_width - 100  # 텍스트가 그려질 최대 가로 길이

    for tag in soup.find_all(['h2', 'p', 'h3', 'ul', 'li']):
        if tag.name == 'h2':
            text = tag.text
            wrapped_text = wrap_text(draw, text, font, max_text_width)
            draw.text((50, y_position), wrapped_text, font=font, fill=TEXT_COLOR)
            y_position += 40 + wrapped_text.count('\n') * 25  # 헤더 다음에 여백 추가
        elif tag.name == 'h3':
            text = tag.text
            wrapped_text = wrap_text(draw, text, font, max_text_width)
            draw.text((50, y_position), wrapped_text, font=font, fill=TEXT_COLOR)
            y_position += 30 + wrapped_text.count('\n') * 25  # 소제목 다음에 여백 추가
        elif tag.name == 'p':
            text = tag.text
            wrapped_text = wrap_text(draw, text, font, max_text_width)
            draw.text((50, y_position), wrapped_text, font=font, fill=TEXT_COLOR)
            y_position += 25 + wrapped_text.count('\n') * 25  # 문단 다음에 여백 추가
        elif tag.name == 'ul':
            y_position += 15  # 리스트 전에 여백 추가
            for li_tag in tag.find_all('li'):
                text = '• ' + li_tag.text
                wrapped_text = wrap_text(draw, text, font, max_text_width - 30)  # 간격 고려
                draw.text((80, y_position), wrapped_text, font=font, fill=TEXT_COLOR)
                y_position += 25 + wrapped_text.count('\n') * 25  # 리스트 아이템 다음에 여백 추가

    # 테두리 그리기
    border_rect = [(0, 0), (image_width, image_height)]
    draw.rectangle(border_rect, outline=BORDER_COLOR, width=BORDER_WIDTH)

    # 이미지 저장
    image.save(output_image_path)

def wrap_text(draw, text, font, max_width):
    """
    텍스트를 주어진 가로 길이(max_width)에 맞게 줄바꿈하는 함수
    """
    lines = []
    words = text.split()
    current_line = words[0]

    for word in words[1:]:
        test_line = current_line + " " + word
        width, _ = draw.textsize(test_line, font)
        if width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    return '\n'.join(lines)

# 예제 HTML
html_content = '''
<h2 data-ke-size="size26">INTJ의 관계 특징 3: 독립적인 성향</h2>
<p data-ke-size="size16">INTJ들은 독립적이고 자주 혼자서 자신의 시간을 즐기는 경향이 있어요. 이들은 자신만의 공간과 시간을 중요하게 생각하기 때문에 다른 사람들과의 관계에서도 독립적인 면모가 드러날 수 있어요.</p>
<p data-ke-size="size16">자신만의 시간을 존중해주는 것이 INTJ와의 관계를 발전시키는 데 도움이 될 수 있어요. INTJ와 함께하는 시간이 특별하고 의미 있는 시간이 되도록 배려해보세요.</p>
<h3 data-ke-size="size23">INTJ와의 관계에서 고려해야 할 점:</h3>
<ul data-ke-list-type="disc" style="list-style-type: disc;">
<li>INTJ의 개인 시간과 공간을 존중하기</li>
<li>함께할 때는 특별하고 의미 있는 경험을 제공하여 INTJ와의 연결을 강화하기</li>
</ul>
'''

# 이미지 생성 및 저장
generateCardnewsContentImageByContent(html_content, 'output_image.jpg')
