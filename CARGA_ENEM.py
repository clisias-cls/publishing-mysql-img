import mysql.connector as ms
from mysql.connector import Error
#from mysql.connector import Error

try:
    conn = ms.connect(host='localhost',
                      database='prova',
                      port=3306,
                      user='root',
                      password='root')
    
    cursor = conn.cursor()
    cursor.callproc('prova.atualiza_modelo_prova')
    # print results
    print("Printing details")
    for result in cursor.stored_results():
        print(result.fetchall())

except ms.Error as error:
    print("Failed to execute stored procedure: {}".format(error))
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("MySQL connection is closed")