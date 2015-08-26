import csv
import MySQLdb


def upload(file_name):
    r=csv.reader(fp,delimiter=',',quotechar='|')
    for row in r:
        print row
        #split_row=row.slice()
        #number=str(split_row[0])
        #value1=str(split_row[1])
        #value2=str(split_row[2])
        #value3=str(split_row[3])
        #value4=str(split_row[4])
        #enter_list.append((number,value1,value2,value3,value4))
        #print(enter_list)
        
        sql_query=('INSERT INTO `insurance`(`name`) VALUES (%s);')
        cursor.execute(sql_query,row)
        
        print ("Done")

fp=open('insurance.csv','rb')
try:
	global db, cursor
	db=MySQLdb.connect("localhost","root","javabean22","SINGULARITY")
	cursor=db.cursor()

except Exception as e:
    print e

upload(fp)            
db.commit()
cursor.close()
db.close()
