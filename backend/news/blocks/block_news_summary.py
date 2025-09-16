from news.crawl_kbs_program_news import extract_article_body
from news.llm.summarizer import summarize_article

def block_news_summary(date_text, head_line_news) -> str:
    output_lines = []
    output_lines.append(f"🗓️ {date_text}\n")
    output_lines.append("🌟 오늘의 헤드라인 뉴스입니다.")

    for idx, news in enumerate(head_line_news):
        title, url = news["title"], news["url"]
        output_lines.append(f"📰 ({idx+1}) {title}")

        body = extract_article_body(url)
        if not body:
            output_lines.append("⚠️ 본문 없음\n")
            continue

        result = summarize_article(body)
        if result["success"]:
            # 한 뉴스당 5분 분량 (700~800자) 확보
            output_lines.append(f"📝 해설 요약:\n{result['summary']}\n")
            output_lines.append(f"💬 DJ 멘트:\n{result['dj_ment']}\n")
        else:
            output_lines.append(f"⚠️ 요약 실패: {result['error']}\n")
    
    return "\n".join(output_lines)