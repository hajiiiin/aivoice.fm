from openai import OpenAI
import os
from dotenv import load_dotenv
import json

from story.blocks.block_story_main import block_story_main
from story.blocks.block_story_discussion import block_story_discussion
from story.story_filter.story_filter import story_filter
from story.story_filter.llm_story_filter import filter_stories_by_llm
from story.story_filter.select_discussion_stories import select_discussion_stories

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_story_radio(blocks: list[str], story_path="story/story.json", keyword=None, prev_type=None, context=None) -> str:
    output_lines = []

    # 사연 필터링 + 선정
    story_filter()
    filter_stories_by_llm()

    # 사연 불러오기
    with open(story_path, "r", encoding="utf-8") as f:
        stories = json.load(f)["stories"]

    # 토론 주제로 발전할 사연 번호 선택
    discussion_indices = select_discussion_stories(stories)

    # 사연 공감 및 토론 멘트 생성
    for i, item in enumerate(stories):
        if "story_main" in blocks:
            output_lines.append(block_story_main(item, keyword, prev_type, context))
        if "story_discussion" in blocks and i in discussion_indices:
            output_lines.append(block_story_discussion(item, keyword, prev_type, context))

    return "\n\n".join(output_lines)

if __name__ == "__main__":
    run_story_radio()