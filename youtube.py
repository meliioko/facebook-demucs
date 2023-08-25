import os
import yt_dlp

DIRECTORY = 'music'

def download_audio(video_id: str, playlist_id: str, directory: str = DIRECTORY):
    """Download the audio given in parameter"""
    
    if playlist_id is None:
        audio_path = f"{directory}/{video_id}.mp3"
    else:
        audio_path = f"{directory}/{playlist_id}/{video_id}.mp3"

    # Download the audio from YouTube.
    ydl_opts = {
        "format": "bestaudio/mp3",
        "outtmpl": audio_path,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(["https://www.youtube.com/watch?v=" + video_id])

    return audio_path


if __name__ == '__main__':
    import sys

    videoId = sys.argv[1]
    dir = sys.argv[2]
    download_audio(videoId, playlist_id=None, directory=dir)
