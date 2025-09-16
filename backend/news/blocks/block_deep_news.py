from news.crawl_kbs_program_news import extract_article_body
from news.llm.summarizer import summarize_article

def block_deep_news(date_text, deep_news) -> str:
    output_lines = []
    output_lines.append(f"🗓️ {date_text}\n")
    output_lines.append("🔎 오늘의 심층 뉴스입니다.")

    for idx, news in enumerate(deep_news):
        title, url = news["title"], news["url"]
        output_lines.append(f"({idx+1}) {title}")

        body = extract_article_body(url)
        if not body:
            output_lines.append("⚠️ 본문 없음\n")
            continue

        result = summarize_article(body, mode="deep")  # 10~15분 분량 (1500~2000자)
        if result["success"]:
            output_lines.append(f"📝 심층 해설:\n{result['summary']}\n")
            output_lines.append(f"💬 DJ 멘트:\n{result['dj_ment']}\n")
        else:
            output_lines.append(f"⚠️ 요약 실패: {result['error']}\n")

    return "\n".join(output_lines)
