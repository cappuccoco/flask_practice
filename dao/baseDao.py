import pymysql
from untils.getConfig import getConfig

class BaseDao:

    # app.config
    def __init__(self,configFile='pymysql.json'):
        self.__connection = None
        self.__cursor = None
        self.__config = {}

        # 读取配置信息
        self.__config_list = ['host','user','password','database','charset']
        for index in self.__config_list:
            self.__config[index] = getConfig('database',index)
        self.__config['port'] =  int(getConfig('database','port'))

        pass

    # getconnection 懒汉式
    def getConnection(self):
        if self.__connection:
            return self.__connection

        try:
            self.__connection = pymysql.connect(**self.__config)
            return self.__connection
        except pymysql.MySQLError as e:
            print("Exception:"+str(e))

    # getcursor
    def getCursor(self):
        if self.__cursor:
            return self.__cursor

        try:
            self.__cursor = self.getConnection().cursor()
            return self.__cursor
        except pymysql.MySQLError as e:
            print("Exception:"+str(e))
        pass


    # execute
    def execute(self,sql,params=None):
        try:
            self.__cursor = self.getCursor()
            if params:
                result = self.__cursor.execute(sql,params)
            else:
                result = self.__cursor.execute(sql)
            return result
        except (pymysql.MySQLError, pymysql.DatabaseError, Exception) as e:
            print("数据库访问异常")
            self.rollback()
            pass


    # rollback
    def rollback(self):
        return self.getConnection().rollback()

    # fetchAll
    def fetchAll(self):
        return self.getCursor().fetchall()

    # fetchOne
    def fetchOne(self):
        return self.getCursor().fetchone()

    # commit
    def commit(self):
        return self.getConnection().commit()

    # close
    def close(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__connection:
            self.__connection.close()


if __name__ == '__main__':
    # dao = BaseDao()
    # sql = "insert into csdndata values (%d,%s,%s,%s)"
    # dao.execute(sql, {100, 'https://baidu.com', '标题', '内容'})
    # dao.commit()
    # dao.close()
    dao = BaseDao()
    dao.getConnection()
    dao.execute("SELECT * FROM userdata WHERE userID = 'a123456' ")
    print(dao.fetchOne())
    dao.close()
    pass