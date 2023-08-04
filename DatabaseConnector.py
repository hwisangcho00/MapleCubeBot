import os
import psycopg2
from dotenv import load_dotenv

class DatabaseConnector:
    
    def __init__(self):
        load_dotenv()
        self.DATABASE_URL = os.getenv('DATABASE_URL')

    def incrementLog(self, name):
        conn = psycopg2.connect(self.DATABASE_URL)
        with conn.cursor() as cur:
            try:
              cur.execute("SET DATABASE = defaultdb")
              cur.execute('''INSERT INTO log VALUES (DEFAULT, %s, current_timestamp);''', (name, ))
              conn.commit()
              cur.close()
            except Exception as e:
               print(e)
            finally:
              conn.close()
  
    def initiateDB(self):
      conn = psycopg2.connect(self.DATABASE_URL)
      with conn.cursor() as cur:
          try:
            cur.execute("SET DATABASE = defaultdb")
            cur.execute('''CREATE TABLE IF NOT EXISTS log (
                        ID SERIAL NOT NULL PRIMARY KEY, 
                        Command VARCHAR(16),
                        Time TIMESTAMP
                        );''')
            conn.commit()
            cur.close()
          except Exception as e:
               print(e)
          finally:
            conn.close()

    def testDB(self):
        conn = psycopg2.connect(self.DATABASE_URL)
        with conn.cursor() as cur:
          try:
            cur.execute("SELECT COUNT(*) FROM log")
            print(cur.fetchall())
          except Exception as e:
               print(e)
          finally:
             conn.close()

if __name__ == '__main__':
  dc = DatabaseConnector()
  dc.testDB()
  
  