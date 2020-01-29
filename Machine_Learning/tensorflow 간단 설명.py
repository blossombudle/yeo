import tensorflow as tf
x_Data = [1, 2, 3, 4, 5, 6, 7]
y_Data = [25000, 55000, 75000, 110000, 128000, 155000, 180000]
w = tf.Variable(tf.random_uniform([1], -100, 100))
b = tf.Variable(tf.random_uniform([1], -100, 100))#랜덤값을 생성할 수 있게 해줌
x = tf.placeholder(tf.float32)#placeholder 임의의 값을 받을 수 있게 해줌
y = tf.placeholder(tf.float32)
h = w*x+b
cost = tf.reduce_mean(tf.square(h-y))#square 제곱, reduce_mean 시그마?
a = tf.Variable(0.01)
optimizer = tf.train.GradientDescentOptimizer(a)#경사하강법
train = optimizer.minimize(cost)#cost 최소화
init = tf.global_variables_initializer()#tf.variable에 선언된 변수값들을 초기화
sess = tf.Session()
sess.run(init)
for i in range(2501):
    sess.run(train, feed_dict={x: x_Data, y: y_Data})
    if i % 500 == 0:
        print(i, sess.run(cost, feed_dict={x: x_Data, y: y_Data}), sess.run(w), sess.run(b))
print(sess.run(h, feed_dict={x: [8]}))
sess.close()
tf.softmax.cross.entroppy