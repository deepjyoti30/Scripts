#!/usr/bin/python3
from random import randint
import os
from sys import argv
from subprocess import Popen


def is_playable(file):
    """Check if the passed file is playable."""
    valid_types = ['mp4', 'mkv', 'avi']

    if file.split('.')[-1] in valid_types:
        return True
    return False


items = []


def get_items(passed_dir):
    """Recursively check the directory to find
    all the files."""
    global items
    passed_dir = os.path.expanduser(passed_dir)

    if not os.path.exists(passed_dir):
        raise FileNotFoundError

    for file in os.listdir(passed_dir):
        if os.path.isdir(os.path.join(passed_dir, file)):
            get_items(os.path.join(passed_dir, file))
        else:
            if is_playable(file):
                items.append(os.path.join(passed_dir, file))


def main():
    dir = str(argv[1])

    get_items(dir)

    rand_number = randint(1, len(items))
    file_to_open = items[rand_number]

    Popen([
            'mpv',
            '--really-quiet',
            '--save-position-on-quit',
            file_to_open
        ])


if __name__ == "__main__":
    main()
