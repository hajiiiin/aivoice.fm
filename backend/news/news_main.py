
from news.crawl_kbs_program_news import crawl_kbs_program_news, extract_article_body # news 크롤링
from llm.summarizer import summarize_article # 뉴스 요약, 멘트 생성
from news.news_closing import make_closing_ment # 클로징

def run_news_radio():
    

    # 🗓️ 뉴스 크롤링
    date_text, head_line_news, current_news = crawl_kbs_program_news()
    print(f"🗓️ {date_text}\n")

    # 🌟 헤드라인 뉴스 요약 및 멘트 생성
    print("🌟 오늘의 헤드라인 뉴스입니다.")
    for idx, news in enumerate(head_line_news):

        title, url = news["title"], news["url"]
        print(f"📰 ({idx+1}) {title}")

        body = extract_article_body(url)
        if not body:
            print("⚠️ 본문 없음\n")
            continue

        result = summarize_article(body)
        if result["success"]:
            if not result['dj_ment']:
                print("⚠️ DJ 멘트 파싱 실패, 원문 출력:")
                print(f"{result['content']}\n")
            else : 
                print(f"📝 요약: {result['summary']}")
                print(f"💬 DJ 멘트: {result['dj_ment']}\n")
        else:
            print(f"⚠️ 요약 실패: {result['error']}\n")

        # break  # 테스트 시 첫 뉴스만

    print("🎧 마무리 멘트")
    print(make_closing_ment(current_news))


if __name__ == "__main__":
    run_news_radio()