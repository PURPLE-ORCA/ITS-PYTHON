import yt_dlp
import os

def downlaad_audio(url, download_path=r'C:\Users\purple Orca\Downloads\AUDIOS'):
    os.makedirs(download_path, exist_ok=True)  

    ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }],
            'addmetadata': True,
            'embedthumbnail': True,
    }

    print(f"Attempting to doawload autio from: {url}")
    print(f"Saving to:{download_path}")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅Download complete!")
    except yt_dlp.utils.DownloadError as e:
        print(f"❌Download failed: {e}")
    except Exception as e:
        print(f"❌An unexpected error occurred: {e}")


if __name__ == "__main__":
    video_url = input("Enter the url:")
    if video_url:
        downlaad_audio(video_url)
    else:
        print("❌No URL provided.")

