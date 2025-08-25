import datetime
from openai import OpenAI
import os
from dotenv import load_dotenv

# .env에서 API 키 불러오기
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def make_closing_ment(current_news):
    if not current_news:
        return "어제 뉴스 돌아보기는 여기까지입니다. 편안한 하루 보내세요."

    lines = [f"그 외에도 "]
    for news in current_news[:3]:
        lines.append(f" - {news['title']}")
    if len(current_news) > 3:
        lines.append("...등의 소식이 전해졌답니다.")

    # lines.append("오늘도 함께해주셔서 감사합니다. 따뜻한 하루 보내세요 ☺️")
    return "\n".join(lines)
