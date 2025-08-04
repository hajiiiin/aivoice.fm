import datetime
from openai import OpenAI
import os
from dotenv import load_dotenv

# .env에서 API 키 불러오기
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_opening_ment():
    today = datetime.datetime.now().strftime("%Y년 %m월 %d일 %A")
    
    prompt = (
        f"{today}입니다. AI 라디오 DJ로서 오늘 하루를 시작하는 청취자들에게 감성적이면서도 따뜻한 오프닝 멘트를 만들어주세요. "
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8  # 좀 더 감성적인 문장
    )

    return response.choices[0].message.content.strip()
