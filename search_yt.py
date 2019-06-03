'''
Just a simple script to search youtube and pass the url

Will use it with mpv to directly watch videos from the cli.
'''

import requests
from bs4 import BeautifulSoup
from sys import argv


def search(querry):
    """Search the querry in youtube and return lim number of results.

    Querry is the keyword, i:e name of the song
    lim is the number of songs that will be added to video array and returned
    """
    # Initialize some tuples
    video = []

    # Replace all the spaces with +
    querry = querry.replace(' ', '+')

    url = "https://www.youtube.com/results?search_query={}".format(querry)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # count = 0
    video = soup.findAll('a', attrs={'class': 'yt-uix-tile-link'})[0]
    return video['href']


if __name__ == '__main__':
    querry = ' '.join(argv[1:])
    url = 'https://youtube.com' + search(querry)
    print(url)
