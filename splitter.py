import subprocess
import os

def split_video(video_path, output_folder, duration):
    output_pattern = os.path.join(output_folder, "clip_%03d.mp4")

    command = [
        "ffmpeg",
        "-i", video_path,
        "-c", "copy",
        "-map", "0",
        "-f", "segment",
        "-segment_time", str(duration),
        "-reset_timestamps", "1",
        output_pattern
    ]

    subprocess.run(command)