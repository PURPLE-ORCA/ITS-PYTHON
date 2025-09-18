import subprocess
import os
import sys

# --- CONFIGURATION ---
# If ffmpeg isn't in your PATH, you'll need to provide the full path to ffmpeg.exe
# e.g., FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"
FFMPEG_PATH = "ffmpeg" # Assumes ffmpeg is in your system PATH

# --- END CONFIGURATION ---

def check_ffmpeg():
    """Crude check to see if ffmpeg is callable."""
    try:
        process = subprocess.run([FFMPEG_PATH, "-version"], capture_output=True, text=True, check=False)
        if process.returncode == 0 and "ffmpeg version" in process.stdout.lower():
            print("FFmpeg found. Good. Maybe this won't be a total disaster.")
            return True
        else:
            print("FFmpeg version check failed or output unexpected.")
            print(f"Stdout: {process.stdout}")
            print(f"Stderr: {process.stderr}")
            return False
    except FileNotFoundError:
        print(f"ERROR: FFmpeg not found at '{FFMPEG_PATH}'.")
        print("Is it installed and in your system PATH? Or did you set FFMPEG_PATH correctly in the script?")
        print("No FFmpeg, no party. This script is now just expensive decoration.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while checking for FFmpeg: {e}")
        return False

def convert_dav_to_mp4(dav_filepath, output_folder):
    """
    Attempts to convert a .dav file to .mp4 using FFmpeg.
    This is more art than science with .dav files, so good luck.
    """
    if not os.path.exists(dav_filepath):
        print(f"Dude, the input file doesn't exist: {dav_filepath}")
        return False

    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder, exist_ok=True)
            print(f"Created output folder: {output_folder}")
        except OSError as e:
            print(f"Could not create output folder: {output_folder}. Error: {e}")
            return False

    filename = os.path.basename(dav_filepath)
    name_without_ext = os.path.splitext(filename)[0]
    mp4_filename = f"{name_without_ext}.mp4"
    mp4_filepath = os.path.join(output_folder, mp4_filename)

    print(f"Attempting to convert '{dav_filepath}' to '{mp4_filepath}'...")

    # The FFmpeg command. This is where the dark magic (or abject failure) happens.
    # -y: Overwrite output files without asking (be careful!)
    # -i: Input file
    # -c:v libx264: Video codec - good ol' H.264 for compatibility.
    # -c:a aac: Audio codec - Advanced Audio Coding, also widely compatible.
    # -b:a 192k: Audio bitrate. Adjust if needed.
    # -vf "setpts=PTS*1": This is a Hail Mary for DAV files with weird timestamps.
    #                      Sometimes DAV files are raw streams and FFmpeg needs help with timing.
    #                      If your video is sped up or slowed down, you might need to experiment
    #                      with the multiplier (e.g., PTS*0.5 for half speed if it's too fast).
    #                      Or remove it entirely if it causes issues.
    #                      Some sources suggest `-r <fps>` if you know the framerate.
    #                      Another common one for Dahua DAVs is `-bsf:v h264_mp4toannexb` BEFORE -c:v copy if you wanted to try copying the stream.
    #                      But for broad compatibility, re-encoding is safer.
    cmd = [
        FFMPEG_PATH,
        "-y",
        "-i", dav_filepath,
        # Uncomment one of the following video codec lines or add your own.
        # Option 1: Re-encode to H.264 (generally safer for compatibility)
        "-c:v", "libx264",
        "-preset", "medium", # encoding speed/quality trade-off
        "-crf", "23",        # quality level (lower is better, 18-28 is sane)
        # Option 2: Try to copy the video stream (faster, but only if it's already H.264/H.265 compatible with MP4)
        # "-c:v", "copy",
        # Audio: Re-encode to AAC (safer)
        "-c:a", "aac",
        "-b:a", "192k",
        # Sometimes DAV files have screwy presentation timestamps (PTS). This MIGHT help. Or not.
        # "-vf", "setpts=N/FRAME_RATE/TB", # This is complex and depends on knowing frame rate
        # "-vf", "setpts=PTS/1.0", # A simpler attempt, might need adjustment or removal
        mp4_filepath
    ]

    # For some specific DAV types (e.g., Dahua H.264), you might need to tell FFmpeg it's a raw H.264 stream:
    # cmd_raw_h264 = [FFMPEG_PATH, "-y", "-f", "h264", "-i", dav_filepath, "-c:v", "copy", mp4_filepath]
    # You'd have to know it's raw H.264 for that to work.

    print(f"Executing command: {' '.join(cmd)}")

    try:
        process = subprocess.run(cmd, capture_output=True, text=True, check=False) # Set check=True to raise exception on non-zero exit
        if process.returncode == 0:
            print(f"SUCCESS! Or at least FFmpeg didn't immediately cry. Check '{mp4_filepath}'.")
            return True
        else:
            print(f"FAIL! FFmpeg threw a tantrum. Return code: {process.returncode}")
            print("FFmpeg STDOUT:")
            print(process.stdout)
            print("FFmpeg STDERR (this is usually where the juicy error messages are):")
            print(process.stderr)
            return False
    except FileNotFoundError:
        print(f"ERROR: FFmpeg not found at '{FFMPEG_PATH}'. Seriously, did you install it and check the path?")
        return False
    except Exception as e:
        print(f"An unholy error occurred during conversion: {e}")
        return False

def main():
    print("DAV to MP4 Converter - The 'It Might Work™' Edition")
    print("=" * 50)

    if not check_ffmpeg():
        sys.exit(1) # Exit if FFmpeg isn't good to go

    # --- USER: SET THESE ---
    input_directory = r"C:\Users\purple Orca\Downloads\towatch"  # Current directory. Change to your DAV folder, e.g., r"D:\PURPLE USB"
    output_directory = os.path.join(input_directory, "converted_mp4s") # Subfolder for MP4s
    # --- END USER SETTINGS ---

    if not os.path.isdir(input_directory):
        print(f"Input directory '{input_directory}' doesn't exist. Quitting. Try harder.")
        sys.exit(1)

    if not os.path.exists(output_directory):
        try:
            os.makedirs(output_directory)
            print(f"Created output directory: {output_directory}")
        except OSError as e:
            print(f"Could not create output directory '{output_directory}'. Error: {e}. Quitting.")
            sys.exit(1)
    
    dav_files_found = 0
    successful_conversions = 0

    for item in os.listdir(input_directory):
        if item.lower().endswith(".dav"):
            dav_files_found += 1
            dav_filepath = os.path.join(input_directory, item)
            print("-" * 30)
            if convert_dav_to_mp4(dav_filepath, output_directory):
                successful_conversions +=1
    
    print("=" * 50)
    if dav_files_found == 0:
        print(f"No .dav files found in '{input_directory}'. Are you sure you pointed me to the right place?")
    else:
        print(f"Processed {dav_files_found} .dav file(s).")
        print(f"Successfully converted: {successful_conversions}")
        print(f"Failed/Skipped: {dav_files_found - successful_conversions}")
        if successful_conversions > 0:
            print(f"Check the '{output_directory}' folder for your (hopefully) shiny new MP4s.")
        if successful_conversions < dav_files_found:
            print("For the failed ones, scroll up and look at the FFmpeg error messages. They're your only clue.")

if __name__ == "__main__":
    main()