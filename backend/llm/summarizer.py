from openai import OpenAI
import os
from dotenv import load_dotenv
from llm.prompt_builder import build_summary_prompt
import re

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 기사 본문을 받아 요약과 DJ 멘트를 생성하는 함수
def summarize_article(article_text: str, model: str = "gpt-4o") -> dict:
    prompt = build_summary_prompt(article_text)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "당신은 청취자와 공감하며 이야기 나누는 감성적인 AI 뉴스 DJ입니다. "
                        "감성적인 위로보다는 해당 뉴스 주제와 연결된 DJ 멘트를 만들어주세요. "
                        "멘트는 지나치게 추상적이지 않고, 실제 뉴스 이슈에 대해 DJ가 생각을 나누거나 "
                        "청취자와 대화를 나누는 자연스러운 톤이면 좋습니다."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800,
        )

        content = response.choices[0].message.content.strip()

        # 정규표현식 기반 파싱
        summary_match = re.search(r"해설 요약\s*:\s*(.+)", content)
        dj_ment_match = re.search(r"DJ 멘트\s*:\s*(.+)", content)

        summary = summary_match.group(1).strip() if summary_match else ""
        dj_ment = dj_ment_match.group(1).strip() if dj_ment_match else ""

        return {
            "success": True,
            "summary": summary,
            "dj_ment": dj_ment,
            "content": content
        }

    except Exception as e:
        return {
            "success": False,
            "summary": "요약 실패",
            "dj_ment": "멘트 생성 실패",
            "error": str(e),
            "content": None
        }
