from pytube import YouTube
import tkinter as tk
from tkinter import *
from tkinter import messagebox
def valid_link(link):
    try:
        YouTube(link)
        return True
    except:
        return False
def download_video(link, file_format):
    yt = YouTube(link)
    messagebox.showinfo("Download Started", f"Video started downloading...")
    video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if video_stream:
        video_stream.download(filename=f'video.{file_format}')
        print(f"Your video has been downloaded as video.{file_format}")
        messagebox.showinfo("Download Complete", f"Your video has been saved as video.{file_format}")
    else:
        messagebox.showwarning("No Video Available", "No video available.")
def download_audio(link, file_format):
    yt = YouTube(link)
    audio_stream = yt.streams.filter(only_audio=True).first()
    messagebox.showinfo("Download Started", f"Audio started downloading...")
    if audio_stream:
        audio_stream.download(filename=f'audio.{file_format}')
        print(f"Your video has been downloaded as audio.{file_format}")
        messagebox.showinfo("Download Complete", f"Audio has been saved as audio.{file_format}")
    else:
        messagebox.showwarning("No Audio Available", "No audio available.")
def download_but(link_entry, format_choice):
    link = link_entry.get()
    file_format = format_choice.get().lower()
    if valid_link(link):
        if file_format in ['mp3', 'mp4']:
            if file_format == 'mp3':
                download_audio(link, file_format)
            elif file_format == 'mp4':
                download_video(link, file_format)
        else:
            messagebox.showwarning("Invalid Choice", "Invalid!! Please select 'mp3' or 'mp4'.")
    else:
        messagebox.showwarning("Invalid Link", "Please enter a valid link.")
def main():
    root = tk.Tk()
    root.title("Downloader")
    root.configure(bg = "light blue")
    heading_label = tk.Label(root, text="YouTube Video & Audio Downloader", bg="light blue", font= ("Helvetica", 20, "bold"))
    heading_label.pack(pady=10)
    link_label = tk.Label(root, text="Enter your link:", bg="light blue", font= ("Helvetica", 14))
    link_label.pack()
    link_entry = tk.Entry(root, width=40, font= ("Helvetica", 14))
    link_entry.pack()
    format_choice = tk.StringVar()
    format_label = tk.Label(root, text="Choose file format:", bg="light blue", font= ("Helvetica", 14))
    format_label.pack()
    format_menu = tk.OptionMenu(root,format_choice, 'mp3', 'mp4')
    format_menu.config(bg="light blue", font= ("Helvetica", 14))
    format_menu.pack(pady=5)
    download_button = tk.Button(root, text="Download", command=lambda: download_but(link_entry, format_choice), bg="green", fg="white", height=2, width=20, font= ("Helvetica", 14))
    download_button.pack()

    root.mainloop()
if __name__ == "__main__":
    main()

