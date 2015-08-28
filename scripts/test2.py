import MySQLdb

try:
    global db,cursor,DB_NAME
    db=MySQLdb.connect("localhost","root","javabean22")
    cursor=db.cursor()
    DB_NAME='test2'

except Exception as err:
	print (err)


def create_database(cursor):
    try:
       cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format (DB_NAME))
       cursor.close()
       db.close()
    except Exception as err:
        print("Failed creating database: {}[%s]"%err)
        exit(1)

create_database(cursor)


