#!/usr/bin/python
import tensorflow as tf
state = tf.Variable(0)
init_op = tf.initialize_all_variables()
with tf.Session() as sess:
	sess.run(init_op)
	print(sess.run(state))
