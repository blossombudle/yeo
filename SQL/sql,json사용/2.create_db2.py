import sqlite3

def create2():
      conn = sqlite3.connect('students2.db')

      cur = conn.cursor()
      cur.execute('''create table information2(
                  number2 integer,
                  iot integer,
                  ml integer,
                  python integer)
      ''')
      
      conn.commit() #최종적으로 테이블 확인
      conn.close()

if __name__=="__main__":
      create2()

