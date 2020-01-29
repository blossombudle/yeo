# 비용함수 그래프 출력 예제

import tensorflow as tf
import matplotlib.pyplot as plt

# 학습 기만 데이터
x = [1,2,3]
y = [1,2,3]

W = tf.placeholder(tf.float32)

H = W*x #가설 정의

cost = tf.reduce_mean(tf.square(H-y)) #비용함수
#reduce_mean() : 텐서 차원에서 평균을 구하는 함수
x = tf.constant([[1.,2.],[3.,6.]])
'''
다음 그림과 같은 2차원의 형태
[1.0,2.0] | 1.5 -> 행 평균
[3.0,6.0] | 4.5
-----------
 2.0 4.0 -> 열 평균
'''
sess = tf.Session()
print(sess.run(x))
print(sess.run(tf.reduce_mean(x)))#전체 데이터 평균
print(sess.run(tf.reduce_mean(x,0)))#열 단위의 평균
print(sess.run(tf.reduce_mean(x,1)))#행 단위의 평균

sess.run(tf.global_variables_initializer())

#변화하는 데이터를 담을 리스트
w_list = []
cost_list = []

for i in range(50,-50):
    feed_w = i * 0.1
    curr_cost, curr_w = sess.run([cost,W], feed_dict={W:feed_w})
    w_list.append(curr_w)
    cost_list.append(curr_cost)
    print('weight :',curr_w, 'cost :',curr_cost)

plt.plot(w_list, cost_list)#학습 중 변화 데이터 그래프 생성
plt.legend()
plt.show()#그래프 출력