def build_summary_prompt(article_text: str, target_length: str = "700~800자", mode: str = "headline") -> str:
    if mode == "deep":
        dj_instruction = (
            "DJ 멘트는 단순한 공감을 넘어서, 해당 뉴스에 대해 심층적으로 토론할 수 있도록 "
            "여러 관점(찬성·반대·사회적 파장 등)을 짚어주고, 청취자에게 사고를 유도하는 질문을 2~3개 던져주세요. "
            "토론을 이어갈 수 있는 논점을 제공하는 톤이면 좋습니다."
        )
    elif mode == "headline":
        dj_instruction = (
            "DJ 멘트는 청취자와 대화를 나누듯 편안하게, 가벼운 공감이나 짧은 의견을 나누는 방식으로 작성해주세요. "
            "너무 깊게 들어가기보다는 청취자가 쉽게 이해하고 반응할 수 있도록 자연스러운 질문이나 코멘트를 포함해주세요."
        )
    else:  # short/current
        dj_instruction = (
            "DJ 멘트는 짧고 간단하게, 한두 문장으로 자연스럽게 정리해 주세요."
        )

    return f"""다음은 KBS 뉴스 기사 본문입니다. 아래 본문을 요약하고, {mode} 스타일의 DJ 멘트를 작성해주세요.

[요청 포맷]
1. 해설 요약: 뉴스의 배경과 맥락을 간결히 정리해 주세요. 단순한 사실 나열보다 청취자가 왜 이 뉴스가 중요한지 이해할 수 있도록 풀어서 설명해주세요. {target_length}문장 정도로 요약하세요.
2. DJ 멘트: {dj_instruction}

[기사 본문]
{article_text}

---

[출력 예시]
요약: (여기에 {target_length}분량의 해설 중심 요약)
DJ 멘트: (여기에 AI DJ의 생각과 토론/공감/정리 멘트)
"""