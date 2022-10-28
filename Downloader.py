from json.tool import main; import PyQt5
import sys
from PyQt5.QtWidgets import  QApplication, QPushButton, QLineEdit, QLabel, QFileDialog, QMessageBox, QMainWindow, QRadioButton, QFileDialog
import youtube_dl

#a function to download the video as a MP3 or MP4 file, takes the URL, the path and the format as parameters
def VideoDownloader(url, path, type):
    try:
        if type == "MP3":
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': path + '/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        else:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': path + '/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }],
            }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except:
        print("Error")