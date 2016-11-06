#!/bin/bash

cd /home/pi/Desktop/piel/scripts

tmux new -s server -d
tmux new -s motors -d

tmux send -t motors.0 'python3 motors.py' ENTER
tmux send -t server.0 'node server.js' ENTER


