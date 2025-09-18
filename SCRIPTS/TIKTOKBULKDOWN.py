import subprocess
import os
import sys

def download_tiktoks_the_sane_way(username):

    print("Checking for yt-dlp updates...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"])
    except Exception as e:
        print(f"Couldn't update yt-dlp, Error: {e}")

    output_dir = f"tiktoks_{username}"
    os.makedirs(output_dir, exist_ok=True)
    print(f"Saving ONLY VIDEOS to '{output_dir}'")

    profile_url = f"https://www.tiktok.com/@{username}"
    cookies_file = "cookies.txt" 

    if not os.path.exists(cookies_file):
        print("\n!!! WARNING: `cookies.txt` not found. !!!")

    command = [
        sys.executable,
        "-m", "yt_dlp",
        "--cookies", cookies_file, 
        

        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        
        "--output", os.path.join(output_dir, f"{username}_%(id)s.%(ext)s"),
        "--merge-output-format", "mp4", # Ensure the final file is always mp4
        "--ignore-errors",
        "--no-overwrites",
        "--sleep-interval", "5", 
        "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        profile_url
    ]

    print(f"\nRunning command: {' '.join(command)}\n")
    subprocess.run(command)

    print(f"\nDone. MP3-free zone.")


if __name__ == "__main__":
    username_to_download = "soy.aleidaramirez"
    download_tiktoks_the_sane_way(username_to_download)