from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from app.opening import generate_opening_ment
from app.closing import generate_closing_ment
from news.news_radio import run_news_radio
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

# 블록 매핑
BLOCK_HANDLERS = {
    # 뉴스
    "headline": lambda keyword: {"type": "headline", "content": run_news_radio(["headline"], keyword=keyword)},
    "deep": lambda keyword: {"type": "deep", "content": run_news_radio(["deep"], keyword=keyword)},
    "current": lambda keyword: {"type": "current", "content": run_news_radio(["current"], keyword=keyword)},

    # 사연
    "story_main": lambda keyword: {"type": "story_main", "content": run_story_radio(["story_main"], keyword=keyword)},
    "story_discussion": lambda keyword: {"type": "story_discussion", "content": run_story_radio(["story_discussion"], keyword=keyword)},

    # 음악
    "music_history": lambda keyword: {"type": "music_history", "content": run_music_radio(["music_history"], keyword=keyword)},
    "music_trend": lambda keyword: {"type": "music_trend", "content":  run_music_radio(["music_trend"], keyword=keyword)},
    "music_genre": lambda keyword: {"type": "music_genre", "content":  run_music_radio(["music_genre"], keyword=keyword)},
    "music_artist": lambda keyword: {"type": "music_artist", "content":  run_music_radio(["music_artist"], keyword=keyword)},
}


@app.post("/api/run-radio")
def run_radio(selected: dict = Body(...)):
    blocks = selected.get("blocks", [])
    keyword = selected.get("keyword", None)
    scripts = []

    # 오프닝 
    scripts.append({"type": "opening", "content": generate_opening_ment(keyword)})

    # 선택된 블록 순서대로 실행
    for block in blocks:
        if block in BLOCK_HANDLERS:
            scripts.append(BLOCK_HANDLERS[block](keyword))

    # 클로징        
    scripts.append({"type": "closing", "content": generate_closing_ment(keyword)})

    return {"scripts": scripts}
