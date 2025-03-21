import subprocess

video_url = input("Enter the video URL (.mp4 or .m3u8): ")
output_file = r"C:\Users\purple Orca\Downloads\pinterest_video.mp4"

subprocess.run(["yt-dlp", "--force-overwrites", "-o", output_file, video_url])
print("Download complete!")