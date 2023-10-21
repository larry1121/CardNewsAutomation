import re  # 추가: 파일 이름 정제를 위한 라이브러리

# sanitize_filename 함수 정의
def sanitize_filename(filename):
    # Replace invalid characters with underscores
    return re.sub(r'[\/:*?"<>|]', '_', filename)
