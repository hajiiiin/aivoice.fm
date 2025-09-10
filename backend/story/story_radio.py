import json
from openai import OpenAI
import os
from dotenv import load_dotenv

from story.story_filter import story_filter
from story.llm_story_filter import filter_stories_by_llm
from story.narration import narration

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_story_radio():
    story_filter()
    filter_stories_by_llm()
    narration("story/story.json")

if __name__ == "__main__":
    run_story_radio()