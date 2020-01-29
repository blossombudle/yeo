#multi_linear_ex01.py
#   multi-variable Linear Regression
#   처음 선형 회귀를 기반으로 여러변서 x가 많은 경우

import tensorflow as tf

#x1_data = [73., 93., 88., 94., 77.]
#x2_data = [80., 88., 91., 96., 66.]
#x3_data = [75., 93., 90., 99., 70.]
x_data = [[73., 93., 88.],
          [89., 94., 77.],
          [80., 88., 91.],
          [75., 93., 90.],
          [73., 65., 70.]
          ]

y_data = [[152.],
          [177.],
          [185.],
          [194.],
          [166.]]

'''
행렬 곱을 활용하기 위해 각각의 기반 데이터를 matrix 형태로
'''

#빈 노드 생성
x = tf.placeholder(tf.float32, shape=[None,3])
y = tf.placeholder(tf.float32, shape=[None,1])

#임이의 기울기 정의
W = tf.Variable(tf.random_normal([3,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#가설정의
H = tf.matmul(x,W)+b

#비용함수
cost = tf.reduce_mean(tf.square(H - y))

#알고리즘과 최소화
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, pred_val, _ = sess.run([cost, H, train],
                                     feed_dict={x:x_data, y:y_data})

    if step % 10 == 0:
        print('step :', step, end=', ')
        print('cost :', cost_val, end=', ')
        print('prediction :', pred_val)

