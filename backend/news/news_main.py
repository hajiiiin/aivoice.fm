
from news.crawl_kbs_program_news import crawl_kbs_program_news, extract_article_body # news 크롤링
from llm.summarizer import summarize_article # 뉴스 요약, 멘트 생성
from news.news_closing import make_closing_ment # 클로징

def run_news_radio():
    output_lines = []

    # 🗓️ 뉴스 크롤링
    date_text, head_line_news, current_news = crawl_kbs_program_news()
    output_lines.append(f"🗓️ {date_text}\n")

    # 🌟 헤드라인 뉴스 요약 및 멘트 생성
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
            if not result['dj_ment']:
                output_lines.append("⚠️ DJ 멘트 파싱 실패, 원문 출력:")
                output_lines.append(result['content'])
            else:
                output_lines.append(f"📝 요약: {result['summary']}")
                output_lines.append(f"💬 DJ 멘트: {result['dj_ment']}\n")
        else:
            output_lines.append(f"⚠️ 요약 실패: {result['error']}\n")

        # break  # 첫 뉴스만 테스트 시

    output_lines.append("🎧 마무리 멘트")
    output_lines.append(make_closing_ment(current_news))

    # 문자열로 합쳐서 리턴
    return "\n".join(output_lines)


if __name__ == "__main__":
    run_news_radio()