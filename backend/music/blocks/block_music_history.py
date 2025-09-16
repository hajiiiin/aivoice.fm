from openai import OpenAI
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def block_music_history(keyword=None):
    today = datetime.now().strftime("%m월 %d일")
    prompt = f"""
    오늘은 {today}입니다. 
    과거 오늘의 음악 역사 속에서 실제 있었던 사건 2~3개를 소개해주세요.
    한국 이슈를 최소 1개 포함하고, 해외 사건도 함께 다뤄주세요.
    DJ 멘트 형식으로 감성 있게 작성하고, 각 사건마다 어울리는 곡을 추천하고, 마치 라디오처럼 곡을 직접 이어주세요.
       - (예: “지금 이 곡 함께 들어보시죠” / “잠시 감상하고 오겠습니다”) 
    각각의 사건과 추천곡 소개는 하나의 흐름 있는 덩어리처럼 작성해주세요.
    (예: "강렬한 퍼포먼스가 인상적인 Kill This Love, 그리고 중독적인 뚜두뚜두 함께 들어보시죠.")
    곡을 들은 후에는 “잘 듣고 오셨나요? 그 시절의 감성이 느껴지네요”처럼 후속 멘트를 넣어주세요.
    표현은 매번 다르게 해주세요.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
    )
    return response.choices[0].message.content.strip()
