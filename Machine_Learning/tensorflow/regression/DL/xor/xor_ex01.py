import tensorflow as tf

x_data = [[0,0],[0,1],[1,0],[1,1]]
y_data = [[0],[1],[1],[1]] #case or
#y_data = [[0],[0],[0],[1]] #case and
#y_data = [[0],[1],[1],[0]] #case xor

X = tf.placeholder(tf.float32,[None,2])
Y = tf.placeholder(tf.float32,[None,1])

W = tf.Variable(tf.random_normal([2,1]))
b = tf.Variable(tf.random_normal([1]))

H = tf.sigmoid(tf.matmul(X,W) + b)
cost = -tf.reduce_mean(Y * tf.log(H) + (1-Y)*tf.log(1-H))

train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

prediction = tf.cast(H > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(prediction, Y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(2001):
        cost_val, w_val, _ = sess.run([cost,W,train], feed_dict={X:x_data, Y:y_data})

        if epoch%200 == 0:
            print("epoch :", epoch, "cost_val :",cost_val, "w_val :", w_val)

        h,p,a = sess.run([H,prediction,accuracy], feed_dict={X:x_data, Y:y_data})
        print("H :", h, "\nP :\n", p, "\nA :",a)