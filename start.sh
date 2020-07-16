#!/bin/bash
sudo apt-get update
sudo apt-get install build-essential -y
sudo apt-get install python3
sudo apt-get install python3-pip -y
sudo apt-get install python3-venv -y
cd /home/ubuntu
git clone https://github.com/eneun/aws-music.git
sudo pip3 install --upgrade pip
python3 -m venv venv
. venv/bin/activate
cd aws-music
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py runserver 0:8000