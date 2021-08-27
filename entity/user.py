from dao.baseDao import BaseDao


class User:

    def __init__(self,userID = None,userName = None,password = None,email = None):
        self.__userID = userID
        self.__userName = userName
        self.__password = password
        self.__email = email
        self.__dao = BaseDao()

    def login(self):
        try:
            if self.__password:
                sql = "SELECT * FROM userdata WHERE userID = '{}' ".format(self.__userID)
                self.__dao.execute(sql)
                result = self.__dao.fetchOne()
                pwd = result[2]
                if pwd == self.__password:
                    return result
            else:
                return False
        except Exception as e:
            print(str(e))
            return False
        finally:
            self.close()

    def regist(self,userID,userpwd,username,useremail):
        try:
            sql = "INSERT INTO userdata VALUES('{}','{}','{}','{}')".format(
                userID, username, userpwd, useremail
            )
            self.__dao.execute(sql)
            self.__dao.commit()
            return True
        except Exception as e:
            print(str(e))
            return False
        finally:
            self.close()

    def checkID(self,userID):
        """
        :param userID:
        :return:  存在则返回 1 ,不存在返回 0 ,报错返回 3
        """
        try:
            sql = "SELECT * FROM userdata WHERE userID = '{}'".format(userID)
            result = self.__dao.execute(sql)
            if result:
                return 1
            else:
                return 0
        except Exception as e:
            print(str(e))
            return 3
        finally:
            self.close()


    def close(self):
        self.__dao.close()




if __name__ == '__main__':
    user = User('a123456',password='123456')
    print(user.login())




