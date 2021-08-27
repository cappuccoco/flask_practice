
# 数据查询
from dao.baseDao import BaseDao

class DataDao(BaseDao):

    # getAllData
    def getAllData(self):
        try:
            sql = "select * from test"
            self.getConnection()
            self.execute(sql)
            result = self.fetchAll()
            data = []
            for x in result:
                data.append(x)

        except Exception as e:
            print("Exception"+str(e))
        finally:
            self.close()

        return data


if __name__ == "__main__":
    data = DataDao().getAllData()
    print(data)


