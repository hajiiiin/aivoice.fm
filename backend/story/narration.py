import json
from openai import OpenAI
import os
import time
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_story_radio(story_path="story.json"):
    with open("story.json", "r", encoding="utf-8") as f:
        story = json.load(f)
        stories = story["stories"]  

    for i,story in enumerate(stories):
        print(f"\n📬 청취자 {story['author']}님의 사연입니다. 『{story['title']}』\n")
        time.sleep(1)

        prompt = f"""
        당신은 감성적인 AI 라디오 DJ입니다. 지금 청취자가 사연을 보냈습니다.

        사연 제목: {story['title']}
        작성자: {story['author']}
        내용:
        \"\"\"
        {story['content']}
        \"\"\"

        다음을 포함한 라디오 멘트를 자연스럽게 구성해주세요:

        1. 사연의 감정을 먼저 파악하고, 그에 공감하는 AI DJ 멘트를 생성해주세요.
        2. 딱딱하거나 기계적이지 않게, 사연자의 감정에 맞게 부드럽고 친근하게 반응해 주세요.
        3. 사연에 대해 먼저 공감한 후, 짧은 피드백이나 질문으로 자연스럽게 대화를 이끌어 주세요.
        4. 너무 길지 않게 2~4문장으로 말해주세요.
        5. 마지막에는 이 분위기에 어울리는 실제 존재하는 노래를 추천해 주세요. (예: 제목, 가수명)

        형식은 라디오 DJ 멘트처럼 자연스럽고 대화하듯 써주세요.
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )

        gpt_text = response.choices[0].message.content.strip()
        print(f"🎙️ DJ: {gpt_text}")

        print("🎵 자, 그럼 이 곡 함께 들어볼까요? 잠시 감상하고 다시 만나요.\n")
        time.sleep(2)

        if i < len(stories) - 1:
            print("📻 다음 사연으로 넘어가 보겠습니다...\n")
            time.sleep(1)
        else:
            print("📻 오늘의 사연은 여기까지입니다. 함께 해주셔서 감사합니다 🎧")

if __name__ == "__main__":
    run_story_radio()