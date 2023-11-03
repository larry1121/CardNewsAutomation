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

    if tag_name in ['h2', 'h3', 'p']:
        original_text = tag.text
        print(f'Original text: {original_text}')  # Debug log
        text = remove_emoji(remove_emoji(original_text))
        print(f'Text after removing emoji: {text}')  # Debug log
        wrapped_text = wrap_text(draw, text, font, max_text_width)
        draw.text((50, y_position), wrapped_text, font=font, fill=TEXT_COLOR)
        y_position += (120 + wrapped_text.count('\n') * 25)*y_correction_constant if tag_name == 'h2' \
            else (50 + wrapped_text.count('\n') * 25)*y_correction_constant if tag_name == 'h3' \
            else (120 + wrapped_text.count('\n') * 40)*y_correction_constant  # Update y_position based on tag name
            
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
   <h2 data-ke-size="size26">INFJ의 이상적인 연애 관계 💑</h2>
<p data-ke-size="size16">INFJ들은 이상적인 연애 관계에서 다음과 같은 가치를 중요시해요:</p>
<h3 data-ke-size="size23">솔직하고 열린 대화를 할 수 있는 관계 🤗</h3>
<p data-ke-size="size16">INFJ들은 솔직하고 열린 대화를 통해 서로를 이해하고, 서로의 감정과 생각을 나눌 수 있는 관계를 원해요. 서로에게 진심으로 다가가기 위해서는 이러한 소통이 매우 중요합니다.</p>
<h3 data-ke-size="size23">상대방을 존중하고 이해하는 관계 🗨️</h3>
<p data-ke-size="size16">INFJ들은 상대방을 존중하고 이해하는 것이 매우 중요해요. 이들은 서로의 공간과 개인적인 시간을 존중하며, 서로의 취향과 가치를 이해하려고 노력합니다.</p>
<h3 data-ke-size="size23">감정적인 지지를 제공하는 관계 🤗</h3>
<p data-ke-size="size16">INFJ들은 서로를 위로하고 감정적인 지지를 제공하는 관계를 바랍니다. 힘든 순간에도 서로를 지지하고 더 나은 방향으로 나아갈 수 있도록 도와줌으로써, 더욱 깊고 의미 있는 연결을 형성할 수 있어요.</p>
<h3 data-ke-size="size23">공통의 이상과 목표를 공유하는 관계 🌈</h3>
<p data-ke-size="size16">INFJ들은 상대방과 공통의 이상과 목표를 공유하는 것을 중요하게 생각해요. 서로가 비슷한 가치관과 이상을 가지고 있다면, 더욱 깊고 의미 있는 관계를 형성할 수 있을거에요.</p>'''

    # 이미지 생성 및 저장
    generateCardnewsContentImageByContent(html_content, 'output_image',"/Users/usere/blogimageautomation/CardNewsAutomation/[MBTI] INTP에게 이상적인 연애 ")
