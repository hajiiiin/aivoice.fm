from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def block_story_discussion(story, keyword=None):
    author = story.get("author", "익명 청취자")
    content = story["content"]

    prompt = f"""
    당신은 라디오 DJ입니다.  
    아래 사연을 바탕으로, 하나의 "토론 주제"를 뽑아내고 청취자와 함께 생각을 나누는 코너를 만듭니다.

    사연 작성자: {author}
    사연 내용:
    \"\"\"
    {content}
    \"\"\"

    요청:
    1. 사연 속에서 토론할만한 주제를 뽑아주세요. (예: "연애 중 연락 빈도, 얼마나 자주 해야 할까?")
    2. 해당 주제에 대해 "찬성 입장"과 "반대 입장"을 DJ가 혼자 얘기하듯 자연스럽게 설명해주세요.
    3. 너무 딱딱하지 않게, 대화체/라디오 톤으로 작성하세요.
    4. 마지막에 청취자 참여 유도 멘트를 추가해주세요.  
       (예: "여러분은 어떻게 생각하시나요? 댓글이나 채팅으로 남겨주세요.")
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
    )

    return response.choices[0].message.content.strip()
