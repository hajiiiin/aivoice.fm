import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def llm_is_story(text: str) -> bool:
    prompt = f"""
    아래 글이 라디오 청취자의 사연인지 판단해주세요. 사연이란 개인적인 경험, 감정, 일상의 사건을 나누는 글입니다.
    예: 가족 이야기, 회사 일, 감동적인 순간, 고민 등

    조건:
    - 단순한 신청곡, 인사, 날씨 얘기, 짧은 코멘트는 사연이 아닙니다.
    - 사연이면 "True", 아니면 "False"만 단답형으로 답해주세요.

    글:
    \"\"\"
    {text}
    \"\"\"
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        result = response.choices[0].message.content.strip()
        return result.lower().startswith("true")
    except Exception as e:
        print("OpenAI Error:", e)
        return False
    
def filter_stories_by_llm(input_path="story/candidate_stories.json", output_path="story/story.json"):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    LIMIT = 10 #테스트용 갯수 제한

    filtered = []
    for item in tqdm(data["candidates"], desc="LLM filtering"):
        try:
            if llm_is_story(item["content"]):
                filtered.append(item)
        except Exception as e:
            print(f"[{item['id']}] 처리 중 오류 발생: {e}")
            continue


    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"stories": filtered}, f, ensure_ascii=False, indent=2)

    print(f"LLM 필터링 완료: {len(filtered)}개 저장됨 → {output_path}")

if __name__ == "__main__":
    filter_stories_by_llm()