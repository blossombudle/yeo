import tensorflow as tf
'''
classification - 분류(Binary)
    - 정해진 두 종류로 분류하는 방법(0 or 1)
    - 특정 유저에게 보여줄 것인가 안보여 줄 것인가
    -넷플릭스에서 유저가 많이 본 영화(데이터)를 기반으로,
    추천 목록에 show/hide 수행!
    
    기준 선형 회귀 기준으로 분류를 한다면,
    특정 점수 기반으로 pass / non-pass를 구분할 수 있지만,
    어떠한 값이 특출나게 높으면 값이 달라진다.
    이는 기존의 pass 데이터가 non-pass 범주로 들어가게 된다.

[목적]
H = W*x+b 예측 모델을 0~1 범위 정도로 압축

Logistic function, Sigmoid function(S자형 곡선)
-> 기존 Hypothesis 모델을 한번 더 가공하여, 0~1로 표현
z = Hypothesis 모델
g(z) = 1 / (1+e^-z) 수식을 활용하여 압축
단순히 가설 함수가 다른 형태로 바뀐 것 뿐
실제 y 값들을 0~1사이로 한번 더 가공 한 것 뿐

cost function : 기존걸로 표현하면 학습이 힘들다
새로운 비용 함수 정의!
    -> y의 범위 0~1
c(H(x),y) -> -log(H(x))   : y = 1
          -> -log(1-H(x)) : y = 0

y가 1일 경우
H(x) = 1 (1일 경우)-> 비용이 0에 가깝다.    (o)
H(x) = 0 (0일 경우)-> 비용이 무한에 가깝다.  (x)

y가 0일 경우
H(x) = 1 (1일 경우)-> 비용이 무한에 가깝다.  (o)
H(x) = 0 (0일 경우)-> 비용이 0에 가깝다.     (x)

그렇다면 비용함수가 2가지 경우이니 함수가 2개?
c(H(x), y) = -y log(H(x)) - (1-y) log(1-H(x))

[함수 흐름]
x -> H -> z -> g(x)
'''

x_data = [[1,2],
          [2,3],
          [3,1],
          [4,3],
          [5,3],
          [6,2]]
y_data = [[0],
          [0],
          [0],
          [1],
          [1],
          [1]]

#빈 노드 생성
X = tf.placeholder(tf.float32, shape=[None,2])
Y = tf.placeholder(tf.float32, shape=[None,1])

# Weight, bias
#   ->가설(임의의 직선을 긋기 위해)
W = tf.Variable(tf.random_normal([2,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='weight')

#가설정의
#   H = tf.matmul(X,W) + b 기존 가설
#   새로운 가설 함수로 가공!
H = tf.sigmoid(tf.matmul(X,W) + b)

#비용 함수
#c(H(x), y) = -y log(H(x)) - (1-y) log(1-H(x))
cost = -tf.reduce_mean(Y * tf.log(H) + (1-Y)*tf.log(1-H))

#경사 하강 알고리즘
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

#ft.cast(...) : 데이터 타입 변환.
#예측 결과의 데이터가 0.5보다 크다면 1, 작다면 0.
prediction = tf.cast(H > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(prediction, Y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(20001):
        cost_val, _ = sess.run([cost, train], feed_dict={X:x_data, Y:y_data})

        #if step % 50 ==0:
        #    print('step :', step, 'cost :', cost_val)

    #학습 종료
    h, p, a = sess.run([H, prediction, accuracy], feed_dict={X:x_data, Y:y_data})
    print('Hypothesis :', h)
    print('Prediction :', p)
    print('Accuracy :', a)