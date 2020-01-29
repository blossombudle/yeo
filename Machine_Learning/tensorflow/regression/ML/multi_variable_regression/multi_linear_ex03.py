import numpy as np
import tensorflow as tf
'''
데이터 전처리(Preprocessing)
    - Scale(범위, 규모)를 축소 (0~1로 많이 나타냄)
    - why? 특정 데이터로 인해 w의 영향(튀어 나갈 수 있다)
대표적인 전처리 알고리즘
    MinMaxScaler   : 최대값이 1, 최소 값이 0이 되도록
    StandardScaler : 평균 0과 표준편차가 1이 되도록
    MaxAbsScaler   : 0을 기준으로 절대값이 가장 큰수가 1 or -1이 되도록
'''
'''
MinMaxScaler 구현
    -> 최대 값을 1, 최소 값이 0이 되도록 만들되, 사이의 데이터를 분포처럼
    -> 모든 값이 0~1 범위로 변환
    -> 다음과 같이 데이터들이 존재한다면,
        9,4,3,6,3,1,9
        (1) 최대값과 최소값을 구한다(최대:9, 최소:1)
        (2) 나머지를 백분율을 생각하여 나누기 활용
        (3) (X값 - 최소값) / (최대값 - 최소값) -> 결론 수식
'''

def min_max_sclaer(data):
    return (data-data.min(axis=0))/(data.max(axis=0)-data.min(axis=0))
# X, Y를 모두 한번에 표현 후
data_list = [[9,7,1,12300,2],
             [3,8,4,11200,1],
             [4,5,7,13400,8],
             [6,3,4,14300,1],
             [3,4,2,13700,1],
             [1,1,9,11700,3],
             [9,1,2,12800,7]]

learning_rate=0.1
num_epochs = 200

# Slicing을 통해 X,Y를 분리
xy_data = np.array(data_list)

print('가공전 :\n',xy_data)
xy_data = min_max_sclaer(xy_data)
print('가공후 :\n',xy_data)



x_data = xy_data[:,0:-1]
y_data = xy_data[:,[-1]]

#Multi-Variable
#print(x_data)
#print(y_data)

X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([4,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

H = tf.matmul(X,W)+b

cost = tf.reduce_mean(tf.square(H-Y))
train = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(num_epochs):
        cost_val, pred, _ = sess.run([cost,H,train], feed_dict={X:x_data, Y:y_data})
        print('epoch :', epoch+1,'cost_val :',cost_val)
        print('Prediction :', pred)

