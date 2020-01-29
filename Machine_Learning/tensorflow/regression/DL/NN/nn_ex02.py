# nn_ex02.py

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
'''
Backpropagation Algorithm
    - 역전파 알고리즘
    - 전파 과정을 통해 w, b를 변화해 가는 과정
        앞에서부터 뒤로 진행하는 형태(Forward Propagation)
        기존 형태와 달리 거꾸로 진행하는 형태(Backward Propagation)
        [] -> [] -> []
        []    []    []
        []    []    []
        [] <- [] <- []
        반대로 w, b가 변화하는 과정을 알아갈 때, sigmoid(0~1) 기반으로 이루어져 있다면,
        0.01 * 0.01 * 0.03... -> 값이 한없이 작아질 수 있다.
        예를들어, Layer가 3개를 거치면서 0.1만 보더라도 처음 값의0.001의 비율을 가진다.
            -> 한없이 작아진 데이터 기반으로, 원본 데이터들 기반의 영향력을 확실히 알 수 없다.
            
        *Vanishing Gradient    
'''

'''
Test Case

TDD(TestDriven Development)
    - 테스트 주도 개발 방법
    
    1. 시험 코드 작성
    Sum(3,7)
    Sum(3,7,11)
    Sum(0.1,0.2)
    
    2. 함수 정의 (기능 정의)
    def Sum(a,b):
        #do something...
        
    3. 시험 코드가 원하는 결과 (실제 결과)에,
       맞도록 함수 구현 후 테스트 반복
'''

#여러 모델을 정의하여 모델간 성능을 비교시에[ seed값 설정
tf.set_random_seed(1000)

mnist = input_data.read_data_sets("../mnist_data/", one_hot=True)

learning_rate=0.001
num_epochs = 15
batch_size = 100

X = tf.placeholder(tf.float32,[None, 784])
Y = tf.placeholder(tf.float32,[None, 10])

W = tf.Variable(tf.random_normal([784,256]))
b = tf.Variable(tf.random_normal([256]))
L = tf.nn.relu(tf.matmul(X,W)+b)

W1 = tf.Variable(tf.random_normal([256,256]))
b1 = tf.Variable(tf.random_normal([256]))
L1 = tf.nn.relu(tf.matmul(L,W1)+b1)

W2 = tf.Variable(tf.random_normal([256,256]))
b2 = tf.Variable(tf.random_normal([256]))
L2 = tf.nn.relu(tf.matmul(L1,W2)+b2)

W3 = tf.Variable(tf.random_normal([256,10]))
b3 = tf.Variable(tf.random_normal([10]))
H = tf.matmul(L2,W3)+b3

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=H, labels=Y))
train = tf.train.AdadeltaOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(num_epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples / batch_size)

        for batch in range(total_batch):
            x_data, y_data = mnist.train.next_batch(batch_size)
            cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data})
            avg_cost += cost_val / total_batch

        print('epoch :', num_epochs+1, 'cost :', avg_cost)

    prediction = tf.equal(tf.argmax(H,1), tf.argmax(Y,1))
    accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))
    print('accuracy :', sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels}))

