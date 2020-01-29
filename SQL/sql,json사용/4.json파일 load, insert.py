import json
import sqlite3
import re

with open('words.json','r') as f:
      json_data = json.load(f)
#print(json.dumps(json_data))

#학번
i=0    
number=[]
while i<10:
      number2 = json_data['number2'][str(i)]
      number.append(number2)
      i=i+1
      
#iot 점수
iot=[]     
print('\t')
i=0
while i<10:
      number2 = json_data['iot'][str(i)]
      iot.append(number2)
      i=i+1
      
#ml 점수
ml=[]
print('\t')
i=0
while i<10:
      number2 = json_data['ml'][str(i)]
      ml.append(number2)
      i=i+1

#python 점수
python = [] 
print('\t')
i=0
while i<10:
      number2 = json_data['python'][str(i)]
      python.append(number2)
      i=i+1

#total
i=0
sum_iot=0
sum_ml=0
sum_python=0

while i<10:
     sum_iot = sum_iot + iot[i]
     sum_ml = sum_ml + ml[i]
     sum_python = sum_python + python[i]
     i = i+1
     
sum_total =sum_iot+sum_ml+sum_python 

#average

average = sum_total/30


print(number)
print(iot)
print(ml)
print(python)
print(sum_total)
print(average)


def insert_infomation():
      conn = sqlite3.connect('students2.db')
      cur = conn.cursor()
      insert_sql = 'insert into information2 values(?,?,?,?)'

      information =list()
      i=0
      while i<10:
            information += [(number[i],iot[i],ml[i],python[i])]
            i = i+1
            
      cur.executemany(insert_sql, information)
      conn.commit()
      conn.close()
      
if __name__=="__main__":
      insert_infomation() 
