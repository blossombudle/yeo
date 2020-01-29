import sqlite3

def insert_infomation():
      conn = sqlite3.connect('students.db')
      cur = conn.cursor()
      insert_sql = 'insert into information values(?,?,?,?,?)'

      information = [
            (0,'a','a동',0000,'f'),
            (1,'b','b동',1111,'m'),
            (2,'c','c동',2222,'f'),
            (3,'d','d동',3333,'f'),
            (4,'e','e동',4444,'m'),
            (5,'f','f동',5555,'m'),
            (6,'g','g동',6666,'m'),
            (7,'h','h동',7777,'f'),
            (8,'i','i동',8888,'m'),
            (9,'j','j동',9999,'f')
            ]
      cur.executemany(insert_sql, information)

      conn.commit()
      conn.close()
      
if __name__=="__main__":
      insert_infomation() 
