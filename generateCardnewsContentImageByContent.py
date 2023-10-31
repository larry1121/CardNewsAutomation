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
    <h2 data-ke-size="size26">자유로운 영혼, 하지만 협력도 필요해요! 🤝</h2>
<p data-ke-size="size16">ISTP는 독립심이 강하고 자유로운 영혼을 가진 사람들이에요. 그들은 자신만의 시간과 공간을 중요시하며, 다른 사람과의 관계에서도 이러한 자유로움을 유지하려고 노력해요. 그러나 협력과 소통이 필요한 순간에는 이들의 유연성과 문제해결 능력이 큰 도움이 될 거예요.</p>
<h3 data-ke-size="size23">관련 경험담: "함께한 여행, ISTP와의 협력"</h3>
<p data-ke-size="size16">저는 한 번 ISTP 친구와 여행을 갔었어요. 그때 그는 계획을 철저하게 세우고, 문제가 발생할 때마다 빠르게 해결하는 능력을 보여주었어요. 그의 독립심과 동시에 협력하는 모습을 보면서, 그와 함께하는 것은 얼마나 유익한 경험이었는지를 느낄 수 있었어요.</p>
<p data-ke-size="size16"> </p>
<p data-ke-size="size16">이렇게 ISTP의 특징을 알아보았는데요, 여러분도 이들의 독특한 성격과 능력에 놀라우셨나요? ISTP와의 관계에서 이러한 특징들을 고려한다면, 더욱 원활한 소통과 협력이 가능할 거예요. 세상은 다양한 성격으로 가득 차있어서, 서로를 이해하고 존중하는 것이 얼마나 소중한 일인지를 느낄 수 있는 좋은 기회일지도 몰라요! 💫</p>
<p data-ke-size="size16"> </p>
<p data-ke-size="size16">그럼 오늘의 이야기도 여기서 마치겠습니다. 다음에도 MBTI 성격 유형에 관한 재미있는 이야기로 찾아뵐게요! 잘 지내세요~ 🌈</p>
<p data-ke-size="size16"> </p>
<p data-ke-size="size16">구독과 좋아요를 눌러서 더 많은 MBTI 연애 팁과 이야기를 받아보세요! 그럼 모두 환상적인 연애를 만들어봐요! <span>💖</span><span>💌</span></p>
<p data-ke-size="size16"> </p>'''

    # 이미지 생성 및 저장
    generateCardnewsContentImageByContent(html_content, 'output_image',"/workspaces/CardNewsAutomation")
