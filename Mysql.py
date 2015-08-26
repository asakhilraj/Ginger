import MySQLdb
from collections import defaultdict
#import mysql.connector
#from mysql.connector import errorcode

try:
	global db, cursor,DB_NAME,HOSPITAL,PHARMACY,DIAGNOSTIC,INSURANCE,ADDRESS,TABLES
	db=MySQLdb.connect("localhost","root","javabean22")
	cursor=db.cursor()
        DB_NAME='SINGULARITY'
        HOSPITAL={}
        DIAGNOSTIC={}
        PHARMACY={}
        ADDRESS={}
        INSURANCE={}
        TABLES=[]
        TABLES.append(HOSPITAL)
        TABLES.append(DIAGNOSTIC)
        TABLES.append(PHARMACY)
        TABLES.append(ADDRESS)
        TABLES.append(INSURANCE)


        

except Exception as err:
	print (err)



def create_database(cursor):
    try:
	    if(MySQLdb.connect(user='root',passwd='javabean22',db=DB_NAME)):
		    print ('already exists [%s]'%DB_NAME)
		    create_tables(TABLES)
		    
	    else:
		    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
          
    except Exception as err:
        print("Failed creating database: {}".format(err))
        exit(1)




#add_countries=("INSERT INTO countries(id,name,abbrev,time_stamp)VALUES(%d,%s,%s)")    
#add_states=("INSERT INTO states(id,countries_id,name,abbrev,time_stamp)VALUES(%d,%s,%s)")  
#add_districts=("INSERT INTO districts(id,states_id,name,time_stamp)VALUES(%d,%s,%s)")  
#add_cities=("INSERT INTO cities(id,districts_id,name,time_stamp)VALUES(%d,%s,%s)")     
#add_zipcodes=("INSERT INTO pincodes(id,cities_id,pincode,timestamp)VALUES(%d,%d,%d,)")

#def set_tables(name,*args):
#     global table
#     table=defaultdict(list)     
#     for args in args:
#         columns=[]
#         columns.append(args)
#         table[name].append(columns)
#     return table



#set_tables('states','id','countries_id','name','abbrev','time_stamp')
#set_tables('districts','id','sates_id','name','abbrev','time_stamp')
#set_tables('cities','id','district_id','name','abbrev','time_stamp')
#set_tables('pincodes','id','cities_id','pincode','time_stamp')



ADDRESS['countries']=(
"CREATE TABLE `countries`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`name` varchar(20) NOT NULL,"
"`abbrev` varchar (10) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY(`id`)"
") ENGINE=InnoDB")

ADDRESS['states']=(
"CREATE TABLE `states`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
" `countries_id` int(11) NOT NULL,"
"`name` varchar(20) NOT NULL,"
"`abbrev` varchar (20) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `countries_states_ibfk` FOREIGN KEY(`countries_id`)"
"  REFERENCES `countries`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")


ADDRESS['districts']=(
"CREATE TABLE `districts`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`states_id` int(11) NOT NULL,"
"`name` varchar(20) NOT NULL,"
"`abbrev` varchar (20) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `states_districts_ibfk` FOREIGN KEY(`states_id`)"
"  REFERENCES `states`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")


ADDRESS['cities']=(
"CREATE TABLE `cities`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`districts_id` int(11) NOT NULL,"
"`name` varchar(20) NOT NULL,"
"`abbrev` varchar (20) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `districts_cities_ibfk` FOREIGN KEY(`districts_id`)"
"  REFERENCES `districts`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")


ADDRESS['pincodes']=(
"CREATE TABLE `pincodes`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`cities_id` int(11) NOT NULL,"
"`pincode` int(50) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `cities_pincode_ibfk` FOREIGN KEY(`cities_id`)"
"  REFERENCES `cities`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")


HOSPITAL['hospital']=(
"CREATE TABLE `hospital`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`place_id` varchar(50) NOT NULL,"
"`name` varchar(150) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`,`place_id`)"
") ENGINE=InnoDB")

HOSPITAL['hospital_address']=(
"CREATE TABLE `hospital_address`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`hospital_id` int(11)  NOT NULL,"
"`address` varchar(500) NOT NULL,"
"`contact_number` int (50) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `hospital_id_ibfk` FOREIGN KEY (`hospital_id`)"
"REFERENCES `hospital`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")


HOSPITAL['hospital_pincode']=(
"CREATE TABLE `hospital_location`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`hospital_address_id` int (11) NOT NULL,"
"`pincodes`int(50) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `hospital_address_ibfk` FOREIGN KEY(`hospital_address_id`)"
"REFERENCES `hospital_address`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")

HOSPITAL['hospital_type']=(
"CREATE TABLE `hospital_type`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`type` varchar(50) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`)"
") ENGINE=InnoDB")

HOSPITAL['facilities']=(
"CREATE TABLE `facilities`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`facilities` varchar (50) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`)"
") ENGINE=InnoDB")

HOSPITAL['specialities']=(
"CREATE TABLE `specialities`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`specialities` varchar (50) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`)"
") ENGINE=InnoDB")

