import tensorflow as tf

'''
딥러닝(Deep Learning)
    Netral Networks               신경망
    Convolutional Neural Networks (CNN, 심층 신경망)
    Recurrent Neural Networks     (RNN, 순환 신경망)
    
    기존의 Logistic Regression의 문제(xor_ex01.py)
        -> 두개의 데이터 분류는 문제가 없다.(둘중 하나로 선택)
        -> 이를, 3개의 선을 긋는 방법으로 해결(NN)
    
    CNN(Convolutational Neural Networks)
        - MNIST(이미지 데이터)
        - 특정 이미지를 봤을 때, 일부의 신경만이 동작
        - 1번 그림을 인식하는 것이 A 뉴런이 일을 한다면,
          2번 그림을 인식하는 것은 다른 B 뉴런이 일을 한다.
        - 부분 부분을 잘라내 여러 레이어를 구성하고, 이를 나중에 병합하여 결과를 도출하겠다.
        
'''


x_data = [[0,0],[0,1],[1,0],[1,1]]
y_data = [[0],[1],[1],[1]] #case or
#y_data = [[0],[0],[0],[1]] #case and
#y_data = [[0],[1],[1],[0]] #case xor

X = tf.placeholder(tf.float32,[None,2])
Y = tf.placeholder(tf.float32,[None,1])

W1 = tf.Variable(tf.random_normal([2,2]), name='weight')
b1 = tf.Variable(tf.random_normal([2]), name='bias')
layer = tf.sigmoid(tf.matmul(X,W1) + b1)

W2 = tf.Variable(tf.random_normal([2,1]), name='weight2')
b2 = tf.Variable(tf.random_normal([1]), name='bias2')
H = tf.sigmoid(tf.matmul(layer ,W1) + b1)

cost = -tf.reduce_mean(Y * tf.log(H) + (1-Y)*tf.log(1-H))
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

prediction = tf.cast(H > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(prediction, Y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(10001):
        cost_val, _ = sess.run([cost,train], feed_dict={X:x_data, Y:y_data})

        if epoch%200 == 0:
            print("epoch :", epoch, "cost_val :",cost_val)

        h,p,a = sess.run([H,prediction,accuracy], feed_dict={X:x_data, Y:y_data})
        print("H :", h, "\nP :\n", p, "\nA :",a)