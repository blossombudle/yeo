import tensorflow as tf

'''
    머신 러닝(ML, Machine Learnig)
        - 수 많은 경우에 따라 동작하다록 로직 구성
        - 특정 경우가 너무 많으니, 유저(개발자)가 정하지않고,
          프로그램 자체가 데이터 기반으로 학습하는 기법!
        
    대표 알고리즘
    Linear Regression    선형 회귀
    Logistic Regression  로지스틱 회귀
        -> Classification 분류
    Supervised Learnig
        -> 이미지 분류, 이메일 스팸 필터, 택시 비용 추산 등...
        -> 이미 결정된 값을 가지고 학습(모델)을 구성
    Training Data Set
    [학습 데이터 셋]
        Y=X
        1=1,4,7
        2=2,5,8
        3=3,6,9
            -> Y가 3이라면, X는 3,6,9라는 결과!
        *반드시, 학습 데이터 셋이 필요!
        *기반된 데이터로 학습하여 새로운 경우를 추출
'''

#시험 성적의 경우 학습 시간에 따라 몇점이 나오냐>를 구함.
#   -> Regression
'''
Training Data Set ->
X(time)   Y(time)
10        95
9         90
5         60
2         30
내가 만약 7시간을 공부했을때 예상 점수는?(예측값)
'''