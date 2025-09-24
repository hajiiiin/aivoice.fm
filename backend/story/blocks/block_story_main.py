from openai import OpenAI
import os
from dotenv import load_dotenv
from common.prompt_utils import build_block_prompt

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def block_story_main(story, keyword=None, prev_type=None, context=None):
    author = story.get("author", "익명 청취자")
    content = story["content"]

    base_instruction = f"""
    당신은 감성적인 AI 라디오 DJ입니다.
    아래 사연을 바탕으로, 청취자에게 따뜻하게 공감하는 멘트를 작성해주세요.

    사연 작성자: {author}
    사연 내용:
    \"\"\"
    {content}
    \"\"\"

    요청:
    1. 먼저 사연의 감정을 충분히 이해하고, 6~8문장 정도로 길게 공감 멘트를 작성해주세요.
    2. 단순 공감에서 끝내지 말고, 청취자가 생각해볼 만한 이야기를 1~2개 덧붙여주세요.
    3. 마지막에는 해당 분위기에 어울리는 실제 존재하는 노래를 추천해주세요.
    4. 이어서 “노래 듣고 돌아온 뒤”에 할 짧은 후속 멘트를 추가해주세요.
       (예: “노래 잘 듣고 오셨나요? OOO님의 목소리는 언제 들어도 감미롭죠.”)
    5. 마지막으로 다음 사연이나 콘텐츠로 자연스럽게 넘어가기 위한 전환 멘트를 1문장 추가해주세요.
       (예: “그럼 다음 사연도 함께 들어볼까요?”)

    최종 출력은 라디오 DJ가 읽는 하나의 자연스러운 흐름의 멘트로 만들어 주세요.  
    중간에 항목 구분 표시 없이, 하나의 연결된 멘트로 작성해주세요.
    DJ의 감정과 분위기를 살려 부드럽고 따뜻하게 말해주세요.
    """

    prompt = build_block_prompt(
        base_instruction=base_instruction,
        block_name="STORY_MAIN",
        keyword=keyword,
        prev_type=prev_type,
        context=context
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
    )

    return response.choices[0].message.content.strip()
