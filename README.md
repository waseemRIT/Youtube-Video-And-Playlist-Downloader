# YouTube Video and Playlist Downloader
This is a powerful YouTube video and playlist downloader tool built using `Python` and the `Pytube library`. 
The tool allows for the easy download of both individual videos and entire playlists in a convenient and user-friendly manner.
## Requirements
* Python
* Pytube library

## Installation
To use the program, you will need to install the required libraries by running the `install.bat` file. This will install the necessary packages listed in the `requirement.txt` file.

## Usage
The program is equipped with two main functions: `SingleVideoDownloader` and `PlayListDownloader`.

### SingleVideoDownloader
```py
SingleVideoDownloader(url, path)
```
This function enables you to download a single video by providing two arguments:

-> url: the YouTube video URL you wish to download.
-> path: the local path where you wish to save the downloaded video.

### PlayListDownloader
```py
PlayListDownloader(url, path)
```
This function allows you to download an entire playlist at once, by providing two arguments:

-> url: The YouTube playlist URL you wish to download.
-> path: The local path where you wish to save the downloaded videos.

You can execute the python file by opening a Command Prompt, and typing py Downloader.py or by running the run.bat file.

## Future Advancements
* Add support for more video/audio formats.
* Implement a feature to select and download only specific videos from a playlist.
* Allow user to input their preferred video and audio qualities to download.
* Implement multithreading to speed up download time.
* Integrate user-authentication to support downloading private videos and playlists.

# Note
The script uses a global list PlayListUrl to store URLs of videos in a playlist. This list is cleared after the playlist has been downloaded.

This tool is provided as a starting point for your own projects, it is important to understand how the code works and to follow best practices for writing clean and maintainable code. Also, please note that this script may not work if YouTube updates their way of serving videos, thus it's just a prototype. However, you can contribute to the project to keep it updated.
