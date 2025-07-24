import yt_dlp

# Download video or audio from a given URL
def download_media(url: str, format_code: str = 'best') -> str:
    output_path = "downloads/%(title)s.%(ext)s"
    
    ydl_opts = {
        'format': format_code,
        'outtmpl': output_path,
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            downloaded_file = ydl.prepare_filename(info_dict)
            return downloaded_file
    except Exception as e:
        return str(e)
