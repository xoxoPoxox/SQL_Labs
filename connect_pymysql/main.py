import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Successfully!")

    try:
        #cursor = connection.cursor()
        with connection.cursor() as cursor:
            insert_query = "INSERT INTO usr (idusr, name, surname) VALUES (2, 'bbb', 'ccc');"
            cursor.execute(insert_query)
            connection.commit()
    finally:
        connection.close()
except Exception as ex:
    print("Connection refused...")
    print(ex)