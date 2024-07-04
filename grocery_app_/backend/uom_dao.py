from sql_connection import get_sql_connection
def get_uoms(connection):
    response=[]
    cursor = connection.cursor()
    query=("SELECT * FROM uom")
    cursor.execute(query)
    for (uom_id,uom_name) in cursor:
        response.append({'uom_id':uom_id,'uom_name':uom_name})
    return response

if __name__ == '__main__':

    connection = get_sql_connection()
    print(get_uoms(connection))