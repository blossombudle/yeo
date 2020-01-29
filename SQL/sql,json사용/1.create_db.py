import sqlite3

def create1():
      conn = sqlite3.connect('students.db')

      cur = conn.cursor()
      cur.execute('''create table information(
                  number integer,
                  name text,
                  address text,
                  call integer,
                  sex integer)
      ''')
      
      conn.commit() #최종적으로 테이블 확인
      conn.close()

if __name__=="__main__":
      create1()

