import pymysql


def connect_db():
    return pymysql.connect(host='127.0.0.1',
                           user='root', passwd='12345678', port=3306,
                           db='arknights', charset='utf8')

