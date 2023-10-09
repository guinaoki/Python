'''

1. 
2. 
3. DB details
4. Driver cx_Oracle

PEP 249 - Python Database specification v2.0

Módulos Python
-cx_Oracle - Oracle Database
-pyodbcc - Microsoft SQL Server
-pymsql - MySQL
-Psycopg2 = PostgreSQL

1. Importar o driver cx_Oracle
2. Estabelecer uma conexão entre o Python e o DB
3. Criar um cursor (Objeto para executar queries e obter resultados após a execução)

'''

import cx_Oracle

#create connection
conn = cx_Oracle.connect(user="RM551456", password="150404", host="oracle.fiap.com.br/orcl")

print(conn.version)

#create cursor
cursor = conn.cursor()

#create table
sql_create = """
CREATE TABLE CEO_DETAILS(

    FIRST_NAME VARCHAR(50),
    LAST_NAME VARCHAR(50),
    COMPANY VARCHAR2(50),
    AGE NUMBER(3,0)

)
"""
#execute query
cursor.execute(sql_create)
print('Tabela Criada')

#fechar a conexão
conn.close()

#fechar o cursor
cursor.close()