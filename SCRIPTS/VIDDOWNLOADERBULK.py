import yt_dlp
import concurrent.futures

def download_video(url):
    ydl_opts = {
        'outtmpl': r'C:\Users\purple Orca\Downloads\DOWNLOADED_VIDEOS/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best' 
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    urls_input = input("Enter video URLs (separated by commas): ")
    urls = [url.strip() for url in urls_input.split(',')]

    print("🚀Starting downloads...")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_video, urls)
    print("✅All downloads complete!")