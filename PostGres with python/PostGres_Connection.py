import psycopg2
from config import config
# connection = psycopg2.connect(host="localhost", database="master",port="5432",user="postgres",password="arslan")
# print("z")

def connect():
    connection = None
    try:
        params = config()
        print("Connecting to the postgres Databse....")
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        print("PostgreSQL database version: ")
        cursor.execute("Select version()")
        db_version = cursor.fetchone()
        print(db_version)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database Connection Terminated')



if __name__ == "__main__":
    connect()
