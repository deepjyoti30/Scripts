# Scripts

## [download.py](https://github.com/deepjyoti30/Scripts/blob/master/download.py)

#### Downloader script written in python.

```
usage: download.py [-h] URL [des]

positional arguments:
  URL         URL of the file
  des         The name of the file to be saved with.

optional arguments:
  -h, --help  show this help message and exit
```

## [get_album.py](https://github.com/deepjyoti30/Scripts/blob/master/get_album.py)

#### Script that uses itunespy to get songs present in the passed album name.

```
usage: python get_album.py albumname

albumname: Name of the album you want songs for.
```

## [lock.sh](https://github.com/deepjyoti30/Scripts/blob/master/lock.sh)

#### Shell script to make a beautiful lockscreen. Uses i3lock.

```
USAGE: ./lock.sh [path_to_img] [path_to_user_img]

Optional arguments:

  path_to_img:      Path to the image to be used as background.
  path_to_user_img: Path to the image to be used as user image.

```

### Tip: Update the two paths inside the script to get it to work.

## [setMetadata.py](https://github.com/deepjyoti30/Scripts/blob/master/setMetadata.py)

#### Interactive metadata setter written in python.

```
Usage: python setMetadata.py MP3_file [albumcover]

MP3_file: path to mp3 file.
albumcover: Path to albumcover. If not passed then this is skipped.
```

## [weather.py](https://github.com/deepjyoti30/Scripts/blob/master/weather.py)

#### Weather script written in python. Uses openweather api. Prints weather icon too.

```
Usage: python weather.py location

location: Name of the place you want weather info of.
```

## [play_from_yt.sh](https://github.com/deepjyoti30/Scripts/blob/master/play_from_yt.sh)

#### Play video from youtube directly from cli.

Depends on the python file [search_yt.py](https://github.com/deepjyoti30/Scripts/blob/master/search_yt.py) to get URL.

```
Usage: ./play_from_yt 'video_name'

song_name: Name of the video you want to see

Important: Make sure the name is inside inverted commas.
```

## [series_better.py](https://github.com/deepjyoti30/Scripts/blob/master/series_better.py)

#### Just a simple script to keep track of the series that you watch locally.

```
Usage: python series_better.py <path to local series dir>
```