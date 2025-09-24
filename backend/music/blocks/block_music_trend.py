from openai import OpenAI
import os
from dotenv import load_dotenv
from common.prompt_utils import build_block_prompt

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def block_music_trend(keyword=None, prev_type=None, context=None):
    base_instruction = f"""
    당신은 감성적인 라디오 DJ입니다.

    이전 코너는 {prev_type}이었고, 이런 분위기였습니다:
    {context}

    이제 [MUSIC_TREND] 코너로 이어주세요.
    최신 음악 트렌드와 차트를 소개하는 시간입니다.

    요구사항:
    1. 최근 1~2주간의 실제 글로벌/한국 음악 차트 트렌드를 다루듯 소개해주세요.
    2. K-POP, 빌보드, 멜론 차트 등 실제 맥락을 반영한 듯한 느낌으로 작성해주세요.
    3. DJ가 청취자에게 이야기하듯 3~4문장으로 자연스럽게 멘트를 작성해주세요.
    4. 곡 추천: 트렌드를 반영한 2곡 (예: - 곡명 - 아티스트)
    5. keyword가 있으면 (예: "가을") 분위기에 맞는 트렌드 곡을 하나 더 추천해주세요.
    6. 곡을 단순 나열하지 말고, **“이 곡을 함께 들어보시죠 / 지금 들어볼까요 / 듣고 오겠습니다”**처럼
       청취자와 함께 듣는 듯한 표현을 해주세요.
    7. 곡 이후에는 **“잘 듣고 오셨나요? / 분위기 참 좋네요”** 같은 후속 멘트로 마무리해주세요.
    8. 표현은 매번 다르게 해주세요. (고정된 멘트 금지)
    
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
        temperature=0.9,
    )
    return response.choices[0].message.content.strip()
