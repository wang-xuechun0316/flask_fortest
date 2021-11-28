from pymysql import connect
from pymysql.cursors import DictCursor
from settings import MYSQL_HOST,MYSQL_PORT,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DATA

class Builds(object):
    def __init__(self):  # create
        self.conn=connect(       # mysql -u root -p
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            database=MYSQL_DATA,
            password=MYSQL_PASSWORD,
            charset='utf8'
        )
        self.cursor=self.conn.cursor(DictCursor)   # dictionary format

    def __del__(self):   # delete
        self.cursor.close()
        self.conn.close()

    def get_build_infos_limit(self):    # get info and print if dictionary format
        sql='select * from build_user limit 1'
        self.cursor.execute(sql)
        data=[]  # create a array
        for temp in self.cursor.fetchall():
            print(temp)
            data.append(temp)   # add a item to this array
        return data