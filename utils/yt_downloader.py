from pytube import YouTube
import argparse

def download_video(url, save_to):
    yt = YouTube(url)
    yt.streams.filter(only_video=True, progressive=False, res="720p").first().download(save_to)
    return None

link = "https://www.youtube.com/watch?v=5L4DQfVIcdg"

