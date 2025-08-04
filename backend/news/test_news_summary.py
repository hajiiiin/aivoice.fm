from crawler import crawl_naver_category_news, NAVER_NEWS_CATEGORIES
from summarizer import summarize_news_titles

if __name__ == "__main__":
    all_news = []
    print("==📡 수집된 뉴스 ==")
    for category, url in NAVER_NEWS_CATEGORIES.items():
        print(f"\n[📚 {category} 뉴스]")
        items = crawl_naver_category_news(category, url, limit=3)
        for item in items:
            print(f"- {item['title']}")
            all_news.append(item)

    print("\n📰 [한 줄 뉴스 요약]")
    summary = summarize_news_titles(all_news)
    print(summary)
