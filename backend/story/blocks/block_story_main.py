from openai import OpenAI
import os
from dotenv import load_dotenv
from common.prompt_utils import build_block_prompt

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def block_story_main(
    story,
    keyword=None,
    prev_type=None,
    context=None,
    last_song=None,
    is_last=False,
    language="ko"
):
    author = story.get("author", "익명 청취자" if language == "ko" else "Anonymous Listener")
    content = story["content"]

    if language == "ko":
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

    else:  # English
        base_instruction = f"""
        You are a warm and empathetic AI Radio DJ.
        Based on the listener's story below, create a natural script that comforts and engages the audience.

        Story Author: {author}
        Story Content:
        \"\"\"
        {content}
        \"\"\"

        Requirements:
        1. Start by briefly introducing the story to the audience. (e.g., "This is a story sent in by OOO...")
        2. Then, deeply empathize with the emotions in the story and write a 6–8 sentence heartfelt response.
        3. Don’t stop at empathy—add 1–2 reflections or thoughts that the audience might consider.
        4. Recommend a real existing song that fits the mood of the story.
        5. Add a short follow-up comment as if returning after the song has finished.  
           - Each time, make it different and mention the previously recommended song ({last_song}).  
             (e.g., "That was Joy’s *Good Person*, wasn’t it warm?",  
             "Did you enjoy the song? OOO’s voice is always so soothing.",  
             "Lee Hi’s *Breathe* left us feeling calm.",  
             "Just now we listened to John Legend’s *All of Me*, and it still lingers in the heart.") 
        """
        if is_last:
            base_instruction += """
            6. Since this is the last story of the day, do not transition to another story.  
               Instead, add a closing remark for the story segment.  
               (e.g., "That brings today’s story segment to a close. Thank you for sharing your hearts with us.")
            """
        else:
            base_instruction += """
            6. End with a natural transition line leading into the next story or segment.  
            (e.g., "Shall we move on to the next story together?")
            """
        base_instruction += """
        The final output should be written as one continuous radio DJ script,  
        without labels or section breaks.  
        Keep the tone warm, natural, and emotionally engaging, as if spoken on-air.
        """

    prompt = build_block_prompt(
        base_instruction=base_instruction,
        block_name="STORY_MAIN" if language == "ko" else "STORY_MAIN_EN",
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