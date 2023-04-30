import pandas as pd
import pymysql
import warnings

warnings.filterwarnings("ignore")


def connect():
    """connect mysql DB"""
    try:
        db = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='12345678',
            db='dqp',
            charset='utf8'
        )
        return db
    except Exception:
        raise Exception("Fail to connect mysql DB")


class ConnectDb:
    def __init__(self, sql: str):
        self._sql = sql

    def query_data(self):
        """run sql"""
        db = connect()

        try:
            df = pd.read_sql_query(self._sql, db)
            return df
        except Exception:
            db.rollback()
            raise Exception("Fail to DB")

    def get_count(self):
        db = connect()
        cursor = db.cursor()
        cursor.execute(self._sql)
        result = cursor.fetchone()
        return result
