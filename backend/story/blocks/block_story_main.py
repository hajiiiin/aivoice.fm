from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def block_story_main(story, keyword=None):
    author = story.get("author", "익명 청취자")
    content = story["content"]

    prompt = f"""
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
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
    )

    return response.choices[0].message.content.strip()
