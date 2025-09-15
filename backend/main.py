from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
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
    scripts = []

    if selected.get("news"):
        scripts.append({"type": "news", "content": run_news_radio()})
    if selected.get("story"):
        scripts.append({"type": "story", "content": run_story_radio()})
    if selected.get("music"):
        scripts.append({"type": "music", "content": run_music_radio()})

    return {"scripts": scripts}
