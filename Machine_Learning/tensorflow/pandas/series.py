import pandas as pd
'''
pandas module(package) -> data table
    - 데이터의 구조를 나타내는 모듈
    - 엑셀이나 sql같은 테이블 형식으로 구성된 데이터 셋을 활용하기 위한 도구
    - 데이터 구조를 구성하기 위한 데이터 셋(Series)와 2차원 데이터 셋(DataFlame)
    Series : 1차원 배열
    DataFrame : 2차원 배열
    이라 생각!
'''

#price = [92600,92400,92100,94300,92300]
#s = pd.Series(price)#리스트를 전달하여 Series로 생성!
#print(s)#연속된 데이터 셋인 Series로 구성, index도 같이 출력
        #2개의 컬럼으로 구성
#print(s[0])
#print(s[1])
#print(type(s))

#인데스 사용자 부여
s = pd.Series(
    [92600,92400,92100,94300,92300],
    index=['2019-01-01','2019-02-01','2019-03-01','2019-04-01','2019-05-01']
)

print(s)
print(s[0],s['2019-02-01'])

#특정 값(스칼라)으로 초기화
s = pd.Series(7, index=['a','b','c','d'])
#index abcd를 모두 index로 초기화
print(s)


#index, values 형식을 접근, 추출 가능
for idx in s.index:
    print(idx, end=' ')#공백으로 한칸씩 띄워라
else:
    print()

for val in s.values:
    print(val,end=' ')
else:
    print()

#인덱스 기준으로 데이터 연산
#   _->동일한 인덱스끼리 연산을 수행
# ->단, 일치하는 인덱스가 없을 경우 NaN 반환
s1 = pd.Series([10,20,30], index=['A','B','C'])
s2 = pd.Series([10,20,30], index=['C','B','A'])

#Series 간의 사칙연산(*인덱스 기준)
print(s1+s2)
print(s1-s2)
print(s1*s2)
print(s1/s2)
print(s1*3)
