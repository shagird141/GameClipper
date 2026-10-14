import subprocess
import os

def trim_video(video_path, output_folder, start_time, end_time):
    filename = os.path.splitext(os.path.basename(video_path))[0]
    output_file = os.path.join(output_folder, filename + "_trimmed.mp4")

    duration = float(end_time) - float(start_time)

    command = [
        "ffmpeg",
        "-ss", str(start_time),
        "-i", video_path,
        "-t", str(duration),
        "-c", "copy",
        output_file
    ]

    subprocess.run(command)

    return output_file