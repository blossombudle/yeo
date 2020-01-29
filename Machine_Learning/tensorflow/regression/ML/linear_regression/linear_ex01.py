#Linear Regression
import tensorflow as tf
'''
Linear Regression(선형회귀)
    - 데어터의 분포를 활용하는 머신러닝 알고리즘
    - 예측을 위한 특정 수식을 추출! (수학적 함수)
    - x축과 y기반의 그래프를 생각
    
    y = x+4라는 수학적 함수가 추출되었따면,
    이 함수를 통해 예측(Prediction) 가능!
    -> x값이 3이라면, y값은 7이다.
    
    Hypothesis(가설)
            - 데이터들을 표현할 수 있는 직선(Linear)이 존재한다.
            - 직선이란 1차 방정식으로 나타낼 수 있는 수학적 개념
            - H(x) = W*x+b(1차원 함수)
            
    Cost function(Loss function)
        -Linear Regression에 활용되는 함수를 이용하여,
        weight, bias 값이 학습 데이터를 얼마나 표현하는지 검증!(계량)
        - 가설(H)로 표현되는 데이터가 실제 데이터의 값이 얼마나 다른지
'''

#Input Data
x = tf.placeholder(tf.float32, shape=[None])
y = tf.placeholder(tf.float32, shape=[None])

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
'''
    cost function에서 궁극적으로 찾고자하는 weight, bias의 초기 값 설정
        ->랜덤으로 설정,[1] 랜덤 수 하나!
'''

#Hypothesis(가설 정의)
H = W * x + b
#Reduce Mean
difference = H-y # 가설과 실제 데이터 직선과의 차이를 계산(거리)
cost = tf.reduce_mean(tf.square(difference))
'''
difference : 가설에서 y 좌표 값의 차이, 단순거리(distance)
tf.square(...) : 거리 차이 값이 음수나 양수이기에 제곱 수행
'''
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

data = {x:[1.0,2.0,3.0,4.0], y:[1.1,2.1,3.1,4.1]}

for step in range(2000 + 1):
    cost_val, weight, bias,_ = sess.run([cost,W,b,train], feed_dict=data)

    #학습정보 출력
    if step % 50 == 0:
        print('step : ', step, end=', ')
        print('cost_val :', cost_val, end=', ')
        print('weight : ', weight, end=', ')
        print('bias : ', bias)