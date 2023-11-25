def generate_mbti_gift_string(mbti, mbtiai):
    result_string = f"⬇️ {mbti}를 위한 선물 🎁 뜯어보기 … 클릭 💝 ⬇️\n\n"
    result_string += f"더 많은 mbti 연애 스킬 → @giftedmbti 팔로우\n\n"
    result_string += f"#giftedmbti#{mbti}#연애툰#인스타툰#{mbti}연애#{mbti}유형#{mbti}만화#{mbti}공감#{mbtiai}#{mbtiai}특#{mbtiai}연애#{mbtiai}이별#{mbti}남자#{mbti}여자#{mbti}친구#친구#결혼#연애#심리테스트#{mbtiai}우정#{mbtiai}밈#{mbtiai}공감#{mbtiai}플러팅#인간관계"

    return result_string

# 예시
mbti_input = input("MBTI를 입력하세요: ")
mbtiai_input = input("엠비티아이를 입력하세요: ")

result = generate_mbti_gift_string(mbti_input, mbtiai_input)
print(result)
