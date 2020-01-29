import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

'''
데이터 가공 및 학습(ML, DL)에서 가장 중ㅇ요한 및 전처리
 H = Wx + b
     1. x(input data = 입력데이터) 초기화
     2. H(Hypothesis)에 대한 처리방법
     2. W(weight)의 초기화
    +@ Optimizer 선택
    
Weight에 난수 초기화는 어떤 값이냐에 따라 매번 달라진다.
    -> 성능에까지 영향을 미찬다.
    -> 단, 0으로 초기화 시 X가 0(Layer 무효, 최초 H가 이상하니까)
    
Pre-Trainig(Processing, Tuning) : W를 초기화 하기 위한 학습 중의 작업

RBM(Restricted Boltzman Machine) : 최초 weight 초기화 방법
    - 두 레이어 사이에서 동작
    - 흐름
        1. A 레이이서  x값에 대한 w를 계산 후 , 다음 레이어에 전달(Forward)
        2. b 레이어는 전달 받은 값을 계산 후, 반대로 A 레이어에 전잘(Backward)
            -> 두 과정을 반복, 최초 x와 예측한 값의 최소가 되는 W를 찾겠다!

xavier : 입력 값과 출력 값 사이의 난수를 선택해 입력 값의 제곱근으로 나누는 형태 
    각 레이어별로 입력 값(X), 출력 값(Y)을 가지고 W를 추론!
'''

#tf.set_random_seed(1000)

mnist = input_data.read_data_sets("../mnist_data/", one_hot=True)

learning_rate=0.001
num_epochs = 15
batch_size = 100

X = tf.placeholder(tf.float32,[None, 784])
Y = tf.placeholder(tf.float32,[None, 10])

init = tf.contrib.layers.xavier_initializer()
W1 = tf.Variable(init([784, 256]))
b1 = tf.Variable(tf.random_normal([256]))
L1 = tf.nn.relu(tf.matmul(X,W1)+b1)
'''
W1 = tf.get_variable('W1', shape = [784,256],
                     initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([256]))
L1 = tf.nn.relu(tf.matmul(X,W1)+b1)
'''

W2 = tf.get_variable('W2', shape = [256,256],
                     initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([256]))
L2 = tf.nn.relu(tf.matmul(L1,W2)+b2)

W3 = tf.get_variable('W3', shape = [256,10],
                     initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([10]))
H = tf.matmul(L2,W3)+b3

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=H, labels=Y))
train = tf.train.AdamOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(num_epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples / batch_size)

        for batch in range(total_batch):
            x_data, y_data = mnist.train.next_batch(batch_size)
            cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data})
            avg_cost += cost_val / total_batch

        print('epoch :', i+1, 'cost :', avg_cost)

    prediction = tf.equal(tf.argmax(H,1), tf.argmax(Y,1))
    accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))
    print('accuracy :', sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels}))
