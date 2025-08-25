import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

from datetime import datetime

def run_music_radio():
    today = datetime.now().strftime("%m월 %d일")

    prompt = f"""
    오늘은 {today}입니다.

    과거의 오늘, 음악 역사 속에서 실제로 있었던 인상 깊은 사건 중 2~3가지를 소개해주세요.
    대한민국 관련 이슈를 최소 1개 이상 포함해 주시고, 가능하다면 한국과 해외 이슈를 균형 있게 다뤄주세요.

    요구사항:
    1. 각 사건은 실제 날짜, 아티스트, 사건명(예: 음반 발매, 첫 공연 등)을 명확히 밝혀주세요.
    2. DJ가 청취자에게 이야기하듯 감정을 담아 2~4문장으로 멘트를 구성해주세요.
    3. 사건과 함께 2~3곡을 추천해주세요.
        - 이 중 1~2곡은 DJ 멘트 속에 추천 이유와 함께 자연스럽게 녹여주세요.
        - 나머지는 간단히 플레이리스트처럼 나열해주세요.
        - 예: “그럼 이슈의 주인공, 블랙핑크의 강렬한 퍼포먼스가 돋보이는 ‘Kill This Love’, 그리고 중독적인 ‘뚜두뚜두’ 함께 들어보시죠.”
        - 추천 이유는 간단한 수식어(예: "중독성 있는", "퍼포먼스가 인상적인")로 표현해주세요.
    4. 너무 정보 나열식이 아닌, 하나의 흐름 있는 라디오 멘트처럼 자연스럽게 말해주세요.
    5. 각각의 사건과 곡 소개는 하나의 덩어리처럼 연결된 DJ 멘트로 작성해주세요.

    형식은 아래 예시처럼 써주세요:

    - [음악 이슈 제목]
    - DJ 멘트 (사건 소개 + 감성 멘트 + 추천곡 소개)
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
    )

    output = response.choices[0].message.content.strip()
    print(output)

if __name__ == "__main__":
    run_music_radio()