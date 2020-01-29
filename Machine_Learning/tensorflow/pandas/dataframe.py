import pandas as pd
'''
DataFrame -> 2-D Data Set(표 형식)
    Series와 dict 데이터를 활용
    JSON형태는 dict 내의 data list 들이 모여있는 형태
    JSON(JavaScript Object Notation)
    - 자바스크립트 언어의 객체 표기법
    - 데이터 저장 구조 (포맷)용도로도 활용!
'''
d = {
    'one':pd.Series([1,2,3], index=['A','B','C']),
    'two':pd.Series([4,5,6,7],index=['A','B','C','D'])
}
df = pd.DataFrame(d)
print(df)
print(type(df))
###################################################################

d = [
    {'name':'bit','age':10,'addr':'Seoul'},
    {'name':'python','age':20,'addr':'Chenan'},
    {'name':'tensor','age':30,'addr':'Asan'}
]

df = pd.DataFrame(d)
print(df)
print(type(d))

###################################################################

#특정 컬럼만 가지고 DataFrame 생성
df2 = pd.DataFrame(d, columns=('name', 'addr'))
print(df2)
print(type(df2))

#데이터 추가
df2['height'] = [170,180,190]
print(df2)
print(type(df2))

#인덱스 선택
df3 = df2.set_index('name')
print(df3)
print(type(df3))

#컬럼 선택
s = df2['name']
print(s)
print(type(s))


#병합(merge)
df4 = pd.DataFrame({'weight':60.8},{'weight':74.2},{'weight':82.3})
df5 = pd.merge(df2, df4, left_index=True, right_index=True)
print(df5)
print(type(df5))


#조인(join)
#공통 key값을 가지는 데이터 셋들을 병합하여 원하는 데이터 추출
df1 = pd.DataFrame({
    'id':[1001,1002,1003,1004,1005,1006,1007],
    'name':['A','B','C','D','E','F','G']
})
df2 = pd.DataFrame({
    'id': [1001, 1003, 1006, 1007],
    'sal': ['10000', '20000', '15000', '8000']
})
#inner join
df3 = pd.merge(df1, df2)
print(df3)

#full outer join
df3 = pd.merge(df1,df2,how='outer')
print(df3)

#left, right outer join
df3=pd.merge(df1,df2,how='left')
print(df3)
df3=pd.merge(df1,df2,how='right')
print(df3)

# on
#이름이 같은 열이 여러개 있는 경우 모두 기준 열로 사용
df1 = pd.DataFrame({
    '성별' : ['남자','여자','여자'],
    '연령' : ['미성년자','성인','미성년자'],
    '번호' : [1,2,3]
})
df2 = pd.DataFrame({
    '성별' : ['남자','남자','여자','여자'],
    '연령' : ['미성년자','성인','미성년자','성인'],
    '번호' : [4,5,6,7]
})
#df3 = pd.merge(df1,df2, on=['성별']) #무엇을 기준으로 조인할 것인지 모른다(같은 값이 많기에)
df3 = pd.merge(df1,df2, on=['성별','연령'])#공통된 컬럼값이 없으면 empty로 출력
print(df3)

#left_on, right_on
#   -> on의 기준 열을 각각 다르게 설정
#   -> 동일한 컬럼명이 아닐 경우에!
df1 = pd.DataFrame({
    'key1':['foo','foo','bar'],
    'key2':['one','two','three'],
    'lval':[1,2,3]
})
df2 = pd.DataFrame({
    'k1':['foo','foo','bar','bar'],
    'k2':['one','one','one','two'],
    'rval':[4,5,6,7]
})
df3 = pd.merge(df1,df2, left_on='key1', right_on='k1')
'''
df1 : left
df2 : right
-> 좌 우측 테이블을 조인하기 위한 기준 열을 지정
'''
print(df3)


#left_index, right_index
#   -> 인덱스를 기준 열로 조인할 때 활용(True)
df1 = pd.DataFrame({
    'key':['A','B','A','A','B','C'],
    'value' : range(6)
})
df2 = pd.DataFrame(
    {'group_val':[3,7]},
    index=['A','B']
)
df3 = pd.merge(df1, df2, left_on='key',right_index=True)
print(df3)

df1 = pd.DataFrame([[1.,2.],[3.,4.],[5.,6.]],
                   columns=['seoul','pusan'],
                   index=['A','C','E'])
df2 = pd.DataFrame(
    [[7.,8.],[9.,10.],[11.,12.],[13.,14.]],
    columns=['cheonan','asan'],
    index=['B','C','D','E']
)
df3 = pd.merge(df1, df2, left_index=True, right_index=True)
print(df3)#각각 설정한 index 기준으로 조인 수행