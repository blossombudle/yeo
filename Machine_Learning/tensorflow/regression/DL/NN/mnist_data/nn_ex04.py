import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

'''
다수의 레이어 존재 시(xor 형태 처럼) 정확히 분류하지말고 어느정도의 오차를 허용.
정확히 분류하고자 할 시, 비선형이 너무 복잡해진다.
    -> 학습 후 결과는 잘 동작하는 것처럼 보일 수 있다.
    -> 아닐 수도 있다.(Overfitting)
    
Overfitting Model 동작시 Layer 분류의 한계점이 존재
    -> 실제 입력 데이터는 정확도가 높겠지만,
       시험입력 데이터는 정확도가 낮을 수 있다.
       
       해결 예시 방법
       1. 더 많은 학습 데이터
       2. 특성 경우의 수를 축소
       3. weight 값 제한(너무 크지 않도록)
Dropout(낙오, 탈락)
    - 모든 weight를 계산하지 않고, 일부분만 연산에 포함시키는 방법
    - 
'''


mnist = input_data.read_data_sets("../mnist_data/", one_hot=True)

learning_rate=0.001
num_epochs = 15
batch_size = 100

X = tf.placeholder(tf.float32,[None, 784])
Y = tf.placeholder(tf.float32,[None, 10])
keep_prob = tf.placeholder(tf.float32)

init = tf.contrib.layers.xavier_initializer()
W1 = tf.Variable(init([784, 256]))
b1 = tf.Variable(tf.random_normal([256]))
L1 = tf.nn.relu(tf.matmul(X,W1)+b1)
L1 = tf.nn.dropout(L1, keep_prob=keep_prob)
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
L2 = tf.nn.dropout(L2, keep_prob=keep_prob)

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
            cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data, keep_prob: 0.7})
            #keep_prob : Dropout 비율(0~1, 0.7은 70% 활용)
            avg_cost += cost_val / total_batch

        print('epoch :', i+1, 'cost :', avg_cost)

    prediction = tf.equal(tf.argmax(H,1), tf.argmax(Y,1))
    accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))
    print('accuracy :', sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels,
                                                      keep_prob: 1}))
