import itunespy
from sys import argv

album_name = str(argv[1:])

album = itunespy.search_album(album_name)
tracks = album[0].get_tracks()

for track in tracks:
    print(track.track_name)