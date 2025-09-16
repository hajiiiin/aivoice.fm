from music.blocks.block_music_history import block_music_history
from music.blocks.block_music_trend import block_music_trend
from music.blocks.block_music_genre import block_music_genre
from music.blocks.block_music_artist import block_music_artist

def run_music_radio(blocks: list[str], keyword: str = None) -> str:
    output_lines = []

    for b in blocks:
        if b == "music_history":
            output_lines.append(block_music_history(keyword))
        elif b == "music_trend":
            output_lines.append(block_music_trend(keyword))
        elif b == "music_genre":
            output_lines.append(block_music_genre(keyword))
        elif b == "music_artist":
            output_lines.append(block_music_artist(keyword))

    return "\n\n".join(output_lines)
