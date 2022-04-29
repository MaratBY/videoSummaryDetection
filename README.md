## Video Summary Detection using Python3

--- 

### Installation and requirements:
- Python >= 3.7

Modules and packages:

`
$ python3 pip install -r requirements.txt
`
---

Additional Functionality: 

If you want to download and test your own video use **/utils/yt_downloader.py** that
allows you to download any video from YouTube by providing the video id of the source
video.
Usage:

`
$ python3 utils/yt_downloader.py -yt_id "5L4DQfVIcdg" -o "./output/" -n "test.mp4"
`

---

First Step is to extract key video frames from video file:

`
$ python3 make_keyframes.py /path/to/video_file.mp4 int float /path/output
`

where: 
- int - sampling rate (x frames per framerate) - e.g. 12
- float - trimming length of the frame per second - e.g. 0.5

---
