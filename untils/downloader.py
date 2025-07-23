import yt_dlp
import os
import uuid

def download_media(url, media_type="video"):
    file_id = str(uuid.uuid4())
    output = f"/tmp/{file_id}.%(ext)s"
    
    ydl_opts = {
        "format": "bestaudio/best" if media_type == "audio" else "best",
        "outtmpl": output,
        "noplaylist": True,
        "quiet": True,
    }

    if media_type == "audio":
        ydl_opts.update({
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }]
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            downloaded_file = ydl.prepare_filename(info)
            if media_type == "audio":
                downloaded_file = downloaded_file.rsplit(".", 1)[0] + ".mp3"
            return downloaded_file
    except Exception as e:
        return f"[❌ Download failed: {e}]"
