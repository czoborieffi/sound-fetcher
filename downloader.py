import yt_dlp
import os
import sys

def download_channel_audio(channel_url, custom_path):
    # Útvonal tisztítása
    clean_path = custom_path.strip().replace('"', '').replace("'", "")
    output_dir = os.path.abspath(clean_path)
    
    # A script jelenlegi mappája (ahol az ffmpeg.exe is van)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Hozzáadjuk a rendszer PATH-hoz, hogy a Windows is lássa
    os.environ["PATH"] += os.pathsep + script_dir

    ydl_opts = {
        'format': 'bestaudio/best',
        # Itt adjuk meg a mappát, ahol az exe-k vannak
        'ffmpeg_location': script_dir, 
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # Töröltük a rossz postprocessor_args részt
        'outtmpl': os.path.join(output_dir, '%(uploader)s', '%(title)s.%(ext)s'),
        'ignoreerrors': True,
        'no_warnings': False, # Kapcsold ki a figyelmeztetéseket, hogy lásd a hibákat
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\n--- START ---")
            print(f"FFmpeg search path: {script_dir}")
            ydl.download([channel_url])
            print(f"\nDONE! MP3 files saved to: {output_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    link = input("YouTube link (Channel or Playlist): ")
    mappa = input("Destination folder (No quotes): ")
    download_channel_audio(link, mappa)