from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)
yd = yt.streams.get_highest_resolution()


# Download an entire playlist
"""
from pytube import Playlist
p = Playlist(link)
for video in p.videos:
    video.streams.get_highest_resolution().download('D:\Jirka\Movies\Videa')
"""

# The directory where you want to download to
yd.download('D:\Jirka\Movies\Videa')