from random import randint
import os
from sys import argv, exit
from subprocess import Popen


items = []


def get_items(passed_dir, blacklist=[]):
    """Recursively check the directory to find
    all the files."""
    global items
    passed_dir = os.path.expanduser(passed_dir)

    if not os.path.exists(passed_dir):
        raise FileNotFoundError

    for file in os.listdir(passed_dir):
        if os.path.isdir(os.path.join(passed_dir, file)):
            temp_items = get_items(os.path.join(passed_dir, file))
            items.append(temp_items)
        else:
            if file[file.find('.') + 1:] not in blacklist:
                items.append(os.path.join(passed_dir, file))
    return items


def main():
    dir = str(argv[1])
    whitelist = str(argv[2:])

    items = get_items(dir, whitelist)

    rand_number = randint(1, len(items))

    print("Randome file is {}".format(items[rand_number]))
    input()


if __name__ == "__main__":
    main()
