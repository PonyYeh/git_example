# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 12:57:43 2018

@author: ting
"""

import tensorflow as tf

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print(sess)

#hello tingens