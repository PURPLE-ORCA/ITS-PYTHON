import os 
import subprocess
from pathlib import Path

folder = Path(r'C:\Users\purple Orca\Downloads\THUMBNAILS')

folder.mkdir(exist_ok=True)

# CHEKCKING IF THE FOLDER EXIST IF NOT THE PROGRAM WILL EXIT
if not folder.is_dir():
    print(f"❌ Error: Folder not fount. create it or check path")
    exit()
else:
    print(f"✅ Folder found: {folder}")

videos_extensions = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv']

print(f"Scanning for videos in {folder}...")
processed_count = 0
deleted_count = 0
error_count = 0

items_in_folder = list(folder.iterdir())
for item in items_in_folder:
    if item.is_file() and item.suffix.lower() in videos_extensions:
        video_file = item
        processed_count += 1
        print(f"Processing video:{video_file.name}")
        thumbnail_file = folder / f"{video_file.stem}.jpg"

        # SKIP IF THUMBNAIL ALREADY EXIST
        if thumbnail_file.exists():
            print(f"⏩ Thumbnail already exists: {thumbnail_file.name}. Skipping.")
            continue 

        command = [
            "ffmpeg",
            "-ss", "2",
            "-i", str(video_file),
            "-frames:v", "1",
            "-q:v", "2",
            "-y", # Overwrite output without asking
            str(thumbnail_file)
        ]

        try:
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"✅ Thumbnail created for {video_file.name} at {thumbnail_file}")

            try:
                video_file.unlink() # DELETE THE VIDEO FILE AFTER THUMBNAIL IS CREATED
                deleted_count += 1
            except OSError as e:
                error_count += 1
                print(f"❌ Error deleting video {video_file.name}: {e}")
        except subprocess.CalledProcessError as e:
            error_count += 1
            print(f" Commad: {' '.join(command)}") #SHOW THE COMMAND RUN
            print(f"   Error Output:\n{e.stderr.decode()}")
            print(f"  Video NOT deleted due to thumbnail error: {video_file.name}")
            if thumbnail_file.exists():
                try:
                    thumbnail_file.unlink()
                    print(f"  Deleted potentially corrupt thumbnail: {thumbnail_file.name}")
                except OSError as del_e:
                    print(f"  Could not delete potentially corrupt thumbnail {thumbnail_file.name}: {del_e}")

        except FileNotFoundError:
            print(f"❌ Error: 'ffmpeg' command not found. Make sure FFmpeg is installed and in your system's PATH.")
            # Stop the script if ffmpeg isn't found
            break
        except Exception as e: # Catch any other unexpected errors
                    error_count += 1
                    print(f"❌ An unexpected error occurred processing {video_file.name}: {e}")
                    print(f"  Video NOT deleted due to unexpected error: {video_file.name}")

# --- Summary ---
print("\n--- Processing Summary ---")
print(f"Folder scanned: {folder}")
print(f"Video files processed: {processed_count}")
print(f"Videos successfully deleted: {deleted_count}")
print(f"Errors encountered (thumbnail or deletion): {error_count}")
print("--------------------------")