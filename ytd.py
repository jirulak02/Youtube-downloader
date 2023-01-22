from pytube import YouTube
from sys import argv

link = argv[1]
directory = argv[2]
yt = YouTube(link)
yd = yt.streams.get_highest_resolution()


# Download an entire playlist
"""
from pytube import Playlist
p = Playlist(link)
for video in p.videos:
    video.streams.get_highest_resolution().download(directory)
"""

yd.download(directory)