#!/usr/bin/env python
# coding: utf-8

import sys
import rospy
import time
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sensor_msgs.msg import JointState
from kortex_driver.srv import *
from kortex_driver.msg import *

labels = ['j1','j2','j3','j4','j5','j6']
x = np.arange(len(labels))
width = 0.7
effort_ = [0,0,0,0,0,0]
fig, ax = plt.subplots(figsize=(10,10))
def callback(data):
    global effort_
    effort_ = list(data.effort[:6])
    print(list(data.effort))


def graph():
    plt.cla()
    a = np.array([9, 9, 9, 9, 9, 9])
    per = np.abs(effort_)
    per = per / a * 100
    
    rect = ax.bar(x, per, width)
    
    ax.set_xticks(x)
    ax.set_ylim(0,200)
    #ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1))
    ax.set_xticklabels(labels)
    ax.set_ylabel('%(Nm)', fontsize=21)
    plt.rcParams["font.size"] = 21
    plt.draw()
    plt.pause(0.05)

def listener():
    rospy.init_node('getter', anonymous=False)
    rospy.Subscriber("/my_gen3_lite/joint_states", JointState, callback)
    while not rospy.is_shutdown():
        graph()
    rospy.spin()

if __name__ == '__main__':
    listener()
