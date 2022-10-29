from PyQt5.QtWidgets import  QApplication, QPushButton, QLineEdit, QLabel, QFileDialog, QMessageBox, QMainWindow, QRadioButton, QFileDialog; import PyQt5
import sys
import pytube

#Storing the Playlist URLS in this list
PlayListUrl = []
def SingleVideoDownloader(url, path, type):
    try:
        if type == "MP3":
            video = pytube.YouTube(url)
            video.streams.filter(only_audio=True).first().download(path)
        elif type == "MP4":
            video = pytube.YouTube(url)
            video.streams.filter(only_video=True).first().download(path)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Success")
        msg.setInformativeText("The video has been downloaded successfully")
        msg.setWindowTitle("Success")
        msg.exec_()
    except:
        #if an error occurs, a message box will be displayed
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText("An error occured while downloading the video")
        msg.setWindowTitle("Error")
        msg.exec_()

def PlayListDownloader(url, path, type):
    #loop through the videos in the playlist and append them to the PlayListUrl list
    for video in pytube.Playlist(url).video_urls:
        PlayListUrl.append(video)
    for video in PlayListUrl:
        try:
            if type == "MP3":
                video = pytube.YouTube(video)
                video.streams.filter(only_audio=True).first().download(path)
            elif type == "MP4":
                video = pytube.YouTube(video)
                video.streams.filter(only_video=True).first().download(path)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Success")
            msg.setInformativeText("The video has been downloaded successfully")
            msg.setWindowTitle("Success")
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("An error occured while downloading the playlist")
            msg.setWindowTitle("Error")
            msg.exec_()
    #Clear the list after downloading the playlist
    PlayListUrl.clear()
class Scene(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Youtube Downloader"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 400
        self.InitWindow()
    def InitWindow(self):
        self.setWindowIcon(PyQt5.QtGui.QIcon("youtube.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.UiComponents()
        self.show()
    def UiComponents(self):
        #URL text box
        self.url_label = QLabel("URL", self)
        self.url_label.move(50, 50)
        self.url_label.resize(200, 40)
        self.url_text = QLineEdit(self)
        self.url_text.move(150, 50)
        self.url_text.resize(400, 40)
        #Path label and text
        self.path_label = QLabel("Path", self)
        self.path_label.move(50, 100)
        self.path_label.resize(200, 40)
        self.path_text = QLineEdit(self)
        self.path_text.move(150, 100)
        self.path_text.resize(400, 40)
        #Prevent the user from typing in the path text
        self.path_text.setDisabled(True)
        #a button to open the file explorer
        self.browse_button = QPushButton("Browse", self)
        self.browse_button.move(500, 150)
        self.browse_button.resize(50, 40)
        #Connecting the button to the function
        self.browse_button.clicked.connect(self.browse)
        #Creating the "Download" button
        self.download_button = QPushButton("Download", self)
        self.download_button.move(250, 200)
        self.download_button.resize(100, 40)
        #Connect the button to the download function
        self.download_button.clicked.connect(self.download)
        #Exit Button.
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.move(250, 250)
        self.exit_button.resize(100, 40)
        #Connecting exit button to a function when pressed.
        self.exit_button.clicked.connect(self.exitevent)
        #MP4 or MP3 Radio Buttons
        self.radio_button1 = QRadioButton("MP4", self)
        self.radio_button1.move(50, 160)
        self.radio_button1.resize(100, 40)
        self.radio_button1.setChecked(True)
        self.radio_button2 = QRadioButton("MP3", self)
        self.radio_button2.move(150, 160)
        self.radio_button2.resize(100, 40)
    def browse(self):
        #Open the file explorer and get the path
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.path_text.setText(directory)
    def download(self):
        url = self.url_text.text()
        path = self.path_text.text()
        #Check if the user has selected MP3 or MP4 and get the value
        if self.radio_button1.isChecked():
            type = "MP4"
        else:
            type = "MP3"
        #Check if the user has entered a path.
        if path == "":
            QMessageBox.about(self, "Error", "Please select a path")
        else:
            if "playlist" in url:
                PlayListDownloader(url, path, type)
            else:
                SingleVideoDownloader(url, path, type)
    def exitevent(self):
        ExitConfirmation = QMessageBox.question(self, 'Exit', "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No)
        if ExitConfirmation == QMessageBox.Yes:
            sys.exit()
        else:
            pass
App = QApplication(sys.argv)
window = Scene()
sys.exit(App.exec())
