def build_summary_prompt(article_text: str, max_sentences: int = 3) -> str:
    return f"""다음은 KBS 뉴스 기사 본문입니다. 아래 본문을 요약하고, 감성적인 DJ 스타일의 멘트를 작성해주세요.

[요청 포맷]
1. 핵심 요약: {max_sentences}문장 이내
2. 감성 멘트: 청취자에게 공감과 여운을 줄 수 있는 따뜻한 말투

[기사 본문]
{article_text}

---

[출력 예시]
요약: (여기에 핵심 내용 요약)
DJ 멘트: (여기에 감성적인 AI DJ의 멘트)
"""

