"""A simple script to set metadata manually."""
import os
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, TCON, TRCK, TYER
from mutagen.mp3 import MP3
from sys import argv


class metadata:
    """A metadata class to store the stuff."""
    def __init__(self):
        self.release_date = ''
        self.track_name = ''
        self.artist_name = ''
        self.collection_name = ''
        self.track_number = 1
        self.primary_genre_name = ''

    def get_input(self):
        """Ask the user to give some inputs."""
        self.release_date = input("Enter the release date. "\
                                  .format(self.release_date))
        self.track_name = input("Enter name of the track. "\
                                .format(self.track_name))
        self.artist_name = input("Enter name of the artist. "\
                                .format(self.artist_name))
        self.collection_name = input("Enter name of the collection. "\
                                    .format(self.collection_name))
        self.track_number = input("Enter number of the track. "\
                                  .format(self.track_number))
        self.primary_genre_name = input("Enter genre of the track. "\
                                        .format(self.primary_genre_name))

    def ret_data(self):
        """Return the metadata."""
        return self


class setMetadata:
    """A setMetadata class to set data."""

    def __init__(self, path, cover):
        self.SONG_PATH = path
        self.cover = cover
        self.__checkexistence()

    def __checkexistence(self):
        """Check if the passed song path exists."""
        if not os.path.isfile(self.SONG_PATH):
            print("{}: does not exist".format(self.SONG_PATH))
            exit(-1)

    def set_data(self, song_data):
        """Set the song data in the song."""
        IS_IMG_ADDED = False

        SONG_PATH = self.SONG_PATH

        audio = MP3(SONG_PATH, ID3=ID3)
        data = ID3(SONG_PATH)

        # If cover is not None then add it
        if self.cover is not None:
            if not os.path.isfile(self.cover):
                print("{}: does not exist. Skipping..".format(self.cover))
            else:
                imagedata = open(self.cover, 'rb').read()
                data.add(APIC(3, 'image/jpeg', 3, 'Front cover', imagedata))
                # REmove the image
                IS_IMG_ADDED = True

        # If tags are not present then add them
        try:
            audio.add_tags()
        except Exception:
            pass

        audio.save()

        data.add(TYER(encoding=3, text=song_data.release_date))
        data.add(TIT2(encoding=3, text=song_data.track_name))
        data.add(TPE1(encoding=3, text=song_data.artist_name))
        data.add(TALB(encoding=3, text=song_data.collection_name))
        data.add(TCON(encoding=3, text=song_data.primary_genre_name))
        data.add(TRCK(encoding=3, text=str(song_data.track_number)))

        data.save()

        # Show the written stuff in a better format
        print('================================')
        print('  || YEAR: ' + song_data.release_date)
        print('  || TITLE: ' + song_data.track_name)
        print('  || ARITST: ' + song_data.artist_name)
        print('  || ALBUM: ' + song_data.collection_name)
        print('  || GENRE: ' + song_data.primary_genre_name)
        print('  || TRACK NO: ' + str(song_data.track_number))

        if IS_IMG_ADDED:
            print('  || ALBUM COVER ADDED')

        print('================================')


if __name__ == "__main__":
    if len(argv) < 2:
        print("Insufficient data")
        exit(-1)

    path = str(argv[1])
    cover = None

    try:
        cover = argv[2]
    except IndexError:
        pass

    song = setMetadata(path, cover)
    data = metadata()
    data.get_input()
    # input(data.ret_data())
    song.set_data(data.ret_data())
