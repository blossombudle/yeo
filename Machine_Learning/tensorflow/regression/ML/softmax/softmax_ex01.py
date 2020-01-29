import tensorflow as tf

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

#x[0]의 데이터가 들어가 y[0]의 값이 나온다
x_data = [[1, 2, 7, 1],
          [8, 2, 6, 2],
          [6, 2, 1, 6],
          [1, 9, 2, 1],
          [5, 8, 1, 3],
          [2, 1, 5, 8],
          [4, 2, 3, 7],
          [3, 2, 1, 4]
          ]

#그룹을 총 3가지 (0,1,2)로 나누고자 할 때,
y_data = [[1, 0, 0], # 2
          [1, 0, 0], # 2
          [0, 1, 0], # 2
          [0, 0, 1], # 1
          [1, 0, 0], # 1
          [0, 1, 0], # 1
          [1, 0, 0], # 0
          [0, 0, 1]  # 0
          ]
'''
y_data 데이터의 데이터 형식 개수가 3개
예측 직선의 결과로 나올 수 있는 경우의 수가 3개
'''
X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 3])

W = tf.Variable(tf.random_normal([4,3]), name='weight')
b = tf.Variable(tf.random_normal([3]), name ='bias')

H = tf.nn.softmax(tf.matmul(X,W)+b)

'''
H = tf.matmul(X,W) + b -> Multi Variable(Linear)
H = sigmoid(tf.matmul(X,W) + b) -> logistic
H = softmax(tf.matmul(X,W) + b) -> softmax(Multi Logistic)
    ->확률 결과의 총 합이 1.0이 되도록
      
    일반적인 Y의 결과 -> 확률로서 나타내겠다
    1.0                 0.2
    2.5                 0.7
    0.5                 0.1
    즉, softmax는 Logistic을 포함하는 개념(Sigmoid)
    
    확률 데이터 -> One - hot encoding(가장 높은것을 1로)
    0.2            0
    0.7            1.0
    0.1            0
    
'''
cost = tf.reduce_mean(-tf.reduce_sum(Y*tf.log(H), axis=1))
'''
이전까지 알고 있던 Logistic Cost function
    c(H(x), y) = -y log(H(x)) - (1-y) log(1-H(x))
               = -(y*log(H(x)) - (1-y) log(1-H(x)))
softmax도 logistic 개념 포함하는데 , 기존과 다른 수식 활용
    -tf.reduce_sum(Y*tf.log(H)) -> 같은 수식!
    
'''

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(2001):
        a, cost_val = sess.run([optimizer, cost], feed_dict={X:x_data, Y:y_data})

        if step % 50 == 0:
            print('step :', 'cost_val :', cost_val)
    '''
    학습을 종료 후야ㅔ 임시 데이터를 넣어 결과 그룹을 출력
    tf.argmax()
       -> 확률이 가장 높은 값의 인덱스 값 반환
       -> [0.2,0.2,0.6] 데이터의 결과는 2
    Hypothesis의 결과 값 -> softmax의 결과인 확률 데이터
    
    '''
    a = sess.run(H, feed_dict={X:[[1,1,2,2]]})
    print(a, sess.run(tf.argmax(a,1)))

    b = sess.run(H, feed_dict={X:[[4,2,2,7]]})
    print(b, sess.run(tf.argmax(b,1)))

    c = sess.run(H, feed_dict={X:[[2,5,5,8]]})
    print(c, sess.run(tf.argmax(c,1)))

    d = sess.run(H, feed_dict={X:[[1,5,5,2]]})
    print(d, sess.run(tf.argmax(d,1)))