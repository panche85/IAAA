#!/bin/bash

bash ./mount_data_drive.sh
watch -n 433 python spider.py # number is in sec
