
from dao.baseDao import BaseDao

class Article:

    def __init__(self):
        self.__dao = BaseDao()

    # 文章的id和title
    def getArticles(self,pagenum,limit=10):
        """
        :param pagenum: pagenum
        :param limit: page limit
        :return: resultset
        """
        try:
            sql = "SELECT id,title FROM csdndata  LIMIT {},{}".format(pagenum*limit,limit)
            self.__dao.execute(sql)
            result = self.__dao.fetchAll()
            data = []
            for x in result:
                data.append(x)
            return data
        finally:
            self.close()

    # 获取文章内容
    def getText(self,articleNum):
        """
        :param articleNum: 文章的id
        :return: 爬取的网页数据
        """
        try:
            sql = "SELECT title,content FROM csdndata WHERE id = '{}'".format(articleNum)
            self.__dao.execute(sql)
            result = self.__dao.fetchOne()
            return result
        finally:
            self.close()

    def getTotalNum(self):
        """
        获取文章总数
        :return:
        """
        try:
            sql = "SELECT COUNT(*) FROM csdndata"
            result = self.__dao.execute(sql)
            num = self.__dao.fetchOne()[0]
            return int(num)
        except Exception as e:
            print(str(e))
            return None
        finally:
            self.close()

    def close(self):
        self.__dao.close()



if __name__ == '__main__':
    article = Article()
    print(article.getTotalNum())













