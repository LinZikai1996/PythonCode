import pymysql


def connect_db(host, user, password, db):
    return pymysql.connect(host=host, user=user, passwd=password, port=3306, db=db, charset='utf8')


def select_sql(conn: pymysql.Connection, sql: str):
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()  # 通过fetchall方法获得数据
    cur.close()
    return data


def execute_sql(conn: pymysql.Connection, sql: str):
    cur = conn.cursor()
    cur.execute(sql)  # 执行sql语句
    conn.commit()  # 提交到数据库执行
    cur.close()


def close_connect(conn: pymysql.Connection):
    conn.close()
