from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from app.opening import generate_opening_ment
from app.closing import generate_closing_ment
from news.news_main import run_news_radio
from story.story_radio import run_story_radio
from music.music_radio import run_music_radio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/run-radio")
def run_radio(selected: dict = Body(...)):
    blocks = selected.get("blocks", [])
    keyword = selected.get("keyword", None)
    scripts = []

    scripts.append({"type": "opening", "content": generate_opening_ment(keyword)})

    if any(b in blocks for b in ["headline", "deep", "current"]):
        scripts.append({"type": "news", "content": run_news_radio(blocks)})

    if "story" in blocks:
        scripts.append({"type": "story", "content": run_story_radio()})

    if "music" in blocks:
        scripts.append({"type": "music", "content": run_music_radio()})

    scripts.append({"type": "closing", "content": generate_closing_ment(keyword)})

    return {"scripts": scripts}
