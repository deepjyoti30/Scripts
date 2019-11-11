#!/usr/bin/sh
# Script to mount my devices.

function scold() {
    echo "+--+ +    |   | |----  --+-- --+--  --+-- |\  |  |"
    echo "|__| |    |   | |---+    |     |      |   | \ |  |"
    echo "|    |___ |___| |___|  --+--   |    --+-- |  \|  0" 
}

DES=$1

if [ -z $1 ]
then
    printf "\nUsage: mt <location>\n"
    exit
fi

if [ "$DES" == "Old" ]
then
    point="/dev/$(lsblk | grep "part" | grep "80G" | grep 'sd[a-z][1-9]' -o)"

    if [ $point == "/dev/" ]; then
        scold
        exit
    fi

    echo "Mounting $point to ~/Old"
    mkdir -p ~/Old
    sudo mount $point ~/Old
elif [ "$DES" == "HDD" ]
then
    point="/dev/$(lsblk | grep "part" | grep "1.8T" | grep 'sd[a-z][1-9]' -o)"
    
    if [ $point == "/dev/" ]; then
        scold
        exit
    fi

    echo "Mounting $point to ~/HDD"
    mkdir -p ~/HDD
    sudo mount $point ~/HDD
elif [ "$DES" == "USB" ]
then
    point="/dev/$(lsblk | grep "part" | grep "7.2G" | grep 'sd[a-z][1-9]' -o)"

    if [ $point == "/dev/" ]; then
        scold
        exit
    fi

    echo "Mounting $point to ~/USB"
    mkdir -p ~/USB
    sudo mount $point ~/USB
fi
