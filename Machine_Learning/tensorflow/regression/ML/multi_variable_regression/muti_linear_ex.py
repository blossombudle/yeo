#multi_linear_ex01.py
#   multi-variable Linear Regression
#   처음 선형 회귀를 기반으로 여러변서 x가 많은 경우

import tensorflow as tf

x1_data = [73., 93., 88., 94., 77.]
x2_data = [80., 88., 91., 96., 66.]
x3_data = [75., 93., 90., 99., 70.]

y_data = [152., 177., 185., 194., 166.]

#빈 노드 생성
x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

#임이의 기울기 정의
w1 = tf.Variable(tf.random_normal([1]), name='weight')
w2 = tf.Variable(tf.random_normal([1]), name='weight2')
w3 = tf.Variable(tf.random_normal([1]), name='weight3')
b = tf.Variable(tf.random_normal([1]), name='bias')

#가설정의
H = w1*x1 + w2*x2 + w3*x3 + b

#비용함수
cost = tf.reduce_mean(tf.square(H - y))

#알고리즘과 최소화
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, pred_val, _ = sess.run([cost, H, train],
                                     feed_dict={x1:x1_data, x2:x2_data, x3:x3_data, y:y_data})

    if step % 10 == 0:
        print('step :', step, end=', ')
        print('cost :', cost_val, end=', ')
        print('prediction :', pred_val)

