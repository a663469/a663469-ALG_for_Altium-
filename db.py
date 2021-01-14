import pymysql
#import sqlite3
#from _datetime import datetime
#from sqlalchemy import create_engine, select, MetaData, Table


class db_altium_lib:
    def sorting_rules(self, group_name):
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='qwer',
                                     db='altium_lib',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `contains`, `not_contains` FROM `sorting_rules` WHERE `group_name`=%s"
                cursor.execute(sql, (group_name,))
                result = cursor.fetchone()
        finally:
            connection.close()
        return result

    def type_components(self):
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='qwer',
                                     db='altium_lib',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `sorting_rules`"
                cursor.execute(sql)
                rows = cursor.fetchall()
                result = []
                for row in rows:
                    result.append(row)
        finally:
            connection.close()
        return result
"""
    def write_components_to_bd(self, group_name, id, art):
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='qwer',
                                     db='altium_lib',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()



    #def sorting_rules_alchemy(self, group_name):
    #    pass

        engine = create_engine("mysql+pymysql://root:qwer@127.0.0.1:3306/altium_lib")
        engine.connect()
        metadata = MetaData()
        db = Table('sorting_rules', metadata, autoload=True, autoload_with=engine)

        #query = select([mysql_db])
        #ResultProxy = connection.execute(query)
        return db.columns.keys()



class db_todo:
    def init_db_todo(self):
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()
        # Create table
        c.execute('''CREATE TABLE stocks(date text, task text, status text)''')
        # Save (commit) the changes
        conn.commit()
        # Just be sure any changes have been committed or they will be lost.
        conn.close()

    def add_to_db_todo(self, task):
        if task == '':
            return 0
        t_now = datetime.now()
        t_now = t_now.strftime("%Y-%m-%d %H:%M:%S")
        status = "no started"
        id_db = len(db_todo.return_db_list("A"))
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()
        c.execute("INSERT INTO stocks VALUES (?, ?, ?, ?)", (t_now, task, status, id_db))
        conn.commit()
        conn.close()
        return 1

    def update_status_in_db_todo(self, status, id_db):
        conn = sqlite3.connect('db.sqlite')
        conn.execute("UPDATE stocks set status = ? where id = ?", (status, id_db))
        conn.commit()
        conn.close()

    def print_all_tasks(self):
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()
        #for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        #    print(row)
        with conn:
            c.execute("SELECT id , date_time, task, status FROM stocks")
            print(c.fetchall())
        conn.close()

    def return_db_list(self):
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()
        tmp = 0
        with conn:
            c.execute("SELECT id , date_time, task, status FROM stocks")
            tmp = (c.fetchall())
        conn.close()
        return tmp
"""