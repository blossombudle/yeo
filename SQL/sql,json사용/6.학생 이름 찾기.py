import sqlite3
import re
def find_students():
      conn = sqlite3.connect('students.db')
      cur = conn.cursor()
      conn2 = sqlite3.connect('students2.db')
      cur2 = conn2.cursor()

      a = 'SELECT * FROM information'
      b = 'SELECT * FROM information2'
      
      cur.execute(a)
      cur2.execute(b)
      
      information = cur.fetchall()
      information2 = cur2.fetchall()

      #private total
      i=0
      private_total=0
      private_average=0
      x=list()
      y=list()

      while i<10:
           private_total = information2[i][2] + information2[i][2] +information2[i][3]
           private_average = private_total/3
           x.append(private_total)
           y.append(private_average)
           i = i+1

      

      #total
      i=0
      sum_iot=0
      sum_ml=0
      sum_python=0

      while i<10:
           sum_iot = sum_iot + information2[i][1]
           sum_ml = sum_ml + information2[i][2]
           sum_python = sum_python + information2[i][3]
           i = i+1
           
      sum_total =sum_iot+sum_ml+sum_python 

      #average

      average = sum_total/30


      i=0
      while i<10:
            print(information[i][1]+'학생 총 합 점수 :',x[i],'\t')
            print('            평균 :',round(y[i],2))
            print('\t')
            i = i+1

      print('Iot 평균 :',sum_iot/10)
      print('\t')
      print('ML 평균 :',sum_ml/10)
      print('\t')
      print('Python 평균 :',sum_python/10)
      print('\t')
      print('총 합 :',sum_total)
      print('\t')
      print('총 평균 :',average)
      print('\t')

      conn.close()
      conn2.close()


      #학생정보 찾기
      conn = sqlite3.connect('students.db')
      cur = conn.cursor()
      conn2 = sqlite3.connect('students2.db')
      cur2 = conn2.cursor()
      
      a = input('조회할 학생 이름을 입력하세요 : ')
      b = 'SELECT * FROM information WHERE name ="'+a+'"'
      cur.execute(b)
      information = cur.fetchone()
      x = information[0]

      c = 'SELECT * FROM information2 WHERE number2 = "'+str(x)+'"'
      cur2.execute(c)
      information2 = cur2.fetchone()


      sum = 0
      sum = information2[1]+information2[2]+information2[3]
      average = sum/3

      print(information[1]+'학생 총 합 점수 :',sum,'\t')
      print('            평균 :',round(average,2))

      
      
      #if information[0] 
      


      conn.close()
      conn2.close()






if __name__=="__main__":
      find_students()
      print('===========================================')
