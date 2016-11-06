#!/bin/bash

cd /home/pi/Desktop/piel

tmux new -s node_server -d

tmux new -s ros_core -d
tmux new -s ros_py_motors -d
tmux new -s ros_py_commandsocket -d


tmux send -t node_server.0 'node scripts/server.js' ENTER

tmux send -t ros_core.0 'roscore' ENTER

tmux send -t ros_py_motors.0 'source catkin_ws/devel/setup.bash' ENTER
tmux send -t ros_py_motors.0 'rosrun piel scripts/cmotors.py' ENTER

tmux send -t ros_py_commandsocket.0 'source catkin_ws/devel/setup.bash' ENTER
tmux send -t ros_py_commandsocket.0 'rosrun piel scripts/commandsocket.py' ENTER