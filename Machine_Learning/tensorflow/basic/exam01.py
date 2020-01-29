import tensorflow as tf
'''
    pip uninstall tensorflow
    pip install tensorflow==1.15.0rc0
    pip install tensorflow-cpu==1.15.0rc0
    pip install tensorflow-gpu==1.15.0rc0
'''
hello = tf.constant("hello tensorflow!!")
sess=tf.Session()
print(sess.run(hello))
'''
tensorflow
    - 데이터 흐름을 그래프로 만들고 실행할 수 있는 라이브러리
    - 파이썬에서 머신러닝 알고리즘을 적용하기 위해 활용
    [수행 흐름]
    1. 데이터 플로우 그래프(Data Flow Graph)를 Build
    2. 데이터를 입력하고 그래프를 실행(Run)
    3. 그래프 내부 노드들을 업데이트(Update)하고 출력!
        -> 2,3 작업을 계속 반복하여 내부 노드(변수)의 값을 갱신!
    Tensor
        - Tensorflow란 데이터 플로우 그래프에서 Tensor가 돌아다니는 형태
        - 단순하게 데이터의 단위, 데이터의 집합(Array, Set)으로 표현!
        - Rank, Shape, Type의 개념을 기반으로 사용
            -Rank - 배열 데이터를 활용하되, 몇 차원 배열인지, 몇 수준인지
                0차원(Scalar, 스칼라) - 데이터 값만 존재
                1차원(Vectro, 백터) - 데이터 값과 위치 존재(Tensor)
                2차원(Matrix, 매트릭스) - 백터들이 모여있는 테이블
                3차원(3-Tensor) - 테이블이 모여있는 큐브(Cube)
                n차원(n-Tensor) - N차원 배열      
           -Tensor(텐서)란 수학적 개념! 어렵게 생각말고, 배열이라 생각!
                - 선형관계를 나타내는 변하지 않는 개념
                - 스칼라곱, 선형변환 같은 수학적 개념을 의미! -> 쉽게생각!
              - 두 개 이상의 독립적인 방향을 동시에 표현 하겠다.
            
                *결론 : 3차원 공간의 x,y,z가 존재한다면,
                x,y,z는 각각의 텐서를 의미하며,
                3-Tensor란 3개의 텐서로 이루어져 있는 Rank를 의미!
                    -> 3차원이다!       
           -Shape : 각 축이 몇 개의 요소(element)들로 구성되어 있는지 표현하는 값
                [2,3]
                - Rank 2 수준 -> 2차원 배열(2-Tensor)
                - 3개의 element가 존재
                    [][][]
                    [][][] 의 형태의 행렬을 의미!
           -Type : 텐서가 담을 수 있는 데이터 타입
                -> tf.int32, tf.float32, ...
'''

#텐서 플로우 주요 함수(노드 생성)
# Tensorflow nod
#   -> 자료구조의 Graph와 데이터 객체를 의미하는 Node를 생각

sess = tf.Session()
'''
tf.Session()
    Session 클래스는 텐서플로우의 노드를 실행하기 위한 클래스
    sess.run(...)을 통해 실제 노드간의 계산식을 수행
'''

# 모든 요소 값이 0인 텐서 생성
tensor = tf.zeros([3,4], tf.int32)
print(tensor)
print(sess.run(tensor))
'''
shape : 정수 리스트 또는 int32 타입의 1차원(1-D) Tensor
dtype : 반환되는 Tensor 데이터 타입 설정
name  : 이름 부여(생략)
'''
exlist = [[1,2,3],[4,5,6]]
tensor = tf.zeros_like(exlist)
#특정 텐서 형태 기준으로 모든 값이 0인 텐서 생성
print(tensor)
print(sess.run(tensor))


exlist =[[3,7]]
tensor = tf.ones_like(exlist)
#특정 텐서 형태 기준으로 모든 값이 1인 텐서 생성
print(tensor)
print(sess.run(tensor))


tensor = tf.fill([2,3],7) # 특정값(스칼라)을 갖는 텐서 생성
print(tensor)
print(sess.run(tensor))

#상수 텐서를 생성하는 함수
tensor = tf.constant([1,2,3])
print(tensor)
print(sess.run(tensor))
tensor = tf.constant(-0.1,shape=[2,3])
print(tensor)
print(sess.run(tensor))