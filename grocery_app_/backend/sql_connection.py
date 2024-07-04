import MySQLdb
__cnx=None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = MySQLdb.connect(user='root', passwd='Nithya@2004', host='127.0.0.1', db='grocery')
    return __cnx