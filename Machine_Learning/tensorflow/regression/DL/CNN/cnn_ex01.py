import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

'''
CNN(Convolutional Neural Nestwork)
    - 이미지를 부분 부분 쪼개어 학습 수행
    - 입력 데이터(이미지)로부터 특징 추출 목적
    
Channel(채널)
    이미지 또한 숫자 데이터 구성
    크기 30 * 28의 3개의 색상 이미지는 Shape=[30,28,3]으로 표현됨
        -> 흑백 이미지는 [30,28,1] (흰색의 명도만 조절하면 되니까)
    
Filter(필터,Kernel)
    이미지의 특성을 찾기 위한 역할(파라미터)
    이미지를 배열로 보았을 때, 유사한 데이터라면 큰 값,
    다르면 0에 가까운 값으로 판단
    
    필터를 원본이미지에 적용
    Origin Image(5X5)   ->  Convolved Feature(3*3)
    1 1 1 0 0   ->  4 3 4
    0 1 1 1 0   ->  2 4 3
    0 0 1 1 1   ->  2 3 4
    0 0 1 1 0       Feature Map, Activation Map  구성
    0 1 1 0 0       *특성 추출이 목적!
    Stride : 필터를 움직인 간격, 위에서 적용한 Stride 값은 1
    Padding : 필터를 여러번 거치게 되면 원본 특성이 사라질 수 있다.
              이를 방지하기 위해 활용하는 것이 패딩(shape값을 유지)
              32*32*3입력 값에서 5*5*3필터를 적용시킨다면,
              Feature Map의 크기는 28*28*3이 된다.
                -> 출력 데이터 크기 = (입력 데이커 크기 - 필터 크기) +1 / Stride
                -> 28 = (32 - 5) + 1 / 1
                * 출력 데이터 크기는 무조건 정수로 떨어져야한다.
                * 정수 결과가 나오지 않는 Stride 크기는 사용할 수 없다.
                * 필터를 씌었을 때 왼쪽 끝과 오른쪽 끝 마무리가 깔끔하게
              - 실제 값에서만 잘 동작하는 경우 (Overfitting)를 방지
              - 이미지 외곽선 추출에 활용도 가능!
    Pooling(*Resizing, Sampling) - 크기를 작아지게
        - Convolutional Layer의 결과 데이터(출력)를 받아,
          데이터 크기를 줄이거나, 특정 데이터를 강조하기 위해 활용
          Max     Pooling : 최대 값 추출 (*)
          Min     Pooling : 최소 값 추출 ()
          Average Pooling : 평균 값 추출 ()
        - 특징 추출 후 내가 원하는 결과를 예측(판단)을 수행하된,
        모든 특징을 참고하여 판단할 필요는 없다.
        (작은 이미지를 가지고도 예측, 판단이 가능하다.)
        * 크기가 작아지게!
    [전체 흐름도]
    input -> Conv -> Pool -> Conv -> Pool -> Conv -> Pool -> NN(Layer)... -> output
'''
mnist = input_data.read_data_sets("../mnist_data/", one_hot=True)

learning_rate = 0.001
num_epochs = 15
batch_size = 100

X = tf.placeholder(tf.float32 ,[None, 784])
X_img = tf.reshape(X,[-1,28,28,1]) #image size 28*28*,(회색조, 흑백)
Y = tf.placeholder(tf.float32,[None, 10])

W1 = tf.Variable(tf.random_normal([3,3,1,32], stddev=0.01))
L1 = tf.nn.conv2d(X_img, W1, strides=[1,1,1,1], padding='SAME')
'''
tf.nn.conv2d(input, filter, strides, padding, ...)
    input : 입력데이터
    filter : Weight와 같이 생각
    -> [filter_height, filter_width, input_channels, output_channel] 
    strides : 필터 이동 간격
    padding : 'SAME' 기존 입/출력 값과 동일하게!
'''
L1 = tf.nn.relu(L1)
L1 = tf.nn.max_pool(L1, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')
#                   L1 = batch?    strides 얼마만큼 이동시키나
# tensor w kernel
'''
tf.nn.max_pool(input, ksize, strides, padding, ...)
    input : 입력 데이터
    ksize : 입력 데이터의 각 차원의 크기
        -> 2칸씩 이동하여 결과 하나를 만들어라.(큰 값)
        ->[2][2][3][2]
          [3][1][7][8]  -> [3][8]
          [4][5][1][0]     [8][4]
          [8][6][3][4]
    strides : 필터 이동 간격
    padding : 'SAME' 기존 입/출력 값과 동일하게!
    풀링 작업은 리사이즈와 함께 하기
    풀링으로 값을 추출 하고 그에 맞게 사이즈 재 배열
'''
W2 = tf.Variable(tf.random_normal([3,3,32,64], stddev=0.01))
L2 = tf.nn.conv2d(L1, W2, strides=[1,1,1,1], padding='SAME')
L2 = tf.nn.relu(L2)
L2 = tf.nn.max_pool(L2, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

L2_flat = tf.reshape(L2, [-1,7*7*64])

W3 = tf.get_variable('W3', shape=[7*7*64,10])
b = tf.Variable(tf.random_normal([10]))
H = tf.matmul(L2_flat, W3) + b

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=H, labels=Y))

train = tf.train.AdamOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    total_batch = int(mnist.train.num_examples / batch_size)
    for i in range(num_epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples / batch_size)
        for epoch in range(total_batch):
            x_data, y_data = mnist.train.next_batch(batch_size)
            cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data})
            avg_cost += cost_val / total_batch
        print('epoch :', i, 'cost :', avg_cost)

    prediction = tf.equal(tf.argmax(H,1), tf.argmax(Y,1))
    accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))
    print('accuracy :', sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels}))