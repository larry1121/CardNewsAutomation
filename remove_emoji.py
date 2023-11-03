import unicodedata

def remove_emoji(text):
    # 변형 선택자를 포함한 이모지와 관련된 문자를 제거하는 수정된 함수
    return "".join(c for c in text if not unicodedata.category(c) in ('So', 'Mn', 'Me'))

sample_text = "테스트 메시지 🤗🗨️!"
clean_text = remove_emoji(sample_text)
print(clean_text)  # "테스트 메시지 !"가 출력되어야 합니다.