HOSPITAL['hospital_facilities']=(
"CREATE TABLE `hospital_facilities`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`facilities_id` int (11) NOT NULL,"
"`hospital_id`int(11) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `hospital_facilities_ibfk` FOREIGN KEY(`hospital_id`)"
"REFERENCES `hospital`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")

HOSPITAL['hospital_specialities']=(
"CREATE TABLE `hospital_specialities`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`specialities_id` int (11) NOT NULL,"
"`hospital_id`int(11) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `hospital_specialities_ibfk` FOREIGN KEY(`hospital_id`)"
"REFERENCES `hospital`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")

DIAGNOSTIC['diagnostics_center']=(
"CREATE TABLE `diagnostic_center`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`place_id` varchar(50) NOT NULL,"
"`name` varchar(150) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`,`place_id`)"
") ENGINE=InnoDB")

DIAGNOSTIC['diagnostic_address']=(
"CREATE TABLE `diagnostic_address`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`diagnostic_id` int(11)  NOT NULL,"
"`address` varchar(500) NOT NULL,"
"`contact_number` int (50) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `diagnostic_id_ibfk` FOREIGN KEY (`diagnostic_id`)"
"REFERENCES `diagnostic_center`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")

DIAGNOSTIC['diagnostic_pincode']=(
"CREATE TABLE `diagnostic_location`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`diagnostic_address_id` int (11) NOT NULL,"
"`pincodes`int(50) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `diagnostic_address_ibfk` FOREIGN KEY(`diagnostic_address_id`)"
"REFERENCES `diagnostic_address`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")

DIAGNOSTIC['facilities']=(
"CREATE TABLE `facilities`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`facilities` varchar (50) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`)"
") ENGINE=InnoDB")

DIAGNOSTIC['diagnostic_facilities']=(
"CREATE TABLE `diagnostic_facilities`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`facilities_id` int (11) NOT NULL,"
"`diagnostic_id`int(11) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `diagnostic_facilities_ibfk` FOREIGN KEY(`diagnostic_id`)"
"REFERENCES `diagnostic_center`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")

PHARMACY['pharmacy']=(
"CREATE TABLE `pharmacy`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`place_id` varchar(50) NOT NULL,"
"`name` varchar(150) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`,`place_id`)"
") ENGINE=InnoDB")

PHARMACY['pharmacy_address']=(
"CREATE TABLE `pharmacy_address`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`pharmacy_id` int(11)  NOT NULL,"
"`address` varchar(500) NOT NULL,"
"`contact_number` int (50) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `pharmacy_id_ibfk` FOREIGN KEY (`pharmacy_id`)"
"REFERENCES `pharmacy`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")

PHARMACY['pharmacy_pincode']=(
"CREATE TABLE `pharmacy_location`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`pharmacy_address_id` int (11) NOT NULL,"
"`pincodes`int(50) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `pharmacy_address_ibfk` FOREIGN KEY(`pharmacy_address_id`)"
"REFERENCES `pharmacy_address`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")

INSURANCE['insurance']=(
"CREATE TABLE `insurance`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`name` varchar(150) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`)"
") ENGINE=InnoDB")

INSURANCE['life_insurance_corporation']=(
"CREATE TABLE `life_insurance_corporation`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`insurances_id` int(11) NOT NULL,"
"`hospital_id` int(11) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `life_insurance_network` FOREIGN KEY(`insurances_id`)"
"REFERENCES `insurance`(`id`) ON DELETE CASCADE,"
"CONSTRAINT `life_insurance_network_hospital` FOREIGN KEY(`hospital_id`)"
"REFERENCES `hospital`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")

INSURANCE['sbi_life_insurance']=(
"CREATE TABLE `sbi_life_insurance`("
"`id` int(11) NOT NULL AUTO_INCREMENT,"
"`insurances_id` int(11) NOT NULL,"
"`hospital_id` int(11) NOT NULL,"
"`creation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
"`modification_time` TIMESTAMP,"
"PRIMARY KEY (`id`),"
"CONSTRAINT `sbi_life_insurance_network` FOREIGN KEY(`insurances_id`)"
"REFERENCES `insurance`(`id`) ON DELETE CASCADE,"
"CONSTRAINT `sbi_life_insurance_network_hospital` FOREIGN KEY(`hospital_id`)"
"REFERENCES `hospital`(`id`) ON DELETE CASCADE"
") ENGINE=InnoDB")





def create_tables(table_list):
    db.select_db(DB_NAME)
        
    if(table_list):
        for i in table_list:
            for name,ddl in i.iteritems():
                try:
                    print("Creating table {}: ".format(name))
                    cursor.execute(ddl)

                         
                except Exception as err:
                    print(err)

    else:
        print('kindly enter a DB name')
       
#if (DB_NAME):
#	try:
create_database(cursor)
#	except Exception as e:
#		if(e=='database exists'):
		
		
#create_tables(TABLES)

db.commit()    
cursor.close()
db.close()






