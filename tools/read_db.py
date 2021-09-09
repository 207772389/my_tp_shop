# -*- coding: utf-8 -*-
"""
@Time ： 2021/7/13 10:21
@Auth ： cainiao
@File ：read_db.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import pymysql

class ReadDb():
    #因为连接对象多处使用，所以弄个类变量，方便使用，也是保证了始终只有一个连接对象
    conn = None
    #获取连接对象
    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect(host="mysql8.test.picooc.cn",user="live",passwd="picooc123",database="live",charset="utf8") #注意这里不是utf-8
        return self.conn
    #获取游标对象
    def get_cursor(self):
        return self.get_conn().cursor()
    #关闭游标对象
    def close_cursor(self,cursor):
        if cursor:
            cursor.close()
    #关闭连接对象
    def close_conn(self):
        if self.conn:
            self.conn.close()
            #注意：关闭完conn，对象还存在内存中，需要手动置空操作
            self.conn = None #释放内存中的地址
    #获取单条记录
    def get_sql_one(self,sql):
        cursor = None
        data = None
        try:
            cursor = self.get_cursor()
            cursor.execute(sql)
            data = cursor.fetchone()
        except Exception as e:
            print("get_sql_one excute error:",e)
        finally:
            self.close_cursor(cursor)
            self.close_conn()
            return data
    #获取多条记录
    def get_sql_all(self,sql):
        cursor = None
        data = None
        try:
            cursor = self.get_cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as e:
            print("get_sql_all excute error:", e)
        finally:
            self.close_cursor(cursor)
            self.close_conn()
            return data

    # 获取指定条数的记录
    def get_sql_many(self, sql ,num):
        cursor = None
        data = None
        try:
            cursor = self.get_cursor()
            cursor.execute(sql)
            data = cursor.fetchmany(num)
        except Exception as e:
            print("get_sql_all excute error:", e)
        finally:
            self.close_cursor(cursor)
            self.close_conn()
            return data
    #修改数据库操作
    def update_sql(self,sql):
        cursor = None
        data = None
        try:
            cursor = self.get_cursor()
            cursor.execute(sql)
            #提交事务
            self.conn.commit()
        except Exception as e:
            #事务回滚
            self.conn.rollback()
            print("update excute error:", e)
        finally:
            self.close_cursor(cursor)
            self.close_conn()
    """长的sql语句要用6个双引号这种样式，这个是调用的示例，sql里的参数写活。"""
    def get_data(self,month_name,platform_anchor_id):
        sql = """SELECT system_anchor_id,transaction_date,platform_anchor_name
      FROM sales_medium WHERE transaction_date >= '2021-0{}-01 00:00:00' 
    AND transaction_date < '2021-0{}-01 00:00:00' 
    AND _is_delete = 0 
    AND is_commission=1
    AND platform = '抖音'
    AND platform_anchor_id={}
    ORDER BY transaction_date""".format(month_name,int(month_name)+1,platform_anchor_id)

        # 调用封装的get_sql_one执行
        first_line = ReadDb().get_sql_one(sql)
        data = first_line[1]
        return str(data)