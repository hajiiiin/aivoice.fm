from news.crawl_kbs_program_news import crawl_kbs_program_news
from news.blocks.block_news_summary import block_news_summary
from news.blocks.block_deep_news import block_deep_news
from news.blocks.block_additional_news import block_additional_news

def run_news_radio(blocks: list[str], keyword: str = None) -> str:
    output_lines = []

    # 🗓️ 뉴스 크롤링 (한 번만 실행)
    date_text, deep_news, head_line_news, current_news = crawl_kbs_program_news()

    # 선택된 블록 실행
    if "headline" in blocks:
        output_lines.append(block_news_summary(date_text, head_line_news))

    if "deep" in blocks:
        output_lines.append(block_deep_news(date_text, deep_news))

    if "current" in blocks:
        output_lines.append(block_additional_news(current_news))

    return "\n".join(output_lines)
