from tool.connect_mysql import connect_db, select_sql, close_connect


def test_connect_mysql():
    connect = connect_db(host='127.0.0.1', user='root', password='12345678', db='dqp')
    print(select_sql(connect, "SELECT count(1) from trade"))
    close_connect(connect)
