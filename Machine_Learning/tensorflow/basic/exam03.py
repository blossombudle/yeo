import tensorflow as tf
sess = tf.Session()

#tf.random_
tensor = tf.random_normal([2,3], 0.0, 1.0, tf.float32)
'''
mean   : 정규 분포의 평균 값
stddev : 정규 분포의 표준 편차
'''
print(tensor)
print(sess.run(tensor))




#tf.random_uniform(shpae, minval, maxval, dtype, seed, name)
#   -> 균등분포의 난수 값 반환
tensor = tf.random_uniform([2,3],0,10,tf.float32) # 0~10의 사이 값
print(tensor)
print(sess.run(tensor))





exlist = [[1,2], [3,4], [5,6]]
tensor = tf.random_shuffle(exlist)
print(tensor)
print(sess.run(tensor))




exlist = [[1,2,3],[4,5,6]]
tensor = tf.random_crop(exlist, [2,1]) #shape[2,1]
'''
특정 크기만큼 랜덤하게 잘라내기 위한 함수
value : 기준텐서
size : value와 동일한 랭크의 텐서
'''
print(tensor)
print(sess.run(tensor))





#난수 시드 값 설정
tf.set_random_seed(777)

a = tf.random_uniform([1])
b = tf.random_normal([1])

with tf.Session() as sess1:
    print(sess1.run(a))
    print(sess1.run(a))
    print(sess1.run(b))
    print(sess1.run(b))

with tf.Session() as sess2:
    print(sess2.run(a))
    print(sess2.run(a))
    print(sess2.run(b))
    print(sess2.run(b))



'''
reduce_sum(tensor, axis, keepdims, name, ....)
    -> 차원을 줄여 합계를 구한다.
'''

tensor = tf.constant([[1,2,3],
                     [4,5,6]])
print(sess.run(tf.reduce_sum(tensor))) # 모든 요소의 합
print(sess.run(tf.reduce_sum(tensor, axis=0))) # [5,7,9] 세로 기준의 합계
print(sess.run(tf.reduce_sum(tensor, axis=1))) # [6,15] 가로 기준의 합계
print(sess.run(tf.reduce_sum(tensor, axis=0, keep_dims=True))) # 세로 기준, 차원 수준 유지