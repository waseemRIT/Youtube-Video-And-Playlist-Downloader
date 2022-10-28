from json.tool import main; import PyQt5
import sys
from PyQt5.QtWidgets import  QApplication, QPushButton, QLineEdit, QLabel, QFileDialog, QMessageBox, QMainWindow, QRadioButton, QFileDialog
import pytube

#a function to download the video as a MP3 or MP4 file, takes the URL, the path and the format as parameters
def VideoDownloader(url, path, type):
    try:
        if type == "MP3":
            video = pytube.YouTube(url)
            video.streams.filter(only_audio=True).first().download(path)
        elif type == "MP4":
            video = pytube.YouTube(url)
            video.streams.filter(only_video=True).first().download(path)
    except:
        print("Error")

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Youtube Downloader"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 400
        self.InitWindow()