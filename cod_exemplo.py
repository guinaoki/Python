import cx_Oracle
#import oracledb

#obter/cirar uma conexão com o BD Oracle
def getConnection():
    try:
        conn = cx_Oracle.connect(user="RM551456", password="150404", host="oracle.fiap.com.br/orcl")
        print(f'Conexão: {conn.version}')
    except Exception as e:
        print('Erro ao obter uma conexão', e)
    return conn

def select():
    conn = getConnection()
    cursor = conn.cursor()
    sql_query =  "SELECT * FROM CEO_DETAILS"
    cursor.execute(sql_query)
    for result in cursor:
        print(result) 
        conn.commit()

def insert(ceo):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT into CEO_DETAILS values('Steve', 'Jobs', 'Apple', 50)"
    cursor.execute(sql_query)

def update():
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql_query = "UPDATE CEO_DETAILS set AGGE = 50 WHERE first_name = 'Steve' "
        conn.commit()
        conn.close()
    except Exception as e:
        print('Something went wrong {e}')
    finally:
        conn.close()

def delete():
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql_query = "DELETE FROM CEO DETAILS where  AGE = 50"
        cursor.execute(sql_query)
        conn.commit()
        print('CEO removed')
    except Exception as e:
        print('Something went wrong: delete {e}')
    finally:
        conn.close()

def close_connection(conn):
    try:
        conn.close()
        print(f'Connection closed!')
    except Exception as e:
        print(f'Something went wrong: {e}')

print(f'Obtendo os dados do BD')
conn = getConnection()
select()
insert()
select()
update()
select()
close_connection(conn)