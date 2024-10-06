from os import getenv
from dotenv import load_dotenv
import psycopg2

load_dotenv()

class PgSQL:

    _host = getenv('DB_HOST')
    _port = getenv('DB_PORT')
    _database = getenv('DB_NAME')
    _user = getenv('DB_USER')
    _password = getenv('DB_PASSWORD')
    conn = None

    def __init__(self):
        print('PgSQL initialized')
    
    def __del__(self):
        if self.conn != None:
            self.conn.close()

    @property
    def host(self): return self._host
    @host.setter
    def host(self, value): self._host = value
    
    @property
    def database(self): return self._database
    @database.setter
    def database(self, value): self._database = value
    
    @property
    def user(self): return self._user
    @user.setter
    def user(self, value): self._user = value
    
    @property
    def password(self): return self._password
    @password.setter
    def password(self, value): self._password = value
    
    def connect(self):
        if self.conn != None:
            return
        db_url = f"postgresql://{self._user}:{self._password}@{self._host}:{self._port}/{self._database}"
        print(db_url)
        self.conn = psycopg2.connect(db_url)
        self.cursor = self.conn.cursor()
        return self
    
    def check_connection(self):
        if self.conn == None:
            return False
        return True
        
    '''
    登録系クエリを実行する 
    '''
    def execute(self, query, params=None):
        try:

            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            exit()
            return False

    '''
    データを1件取得する
    '''
    def fetch_one(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            result = self.cursor.fetchone()
            return result[0]
        except Exception as e:
            print(e)
            exit()
            return None
    
    '''
    データを全て取得する
    '''
    def fetch_all(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            exit()
            return None

    def close(self):
        self.conn.close()

    


