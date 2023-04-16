import psycopg2
from config import host, user, password, db_name


def insertBook(id_b, aut, nam):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    with connection.cursor() as cursor:
        ex = (id_b, aut, nam)
        cursor.execute(
            """INSERT INTO public."Books"(id_book, author, name) VALUES (%s, %s, %s)""", ex
        )
        connection.commit()
        print("INSERTED!")
def printBook():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM public."Books"; """
        )
        rw = cursor.fetchall()
        for row in rw:
            print("Id =", row[0], )
            print("Автор =", row[1])
            print("Название =", row[2], "\n")
def updateBook(au, id_b):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    cur = connection.cursor()
    cur.execute("""UPDATE public."Books" set author = %s where id_book = %s""", (au, id_b))
    connection.commit()

term = int(input('Выбери действие: добавить книгу - 1, показать все книги - 2, изменить книгу - 3 '))
if term == 1:
        id_b = int(input('Введите id книги: '))
        aut = input('Введите автора: ')
        nam = input('Введите название: ')
        insertBook(id_b, aut, nam)
elif term == 2:
    printBook()
elif term == 3:
    id_b = int(input('Введите id книги: '))
    au = input('Новый автор: ')
    updateBook(au, id_b)