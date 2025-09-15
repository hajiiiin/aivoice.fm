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
    1. 사건 소개
       - 실제 날짜 / 아티스트 / 사건명(예: 음반 발매, 첫 공연 등)을 명확히 밝혀주세요.
       - DJ가 청취자에게 이야기하듯 감정이 담긴 2~4문장 멘트로 구성해주세요.

    2. 곡 추천 (아래 기준을 따르세요)
       - 아티스트 기반 1곡: 해당 사건의 주인공 아티스트의 대표곡/해당 시기 곡.
       - 분위기/키워드 기반 1~2곡: 사건과 어울리는 분위기/테마/시기와 관련된 추천곡.
       - 추천곡 중복 X, 방송 부적합 곡 제외.
       - 곡 구분 방식
         - 1~2곡은 DJ 멘트에 자연스럽게 녹여주세요. (예: "강렬한 퍼포먼스가 인상적인 Kill This Love, 그리고 중독적인 뚜두뚜두 함께 들어보시죠.")
         - 나머지 곡은 플레이리스트처럼 나열해주세요. (예: - 추가 추천곡: 곡명 - 아티스트)

    3. 전체 스타일
       - 정보 나열식이 아닌, 감성적이고 자연스럽게 이어지는 라디오 DJ 멘트 형식으로 작성해주세요.
       - 각각의 사건과 추천곡 소개는 하나의 흐름 있는 덩어리처럼 작성해주세요.

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
    return output

if __name__ == "__main__":
    run_music_radio()