import datetime
from openai import OpenAI
import os
from dotenv import load_dotenv

# .env에서 API 키 불러오기
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_opening_ment(keyword: str = None, language="ko"):
    today = datetime.datetime.now().strftime("%Y년 %m월 %d일 %A")
    
    if language == "ko":
        prompt = f"{today}입니다. AI 라디오 DJ로서 오늘 하루를 마무리하는 청취자들에게 감성적이면서도 따뜻한 오프닝 멘트를 너무 길지 않게 만들어주세요. "
        if keyword:
            prompt += f"'{keyword}'와 관련된 계절감이나 분위기를 반영해 주세요."
        else:
            prompt += "청취자에게 친근하게 하루를 마무리할 수 있도록 작성해주세요."
    else:  # English
        prompt = f"Today is {today}. As an AI radio DJ, please create a warm and emotional opening ment for listeners wrapping up their day. Keep it concise and heartfelt. "
        if keyword:
            prompt += f"Make sure to reflect the seasonal mood or atmosphere related to '{keyword}'."
        else:
            prompt += "Make it friendly so listeners can end their day on a comforting note."

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8  # 좀 더 감성적인 문장
    )

    return response.choices[0].message.content.strip()
