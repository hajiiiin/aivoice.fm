from openai import OpenAI
import os
from dotenv import load_dotenv
from common.prompt_utils import build_block_prompt

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def block_story_main(story, keyword=None, prev_type=None, context=None, last_song=None, is_last=False):
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
    1. 먼저 사연을 **청취자에게 간단히 소개**해주세요. (예: "OOO님이 보내주신 사연입니다...")
    2. 그 후, 사연의 감정을 충분히 이해하고, 6~8문장 정도로 길게 공감 멘트를 작성해주세요.
    3. 단순 공감에서 끝내지 말고, 청취자가 생각해볼 만한 이야기를 1~2개 덧붙여주세요.
    4. 마지막에는 해당 분위기에 어울리는 실제 존재하는 노래를 추천해주세요.
    5. 이어서 곡이 끝난 뒤의 후속 멘트를 추가해주세요.  
       - 매번 다르게, 직전 추천곡({last_song})을 언급해서 말해주세요.  
         (예: "방금 들은 조이의 좋은 사람, 참 따뜻했죠.", 
         “노래 잘 듣고 오셨나요? OOO님의 목소리는 언제 들어도 감미롭죠.”,
         "이하이의 한숨 덕분에 마음이 차분해지네요.", 
          "방금 함께한 존 레전드의 All of Me, 여운이 남습니다.") 
    """
    if is_last:
        base_instruction += """
        6. 이번 사연이 오늘의 마지막 사연이므로, 
           "다음 사연"으로 넘어가지 말고 사연 코너 전체를 마무리하는 멘트를 추가해주세요.
           (예: "이렇게 오늘의 사연 코너를 마무리합니다. 함께해 주셔서 감사합니다.")
        """
    else:
        base_instruction += """
        6. 마지막으로 다음 사연이나 콘텐츠로 자연스럽게 넘어가기 위한 전환 멘트를 1문장 추가해주세요.
        (예: "그럼 다음 사연도 함께 들어볼까요?")
        """
    base_instruction += """
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
