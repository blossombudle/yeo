import tensorflow as tf

x_data = [[50, 49, 30, 70],
          [25, 40, 80, 20],
          [60, 20, 70, 60],
          [100, 90, 40, 50],
          [50, 80, 15, 35],
          [50, 100, 56, 85],
          [40, 20, 30, 70],
          [70, 80, 60, 50]
          ]

y_data = [[0, 1] if sum(x) >= 200 else [1, 0] for x in x_data]

'''
Classification(분류)
    -> 0과 1(Binary) 형태가 아닌 0,1,2 세가지 분류
    -> 세가지 이상 그룹처럼 나누는 것이 목적
    이진형식의 분류 방법으로도 나눌수는 있다.

    H(x) : W * x
                      [[x1]
    [[w1] [w2] [w3]] * [x2] = H(x)
                       [x3]]
    -> 이와 같이 H(x)가 여러 개일 경우!

softmax(...)
    데이터가 많으면 그 만큼의 Logistic(Sigmoid)이 필요
    H = W * x = y 형태에서, 가설 함수의 결과(y)의 데이터가 하나가 아닌 여러개(1차원, 벡터)로 반환 

    각각의 데이터의 확률을 구하겠다.(목적)

    softmax(...)의 역할
        - n개의 데이터를 예측하고자 할 때 활용
        - 분류하고 싶은 데이터 개수만큼 확률로 변환
        - 확률 총합이 1이 되도록 결과를 반환

    만약 결과가 다음과 같다면,
    [0.2,0.2,0.6] -> [0.0,0.0,1.0]로 변환
    확률 제일 높은 0.6을 1.0으로 표현하는 방법
'''
tf.set_random_seed(1000)
X = tf.placeholder(tf.float32, shape=[None, 4], name="X")
Y = tf.placeholder(tf.float32, shape=[None, 2], name="Y")

W = tf.Variable(tf.random_normal([4,2]), name='weight')
b = tf.Variable(tf.random_normal([2]), name ='bias')

H = tf.nn.softmax(tf.matmul(X,W)+b)

cost = tf.reduce_mean(-tf.reduce_sum(Y*tf.log(H), axis=1))


optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(cost)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(5001):
        _, cost_val = sess.run([optimizer, cost], feed_dict={X:x_data, Y:y_data})

        if step % 50 == 0:
            print('step :', step, 'cost_val :', cost_val)

    a = sess.run(H, feed_dict={X:[[50,60,70,50]]})
    print(a, sess.run(tf.argmax(a,1)))

    b = sess.run(H, feed_dict={X:[[40,20,30,50]]})
    print(b, sess.run(tf.argmax(b,1)))

    c = sess.run(H, feed_dict={X:[[60,70,20,60]]})
    print(c, sess.run(tf.argmax(c,1)))

    d = sess.run(H, feed_dict={X:[[30,55,30,70]]})
    print(d, sess.run(tf.argmax(d,1)))

