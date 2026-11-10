import yt_dlp
import os

def download_channel_audio(channel_url, custom_path):
    clean_path = custom_path.strip().replace('"', '').replace("'", "")
    output_dir = os.path.abspath(clean_path)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_dir = os.path.join(script_dir, "bin")
    
    os.environ["PATH"] += os.pathsep + ffmpeg_dir

    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': ffmpeg_dir,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
                
        # Időtartam szűrés
        'match_filter': yt_dlp.utils.match_filter_func("duration > 60"),
        
        # Duplikáció védelem
        'nooverwrites': True,
        'download_archive': os.path.join(output_dir, 'downloaded_history.txt'),
        
        # -----------------------------
        'ignoreerrors': True,
        'no_warnings': False,
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\n--- START ---")
            print(f"FFmpeg path: {ffmpeg_dir}")
            ydl.download([channel_url])
            print(f"\nDONE! MP3 files saved to: {output_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    link = input("YouTube link (Channel or Playlist): ")
    mappa = input("Destination folder (No quotes): ")
    download_channel_audio(link, mappa)