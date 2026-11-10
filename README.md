<div align="center">

# 🎧 sound-fetcher

YouTube channel & playlist audio downloader.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/yt--dlp-Latest-red?style=flat-square&logo=youtube&logoColor=white" alt="yt-dlp">
  <img src="https://img.shields.io/badge/FFmpeg-Embedded-green?style=flat-square&logo=ffmpeg&logoColor=white" alt="FFmpeg">
</p>

*Originally built for my dad to easily load up full playlists and albums onto his car USB stick without dealing with streaming apps.*

</div>

---

### ⚙️ How It Works

Behind the scenes, the script automates the entire processing pipeline through a single prompt:

* **Dynamic Path Resolution & Bin Linking**  
  Detects its execution directory, locates the local `bin/` folder with the standalone `ffmpeg` executables, and dynamically appends it to the system PATH so `yt-dlp` can process audio natively.

* **Audio Extraction & Encoding**  
  Leverages `yt-dlp` and `FFmpegExtractAudio` to pull raw audio streams and encode them directly into clean **192 kbps MP3** files.

* **Flat Output Mapping**  
  Bypasses nested folders by applying a flat output template (`%(title)s.%(ext)s`), saving all tracks straight into your target directory for instant USB transfer.

* **Filtering & History Tracking**  
  Uses an inline duration check (`duration > 60`) to filter out shorts and soundbites, while a local `downloaded_history.txt` archive prevents duplicate downloads.

---

<div align="center">
  <small>made with 🤍 by <a href="https://github.com/czoborieffi">czoborieffi</a></small>
</div>
