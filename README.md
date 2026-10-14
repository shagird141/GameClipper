**🎬 GameClipper**

A lightweight Windows desktop application for splitting and trimming videos using FFmpeg.

✨ Features

- **Split Videos:** Divide long videos into smaller clips of a specified duration.
- **Trim Videos:** Extract a specific section of a video using start and end times.
- **Simple Interface:** Easy-to-use graphical interface built with CustomTkinter.
- **Quality Preservation: Uses stream copying to avoid unnecessary re-encoding where supported.

**🛠️ Requirements**

- Windows
- Python 3
- FFmpeg installed and available in your system PATH

**🚀 Installation**

1. Install [Python](https://www.python.org/downloads/).
2. Install [FFmpeg](https://ffmpeg.org/download.html) and add it to your system PATH.
3. Download this repository by clicking **Code → Download ZIP**.
4. Extract the ZIP file.
5. Open a terminal inside the extracted GameClipper folder.
6. Install the required Python package:

   ```bash
   py -m pip install -r requirements.txt
   ```

**▶️ How to Run**

Double-click `run.bat` inside the GameClipper folder.

Follow the instructions in the application to select your video, choose an output folder, and split or trim your video.

**📁 Project Structure**

- `main.py` — Main application interface.
- `splitter.py` — Video-splitting functionality.
- `trimmer.py` — Video-trimming functionality.
- `hooks.py` — Hook text templates.
- `requirements.txt` — Python dependencies.
- `run.bat` — Windows launcher.

**📌 Project Status**

GameClipper is an early-stage project. More features and improvements may be added in the future.

**📄 License**

No license has been added yet.
