import pyodbc

cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                    "Server=localhost;"
                    "Database=chugunova;"
                    "Trusted_Connection=yes;")
cursor = cnxn.cursor()
cursor.execute("INSERT INTO dbo.password (id, password) VALUES (1, 111)")
cursor.execute("INSERT INTO dbo.password (id, password) VALUES (2, 222)")
cursor.commit()

#row = cursor.fetchone()
cnxn.close()