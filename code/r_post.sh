#!/bin/bash

# This script is executed every day at 7:30 AM.
# note: Ako sakas da go smenis ova treba so comanda "crontab -e".

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" # Get the location of the script

cd $DIR
sudo python daily_back_up.py
