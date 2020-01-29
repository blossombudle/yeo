import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

'''
Neural Networks(NN)
'''

#학습 입력 데이터
mnist = input_data.read_data_sets('mnist_data/', one_hot=True)

#파라미터 선언부
learning_rate=0.1 # 학습 주기(W)
num_epochs = 20   # 총 세대수(학습 수)
batch_size = 100  # 학습 묶음 크기, batch:총 데이터에서 100개씩 처리하겠다
total_size = mnist.train.num_examples # 총 데이터 수
num_iterations = int(total_size / batch_size) # 반복 수(100개씩 몇번)


X = tf.placeholder(tf.float32,[None, 784]) # 이미지 파일 28 x 28 = 784
Y = tf.placeholder(tf.float32,[None, 10]) # 0~9

W = tf.Variable(tf.random_normal([784,10]))
b = tf.Variable(tf.random_normal([10]))
extra = tf.Variable(tf.random_normal([10,10]))

with tf.name_scope('for'):
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(1,500):
            if i == 1:
                c = tf.sigmoid(tf.matmul(X, W) + b)
            c = tf.sigmoid(tf.matmul(c, extra) + b)

    tf.summary.histogram('W', W)
    tf.summary.histogram('b', b)
    tf.summary.histogram('H', c)

H = c
cost = tf.reduce_mean(-tf.reduce_sum(Y*tf.log(H), axis=1))
#최적화
train = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

'''
Cross Entry -> softmax 
logits      -> Hypothesis
'''
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=H, labels=Y))
train = tf.train.AdadeltaOptimizer(learning_rate).minimize(cost)
'''
Optimizer
    (1)
    Gradient Descent(GD) : 전체 데이터 기반
    Stochastic Gradient Descent(GSD) : 전체 데이터를 부분적으로 나누어 연산
        공통 단점 -> 극소 값을 찾은 뒤 더이상 학습 진행이 안된다.
    (2)
    Momentum : 관성 개념을 도입하여 보완한 알고리즘
    NAG : 관성 방향으로 움직인 뒤 계산된 방향을 찾아가는 알고리즘
    Nadam : NAG와 RMSProp 두가지를 합한 알고리즘
    Adam : Momentum과 Learnig Rate 개선을 위한 RMSProp 두가지를 합한 알고리즘
    
Learning Rate
    -> 단순히 특정 값 기준으로 딱딱하게 변화하는 것을 보완한 알고리즘들
Adagard : 처음에는 빠르게, 나중엔 느리게(세밀하게)
RMSProp : 세밀하게 변화하되, 데이터 특성을 고려하여 조정(기울기 값이 올라가는 경우)
AdaDelta : 너무 세밀하다면 학습이 안되는 경우를 방지
'''

with tf.Session() as sess:
    merge_summary = tf.summary.merge_all()
    file_writer = tf.summary.FileWriter('./logs/xor_ex04_log')
    file_writer.add_graph(sess.graph)

    sess.run(tf.global_variables_initializer())

    for epoch in range(num_epochs):
        cost_avg = 0
        for i in range(num_iterations):
            #100개씩 뽑아 학습데이터를 넣어주겠다
            x_data, y_data = mnist.train.next_batch(batch_size)
            _, cost_val = sess.run([train, cost], feed_dict={X:x_data, Y:y_data})
            cost_avg += cost_val / num_iterations #데이터 평균 : 코스트 550번 값을 구해서 더한 후 550으로 나누어서 평균을 만듬

        print('epoch :', epoch + 1, 'cost_val :', cost_avg)
    '''
    Test Data
    {X : mnist.test.images,
     Y : mnist.test.labels}
    '''
    correct_prediction = tf.equal(tf.argmax(H,1), tf.argmax(Y,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print('accuracy :', sess.run(accuracy, feed_dict={X:mnist.test.images, Y:mnist.test.labels}))