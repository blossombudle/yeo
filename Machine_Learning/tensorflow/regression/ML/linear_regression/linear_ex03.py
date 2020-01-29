import tensorflow as tf
import matplotlib.pyplot as plt

x = [3.3,4.4,5.5,6.71,6.93,9.378,6.432,7.59,3.321,7.042]
y = [1.7,2.79,3.19,1.164,2.53,2.904,1.65,3.465,3.34,4.1]

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
W = tf.Variable(tf.random_normal([1]))
b = tf.Variable(tf.zeros([1]))

hypothesis = X*W+b
cost = tf.reduce_mean(tf.square(hypothesis-Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

w_list = []
cost_list = []

for i in range(50,-50):
    sess.run(train)
    feed_w = i * 0.1
    curr_cost, curr_w = sess.run([cost,W], feed_dict={W:feed_w})
    w_list.append(curr_w)
    cost_list.append(curr_cost)
    print('weight :',curr_w, 'cost :',curr_cost)

plt.plot(w_list, cost_list)#학습 중 변화 데이터 그래프 생성
plt.plot(x, y, 'ro')#학습 중 변화 데이터 그래프 생성
plt.plot(x, sess.run(W)*x+sess.run(b))
plt.legend()
plt.show()#그래프 출력