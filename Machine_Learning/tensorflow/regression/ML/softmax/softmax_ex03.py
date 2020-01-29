import tensorflow as tf

x_data = [[1, 2, 7],
          [8, 2, 6],
          [6, 2, 1],
          [1, 2, 2],
          [5, 8, 1],
          [2, 1, 5],
          [4, 2, 3],
          [3, 2, 1]
          ]

y_data = [[0, 1, 0], # 2
          [0, 0, 1], # 2
          [0, 1, 0], # 2
          [1, 0, 0], # 1
          [0, 0, 1], # 1
          [0, 1, 0], # 1
          [0, 1, 0], # 0
          [1, 0, 0]  # 0
          ]


#빈노드 생성
X = tf.placeholder(tf.float32, shape=[None, 3])
Y = tf.placeholder(tf.float32, shape=[None, 3])

#가설 함수 정의를 위한 W,b(초기값)
W = tf.Variable(tf.random_normal([3,3]), name='weight')
b = tf.Variable(tf.random_normal([3]), name ='bias')

#가설 함수 정의
H = tf.nn.softmax(tf.matmul(X,W)+b)

#비용 함수 정의
cost = tf.reduce_mean(-tf.reduce_sum(Y*tf.log(H), axis=1))

#학습 주기
learning_rate = 0.1

#예측 알고리즘
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

prediction = tf.argmax(H,1)
accuracy = tf.reduce_mean(tf.cast(tf.equal(prediction, tf.argmax(Y,1)), dtype=tf.float32))
'''
[학습 추적 정보 출력]
각 학습 별 비용, 기울기를 출력하고, 학습 후 예측 정보와, 정확도를 출력하세요.
'''

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(301):
        cost_val, w_val = sess.run([cost, W, optimizer], feed_dict={X:x_data, Y:y_data})
        print('step :', step, 'cost :',cost_val, 'weigh :',w_val)

    print('Prediction :', sess.run(prediction, feed_dict={X:x_data}))
    print('Accuracy :', sess.run(accuracy, feed_dict={X:x_data, Y:y_data}))

    a = sess.run(H, feed_dict={X:[[1,1,2]]})
    print(a, sess.run(tf.argmax(a,1)))

    b = sess.run(H, feed_dict={X:[[4,4,6]]})
    print(b, sess.run(tf.argmax(b,1)))

    c = sess.run(H, feed_dict={X:[[2,5,5]]})
    print(c, sess.run(tf.argmax(c,1)))

    d = sess.run(H, feed_dict={X:[[1,5,5]]})
    print(d, sess.run(tf.argmax(d,1)))

