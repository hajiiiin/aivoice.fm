def build_block_prompt(base_instruction: str, block_name: str, keyword: str = None, prev_type: str = None, context: str = None) -> str:
    """
    모든 블럭에서 공통으로 사용하는 프롬프트 빌더
    - base_instruction: 해당 블럭 고유의 작성 규칙
    - block_name: 현재 블럭 이름
    - keyword: 오늘의 키워드
    - prev_type: 직전 블럭 타입 (transition에 활용)
    - context: 지금까지의 스크립트 일부 (맥락 유지)
    """
    transition_part = f"이전 코너는 {prev_type}이었고, 분위기는 다음과 같았습니다:\n{context}\n" if prev_type else ""
    
    return f"""
    당신은 감성적인 라디오 DJ입니다. 
    {transition_part}
    이제 [{block_name}] 코너를 진행해주세요.

    {base_instruction}

    추가 규칙:
    1. 새로 인사(예: '안녕하세요')는 하지 마세요.
    2. 이전 코너에서 자연스럽게 이어가는 전환 멘트를 반드시 포함하세요.
    3. 곡 추천 시에는 매번 다른 표현을 사용해야 합니다.
       - 예시: "이 곡을 함께 들어볼까요?", "잠시 감상해보시죠.", "이 노래로 분위기를 이어가시죠."
    4. 곡이 끝난 뒤 후속 멘트도 매번 다른 표현을 사용해야 합니다.
       - 예시: "좋은 감정이 전해지네요.", "방금 곡, 마음에 울림이 있었죠?", "분위기가 한층 따뜻해진 것 같아요."
    5. 같은 블럭 안에서도 같은 멘트를 반복하지 말고 반드시 변화를 주어야 합니다.
    6. 전체 톤은 DJ가 직접 말하는 라디오 대본처럼 따뜻하고 자연스럽게 작성하세요.

    키워드: {keyword}
    """
