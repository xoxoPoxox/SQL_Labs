import psycopg2
from config import host, user, password, db_name


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO public.usr(id, name) VALUES (1, 'abc')"""
        )
        connection.commit()
        print("INSERTED!")
        connection.close()
except Exception as ex:
    print("[INFO] Error!!!", ex)
