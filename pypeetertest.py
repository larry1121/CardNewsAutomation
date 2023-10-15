import asyncio
from pyppeteer import launch

async def generateCardnewsContentImageByContent(html_content, output_image_path='card_image.jpg'):
    # 브라우저 실행
    browser = await launch(headless=True)
    page = await browser.newPage()

    # 페이지에 HTML 콘텐츠 설정
    await page.setContent(html_content)

    # 적절한 렌더링을 보장하기 위해 짧은 시간 동안 대기
    await page.waitForTimeout(1000)

    # 콘텐츠의 경계 상자(bounding box) 가져오기
    bounding_box = await page.evaluate('''() => {
        const element = document.querySelector('.tt_article_useless_p_margin.contents_style');
        const { x, y, width, height } = element.getBoundingClientRect();
        return { x, y, width, height };
    }''')

    # 경계 상자의 스크린샷을 찍기
    await page.screenshot({
        path: output_image_path,
        clip: {
            x: bounding_box['x'],
            y: bounding_box['y'],
            width: bounding_box['width'],
            height: bounding_box['height'],
        },
    })

    # 브라우저 닫기
    await browser.close()

# 예시 사용법
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Card Content</title>
</head>
<body>
    <h1>Hello Card!</h1>
</body>
</html>
"""
output_path = '이미지를 저장할 경로/card_image.jpg'

# 이벤트 루프 실행
asyncio.get_event_loop().run_until_complete(generateCardnewsContentImageByContent(html_content, output_path))
