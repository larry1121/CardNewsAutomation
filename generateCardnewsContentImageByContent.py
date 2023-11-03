import os
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
from config import BASE_FONT_SIZE, FONT_PATH, IMAGE_SIZE, BACKGROUND_COLOR, TEXT_COLOR, BORDER_COLOR, BORDER_WIDTH
from remove_emoji import remove_emoji

def generateCardnewsContentImageByContent(html_content, ImageName, save_path):
    print("-----------------------------------------------------------------------------------")
    print(f"current card content : {html_content}")
    base_font_size = BASE_FONT_SIZE
    while True:
        # HTML 파싱
        soup = BeautifulSoup(html_content, 'html.parser')

        # 이미지 크기 및 배경 설정
        image_width, image_height = IMAGE_SIZE
        image = Image.new('RGB', (image_width, image_height), BACKGROUND_COLOR)
        draw = ImageDraw.Draw(image)

        # 사용할 폰트 설정
        
        font = ImageFont.truetype(FONT_PATH, base_font_size)

        # HTML 태그에 따라 텍스트 그리기
        y_position = 100  # 시작 위치
        max_text_width = image_width - 100  # 텍스트가 그려질 최대 가로 길이

        for tag in soup.find_all(['h2', 'p', 'h3', 'ul', 'li']):
            tag_name = tag.name
            tag_font_size = get_font_size(tag_name, base_font_size)  # 각 태그별로 글씨 크기 계산
            font = ImageFont.truetype(FONT_PATH, tag_font_size)  # 태그별로 폰트 크기 설정
            

            y_position = draw_tag(draw, tag, tag_name, font, y_position, max_text_width)

        # 테두리 그리기
        border_rect = [(0, 0), (image_width, image_height)]
        draw.rectangle(border_rect, outline=BORDER_COLOR, width=BORDER_WIDTH)



        filename = os.path.join(save_path, f"{ImageName}.jpg")  # Save as JPG format
        # 이미지 저장
        image.save(filename, 'png')

        # Check if the total height exceeds the image height
        if y_position > image_height:
            # Decrease font size and regenerate the image
            base_font_size = base_font_size-1

            print(f"decreasing fontsize... ImageName : {ImageName}, current font size : {base_font_size}")
        else:
            print(f"\n{ImageName}.jpg generated, font size : {base_font_size}\n\n")
            break


def draw_tag(draw, tag, tag_name, font, y_position, max_text_width):
    """
    Draw text for a specific HTML tag
    """

    y_correction_constant = (font.size/50)

    if tag_name == 'h2':
        text = remove_emoji(tag.text)
        wrapped_text = wrap_text(draw, text, font, max_text_width)
        draw.text((50, y_position), wrapped_text, font=font, fill=TEXT_COLOR)
        y_position += (120 + wrapped_text.count('\n') * 25)*y_correction_constant  # 헤더 다음에 여백 추가
    elif tag_name == 'h3':
        text = remove_emoji(tag.text)
        wrapped_text = wrap_text(draw, text, font, max_text_width)
        draw.text((50, y_position), wrapped_text, font=font, fill=TEXT_COLOR)
        y_position += (50 + wrapped_text.count('\n') * 25)*y_correction_constant  # 소제목 다음에 여백 추가
    elif tag_name == 'p':
        text = remove_emoji(tag.text)
        wrapped_text = wrap_text(draw, text, font, max_text_width)
        draw.text((50, y_position), wrapped_text, font=font, fill=TEXT_COLOR)
        y_position += (120 + wrapped_text.count('\n') * 40)*y_correction_constant  # 문단 다음에 여백 추가
    elif tag_name == 'ul':
        y_position += 60  # 리스트 전에 여백 추가
        for li_tag in tag.find_all('li'):
            text = '- ' + li_tag.text
            wrapped_text = wrap_text(draw, text, font, max_text_width - 30)  # 간격 고려
            draw.text((80, y_position), wrapped_text, font=font, fill=TEXT_COLOR)
            y_position += (70 + wrapped_text.count('\n') * 25)*y_correction_constant  # 리스트 아이템 다음에 여백 추가

    return y_position

def wrap_text(draw, text, font, max_width):
    """
    텍스트를 주어진 가로 길이(max_width)에 맞게 줄바꿈하는 함수
    """
    try:
        if not text:
            return ""

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

    except IndexError:
        # 리스트 인덱스가 범위를 벗어날 때의 예외 처리
        return ""


def get_font_size(tag_name, base_size):
    """
    태그별로 글씨 크기를 계산하는 함수
    """
    size_factors = {'h2': 1.5, 'h3': 1.2, 'p': 1.0, 'ul': 1.0, 'li': 1.0}
    return int(base_size * size_factors.get(tag_name, 1.0))

if __name__ == "__main__":
    # 예제 HTML
    html_content = '''
    <h2 data-ke-size="size26">플러팅과 INTP: 서론에서부터 끝까지 한 걸음씩</h2>
<p data-ke-size="size16">INTP는 관계를 형성하는데 조금 더 많은 시간이 필요한 편이에요. 그래서 플러팅을 하기에는 적합하지 않다고 생각할 수 있지만, 사실은 그렇지 않아요. 플러팅을 통해 INTP와 가까워지는 방법을 알아보도록 해요!</p>
<h3 data-ke-size="size23">서론에서 시작하기: 지적인 호기심을 자극하는 주제로!</h3>
<p data-ke-size="size16">INTP는 지적 호기심이 높기 때문에, 서로의 관심사에 대해 이야기하는 것이 플러팅을 시작하는 좋은 방법이에요. 예를 들어, 공통적인 취미나 책, 영화, 과학적인 주제에 대해 토론해보면 INTP는 흥미를 갖고 더 많은 시간을 함께 보내고 싶어질 거예요. 자신만의 독특한 관점과 아이디어를 공유하는 것은 INTP에게 큰 매력이 됩니다.</p>
<h3 data-ke-size="size23">약간의 거리: 누군가가 침입하지 않는 공간</h3>
<p data-ke-size="size16">INTP는 내적 세계에 많은 시간을 보내는 경향이 있어요. 때문에 상대방이 너무 강력하게 다가오는 것보다는 조금의 거리감을 유지하는 것이 중요합니다. 서로에게 충분한 공간과 자유를 주면서 관심을 표현하는 것이 INTP와의 플러팅을 성공시키는 비결이에요.</p>'''

    # 이미지 생성 및 저장
    generateCardnewsContentImageByContent(html_content, 'output_image',"/Users/usere/blogimageautomation/CardNewsAutomation/[MBTI] INTP에게 이상적인 연애 ")
