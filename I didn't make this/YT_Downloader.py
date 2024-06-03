from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

# url = "https://www.youtube.com/watch?v=34HY91kXkIg"
# save_path = "C:/Users/sampl/OneDrive/Desktop/IMPORTANT/Coding Things/YT Videos downloaded"

# download_video(url, save_path)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
        return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube url:\n")
    save_dir = open_file_dialog()

    if not save_dir:
        print("Invalid save location.")
    else:
        print("Started Download...")
        download_video(video_url, save_dir)