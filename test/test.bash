#!/bin/bash
# SPDX-FileCopyrightText: 2023 Daito Tomita <s22C1090CW@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source $dir/.bashrc

timeout 7 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Listen: 7 素数'
