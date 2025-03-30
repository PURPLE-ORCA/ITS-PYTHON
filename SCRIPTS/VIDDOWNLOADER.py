import yt_dlp

def download_video(url):
    ydl_opts = {
        'outtmpl': r'C:\Users\purple Orca\Downloads\DOWNLOADED_VIDEOS/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best' 
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Enter URL: ")
    download_video(url)
    print("✅Download complete!")