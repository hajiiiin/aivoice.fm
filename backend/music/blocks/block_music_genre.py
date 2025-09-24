from openai import OpenAI
import os
from dotenv import load_dotenv
import random
from common.prompt_utils import build_block_prompt

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def block_music_genre(keyword=None, prev_type=None, context=None):
    genres = ["재즈", "록", "EDM", "발라드", "힙합", "인디"]
    selected_genre = random.choice(genres)

    base_instruction = f"""
    당신은 감성적인 라디오 DJ입니다.
    이전 코너는 {prev_type}이었고, 이런 분위기였습니다:
    {context}

    이제 [MUSIC_GENRE] 코너로 자연스럽게 이어주세요.
    오늘은 "{selected_genre}" 장르를 탐험하는 시간입니다.
    
    요구사항:
    1. 이 장르의 특징을 2~3문장으로 소개해주세요.
    2. 대표적인 아티스트나 곡을 1~2개 예시로 들어주세요.
    3. keyword가 있으면 (예: "가을") 그 분위기와 "{selected_genre}" 장르를 연결해서 곡 추천 1개를 추가해주세요.
    4. 추천곡은 단순 나열이 아닌, “이 곡을 들으며 {selected_genre}의 매력을 느껴보시죠”처럼 청취자와 함께 듣는 톤으로 말해주세요.
    5. 곡이 끝난 뒤에는 “방금 들은 곡, 참 인상적이었죠?”처럼 마무리 멘트를 해주세요.
    6. 표현은 매번 달라지도록 해주세요.

    키워드: {keyword}
    """

    prompt = build_block_prompt(
        base_instruction=base_instruction,
        block_name="MUSIC_ARTIST",
        keyword=keyword,
        prev_type=prev_type,
        context=context
    )


    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85,
    )
    return response.choices[0].message.content.strip()
