import emoji

def remove_emoji(input_string):
    # 이모지를 찾아내기
    emojis = [c for c in input_string if emoji.is_emoji(c)]

    # 이모지를 제거한 문자열 생성
    string_without_emoji = ''.join([c for c in input_string if c not in emojis])

    return string_without_emoji


if __name__ == "__main__":
    # 예제 사용
    original_string = "[MBTI] INTJ는 왜 그럴까? 😎"
    string_without_emoji = remove_emoji(original_string)
    print(f"Original String: {original_string}")
    print(f"String without Emoji: {string_without_emoji}")
