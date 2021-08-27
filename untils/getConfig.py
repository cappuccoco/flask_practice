import configparser
import os


def getConfig(section,key):
    """
    :param section: 配置名称
    :param key: 配置项
    :return:
    """
    config = configparser.ConfigParser()
    path = os.path.dirname(os.path.dirname(__file__))
    config.read(path+os.sep+'app.config')
    return config.get(section,key)

if __name__ == '__main__':
    print(type(getConfig('database','host')))















