import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
'''
MNIST Database
    - 손 글씨 모음집
    - 머신러닝 시험용으로 많이 활용
'''

#학습 입력 데이터
mnist = input_data.read_data_sets('mnist_data/', one_hot=True)

#파라미터 선언부
learning_rate=0.1 # 학습 주기(W)
num_epochs = 20   # 총 세대수(학습 수)
batch_size = 100  # 학습 묶음 크기, batch:총 데이터에서 100개씩 처리하겠다
total_size = mnist.train.num_examples # 총 데이터 수
num_iterations = int(total_size / batch_size) # 반복 수(100개씩 몇번)
#루프를 위해 정수형으로 변환

#빈 노드 생성
X = tf.placeholder(tf.float32,[None, 784]) # 이미지 파일 28 x 28 = 784
Y = tf.placeholder(tf.float32,[None, 10]) # 0~9

W = tf.Variable(tf.random_normal([784,10]))
b = tf.Variable(tf.random_normal([10]))

#가설 정의
H = tf.nn.softmax(tf.matmul(X,W)+b)

#비용 함수
cost = tf.reduce_mean(-tf.reduce_sum(Y*tf.log(H), axis=1))

#최적화
train = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess:
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

    #예측과 실제값이 같나
    correct_prediction = tf.equal(tf.argmax(H,1), tf.argmax(Y,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print('accuracy :', sess.run(accuracy, feed_dict={X:mnist.test.images, Y:mnist.test.labels}))