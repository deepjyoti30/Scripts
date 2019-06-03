#!/bin/sh

# The querry must be passed by the user
Querry=$1

echo "Getting the URL for: $Querry"

# Get the URL using the python script
URL=$(python ~/Python/search_yt.py $Querry)

echo "URL fetched."

# Play using mpv
mpv $URL