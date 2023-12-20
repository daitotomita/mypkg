# SPDX-FileCopyrightText: 2023 Daito Tomita s22C1090CW@s.chibakoudai.jp
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
     global node
     f=0
     for i in range(1, msg.data+1):
        if msg.data%i==0:
            f+=1
     if f==2:
         node.get_logger().info("Listen: %d 素数" % msg.data)
     elif msg.data==51:
         node.get_logger().info("Listen: %d グロタンディーク素数" % msg.data)
     else:
         node.get_logger().info("Listen: %d 合成数" % msg.data)
        
rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)
