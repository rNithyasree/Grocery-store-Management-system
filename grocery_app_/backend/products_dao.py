from sql_connection import get_sql_connection
def get_all_products(connection):
    #cnx = MySQLdb.connect(user='root', passwd='Nithya@2004',host='127.0.0.1',db='grocery')
    cursor = connection.cursor()
    query = "SELECT products.product_id,products.name,products.uop,products.price_per_unit,uom.uom_name from products inner join uom on products.uop=uom.uom_id;"
    cursor.execute(query)
    response=[]

    for (product_id,name,uop,price_per_unit,uom_name) in cursor:
        response.append({'product_id':product_id,'name':name,'uop':uop,'price_per_unit':price_per_unit,'uom_name':uom_name})

    #cnx.close()
    return response
def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products (name, uop, price_per_unit) VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uop'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid


def delete_product(connection,product_id):
    cursor = connection.cursor()
    query=("delete from products where product_id="+str(product_id))
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid


if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection,3))
