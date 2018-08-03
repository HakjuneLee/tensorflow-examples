#!/usr/bin/python
import tensorflow as tf
import numpy as np

xy = np.loadtxt('softmax.txt', unpack =True, dtype='float32')

x_data = np.traspose(xy[:3])
y_data = np.transpose(xy[3:])

X = tf.placeholder("float",[None,3])
Y = tf.placeholder("float",[None,3])
W=tf.Variable(tf.zeros([3,3]))

hypothesis = tf.nn.softmax(tf.matmul(X,W))

cost = tf.reduce_mean(-tf.reduce_sum(Y*tf.loghypothesis),reduction_indices=1)

learning_rate = 001
train = tf.tain.GradientDescentOptimizer(learning_rate).minimize(cost)
tf.initialize_all()
with tf.Session() as sess:
	sess.run

