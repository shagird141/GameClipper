import customtkinter as ctk
from tkinter import filedialog
import splitter
import trimmer

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Game Clipper")
app.geometry("550x600")

video_path = ""
output_folder = ""

def browse_video():
    global video_path
    video_path = filedialog.askopenfilename(
        filetypes=[("Video Files", "*.mp4 *.mkv *.avi *.mov")]
    )
    video_label.configure(text=video_path)

def browse_output():
    global output_folder
    output_folder = filedialog.askdirectory()
    output_label.configure(text=output_folder)

def create():
    duration = duration_entry.get()

    if video_path == "" or output_folder == "":
        status.configure(text="Select a video and output folder.")
        return

    splitter.split_video(video_path, output_folder, duration)
    status.configure(text="Finished!")


# ← Paste Step 4 here

def browse_trim_video():
    global trim_video
    trim_video = filedialog.askopenfilename(
        filetypes=[("Video Files", "*.mp4 *.mkv *.avi *.mov")]
    )
    trim_label.configure(text=trim_video)


def trim():
    if trim_video == "" or output_folder == "":
        status.configure(text="Select a trim video and output folder.")
        return

    try:
        start = float(start_entry.get())
        end = float(end_entry.get())
    except ValueError:
        status.configure(text="Invalid start/end time.")
        return

    trimmer.trim_video(trim_video, output_folder, start, end)

    status.configure(text="Trim complete!")


title = ctk.CTkLabel(app, text="🎬 Game Clipper", font=("Arial", 24))
title.pack(pady=15)

ctk.CTkButton(app, text="Browse Video", command=browse_video).pack(pady=5)
video_label = ctk.CTkLabel(app, text="No video selected")
video_label.pack()

ctk.CTkButton(app, text="Output Folder", command=browse_output).pack(pady=5)
output_label = ctk.CTkLabel(app, text="No output folder selected")
output_label.pack()

duration_entry = ctk.CTkEntry(app, placeholder_text="Clip duration (seconds)")
duration_entry.insert(0, "30")
duration_entry.pack(pady=10)

ctk.CTkButton(app, text="Create Clips", command=create).pack(pady=15)

status = ctk.CTkLabel(app, text="Ready")
status.pack()
ctk.CTkLabel(app, text="------------------------------------").pack(pady=10)

trim_title = ctk.CTkLabel(app, text="✂ Trim Video", font=("Arial", 20))
trim_title.pack(pady=5)

trim_video = ""
ctk.CTkButton(app, text="Browse Trim Video", command=browse_trim_video).pack(pady=5)

trim_label = ctk.CTkLabel(app, text="No trim video selected")
trim_label.pack()

start_entry = ctk.CTkEntry(app, placeholder_text="Start Time (seconds)")
start_entry.pack(pady=5)

end_entry = ctk.CTkEntry(app, placeholder_text="End Time (seconds)")
end_entry.pack(pady=5)

ctk.CTkButton(app, text="Trim Video", command=trim).pack(pady=10)
app.mainloop()