#경사도 하강 알고리즘

import tensorflow as tf
import matplotlib.pyplot as plt

x = [1,2,3]
y = [1,2,3]

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
W = tf.Variable(tf.random_normal([1]))
b = tf.Variable(tf.zeros([1]))
#가설
hypothesis = X*W+b
#비용함수
cost = tf.reduce_mean(tf.square(hypothesis-Y))

learning_rate=0.1
gradient = tf.reduce_mean((W*x-y)*x)
descent = W - learning_rate*gradient
update = W.assign(descent)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

w_list = []
cost_list = []

for step in range(30+1):
    sess.run(update, feed_dict={X : x, Y : y})
    print('step :', step, end=', ')
    print('cost :', sess.run(cost, feed_dict={X:x, Y:y}), end=', ')
    print('weight :', sess.run(W))