from random import randint
import os
from sys import argv, exit
from subprocess import Popen

dir = str(argv[1])

if not os.path.isdir(dir):
    print("{} not a directory!\a".format(dir))
    exit()

items = os.listdir(dir)

rand_number = randint(1, len(items))
count = 1


def get_playable_file(_path):
    """Extract a playable file from the path.
    Useful if the random number matches a folder.
    In that case this function will return the path
    to a playable file inside the folder."""

    # First check, if path is a folder.
    if os.path.isdir(_path):
        playable_file = _path
        for file in os.listdir(_path):
            if file.endswith("mp4"):
                playable_file = os.path.join(_path, file)
        return playable_file
    else:
        return _path


for file in items:
    if count == rand_number:
        file_to_open = get_playable_file(os.path.join(dir, file))
        input("Playing {}".format(file_to_open))
        Popen(['mpv',
              '--really-quiet',
              '--save-position-on-quit',
              file_to_open])
        print("Done")
    count += 1
