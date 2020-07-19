#!/bin/bash
sudo apt-get update
sudo apt-get install build-essential -y
sudo apt-get install python3
sudo apt-get install python3-pip -y
sudo apt-get install python3-venv -y
cd /home/ubuntu
sudo pip3 install --upgrade pip
. venv/bin/activate
cd aws-music
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py runserver 0:80