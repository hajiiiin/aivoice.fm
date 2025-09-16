from openai import OpenAI
import os
from dotenv import load_dotenv
import random
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 로컬 JSON에서 아티스트 불러오기
def load_artists(path="data/artists.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)["artists"]

# 키워드 기반 아티스트 선택 (LLM)
def pick_artist_by_keyword(keyword: str) -> str:
    prompt = f"""
    당신은 음악 전문 AI입니다.
    키워드 "{keyword}"와 어울리는 아티스트 1명을 추천해주세요.
    한국/해외 아티스트 모두 가능하며, 전 세계적으로 유명한 뮤지션 위주로 골라주세요.
    답변은 아티스트 이름만 출력하세요.
    """
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return res.choices[0].message.content.strip()

# 메인 블록
def block_music_artist(keyword=None):
    if keyword:
        selected_artist = pick_artist_by_keyword(keyword)
    else:
        artists = load_artists()
        selected_artist = random.choice(artists)["name"]

    prompt = f"""
    당신은 감성적인 라디오 DJ입니다.
    오늘은 "{selected_artist}" 아티스트를 집중 조명하는 코너입니다.

    요구사항:
    1. 아티스트의 특징/음악적 매력을 2~3문장으로 소개해주세요.
    2. 대표곡 소개하고, “이 곡 함께 들어보시죠 / 지금 들어볼까요”처럼 곡을 DJ가 직접 트는 것처럼 이어주세요.
    3. keyword가 있으면 (예: "가을") 그 키워드와 "{selected_artist}"의 곡 중 하나를 연결해서 추천해주세요.
    4. 곡이 끝난 뒤에는 “잘 듣고 오셨나요? 역시 {selected_artist}답네요”처럼 후속 멘트를 넣어주세요.
    5. 전체 톤은 따뜻하고 친근한 라디오 멘트로 작성하고, 표현은 매번 달라지도록 해주세요.


    키워드: {keyword}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    print(block_music_artist("가을"))
