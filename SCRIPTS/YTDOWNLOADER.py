import yt_dlp

def download_video(url, save_path="."):
    ydl_opts = {"outtmpl": f"{save_path}/%(title)s.%(ext)s"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter YouTube URL: ")
    download_video(video_url)
