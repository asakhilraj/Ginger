import MySQLdb
import json
import re

try:
	global db, cursor,result,rl
	db=MySQLdb.connect("localhost","root","javabean22","SINGULARITY")
	cursor=db.cursor()
	result=open('response_json2.txt','r')
	FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
	WHITESPACE = re.compile(r'[ \t\n\r]*', FLAGS)
        
except Exception as err:
	print (err)

def store_in_hospital(name,place_id,address):
    print("got a hospital %s"%name)
    sql_query=('INSERT INTO `hospital` (`name`,`place_id`) VALUES (%s,%s)')
    cursor.execute(sql_query,(name,place_id))
    print("Inserted into hospital {0} {1}".format(name,place_id))
    sql_query2=('INSERT INTO `hospital_address`(`hospital_id`,`address`) VALUES(%s,%s)')
    sub_query2=('SELECT `id` from hospital where `place_id`=%s')
    print sub_query2
    #print ("place_id=")
    #print(type(place_id))
    cursor.execute(sub_query2,(place_id,))
    x=cursor.fetchone()
    hid=x
    #print(sql_query2,(hid,address))
    #print sql_query2
    #print("address=")
    #print(type(address))
    cursor.execute(sql_query2,(hid,address))
    print('Address of the hospital inserted')
    
    return 0

def store_in_pharmacy(name,place_id,address):
    print("got a pharmacy %s"%name)
    sql_query=('INSERT INTO `pharmacy` (`name`,`place_id`) VALUES (%s,%s)')
    cursor.execute(sql_query,(name,place_id))
    print("Inserted into pharmacy {0} {1}".format(name,place_id))
    sql_query3=('INSERT INTO `pharmacy_address`(`pharmacy_id`,`address`) VALUES(%s,%s)')
    sub_query3=('SELECT `id` from pharmacy where `place_id`=%s')
    print sub_query3
    print("place_id=")
    print(type(place_id))
    cursor.execute(sub_query3,(place_id,))
    x=cursor.fetchone()
    pid=x
    print sql_query3
    print("address=")
    print(type(address))
    cursor.execute(sql_query3,(pid,address))
    print('Address of the pharmacy inserted')

    return 0

def store_in_diagnostic(name,place_id,address):
    print("got a diagnostic center %s"%name)
    sql_query=('INSERT INTO `diagnostic_center` (`name`,`place_id`) VALUES (%s,%s)')
    cursor.execute(sql_query,(name,place_id))
    print("Inserted into diagnostic center {0} {1}".format(name,place_id))
    sql_query4=('INSERT INTO `diagnostic_address`(`diagnostic_id`,`address`) VALUES(%s,%s)')
    sub_query4=('SELECT `id` from diagnostic_center where `place_id`=%s')
    print sub_query4
    print("place_id=")
    print(type(place_id))
    cursor.execute(sub_query4,(place_id,))
    x=cursor.fetchone()
    did=x
    print sql_query4
    print("address=")
    print(type(address))
    cursor.execute(sql_query4,(did,address))
    print('Address of the diagnostic center inserted')

    return 0

def check_hospital(x,name):
    if(x=='Hospital'):
        print('Hospital caught %s'%name)
        #store_in_hospital(name,place_id,address)
    elif(x=='hospital'):
	print('hospital caught %s'%name)
        #store_in_hospital(name,place_id,address)
    elif(x=='hospitals'):
	print('hospitals caught %s'%name)
        #store_in_hospital(name,place_id,address)
    elif(x=='Hospitals'):
	print('Hospitals caught %s'%name)
        #store_in_hospital(name,place_id,address)
    else:
        return 0

    
    return 1

def check_pharmacy(x,name):
    if(x=='store'):
	print('store caught %s'%name)
        #store_in_pharmacy(name,place_id,address)
    elif(x=='Store'):
        print('sotre caught %s'%name)
        #store_in_pharmacy(name,place_id,address)
    elif(x=='Medicals'):
        print('Medicals caught %s'%name)
        #store_in_pharmacy(name,place_id,address)
    elif(x=='MedPlus'):
        print('MedPlus caught %s'%name)
        #store_in_pharmacy(name,place_id,address)
    elif(x=='medicals'):
        print('medicals caught %s'%name)
        #store_in_pharmacy(name,place_id,address)
    elif(x=='shop'):
        print('shop caught %s'%name)
        #store_in_pharmacy(name,place_id,address)
    elif(x=='Shop'):
        print('Shop caught %s'%name)
        #store_in_pharmacy(name,place_id,address)
    elif(x=='stores'):
        print('stores caught %s'%name)
        #store_in_pharmacy(name,place_id,address)
    elif(x=='Stores'):
	print('Stores caught %s'%name)
        #store_in_pharmacy(name,place_id,address)
    elif(x=='pharmacy'):
	print('pharmacy caught %s'%name)
        #store_in_pharmacy(name,place_id,address)
    elif(x=='Pharmacy'):
	print('Pharmacy caught %s'%name)
        #store_in_pharmacy(name,place_id,address)
    else:
        return 0
   
    return 1


def check_diagnostic(x,name):
    if(x=='Diagnostics'):
        print('Diagnostics caught %s'%name)
        #store_in_diagnostic(name,place_id,address)
    elif(x=='diagnostic'):
        print('diagnostic caught %s'%name)
        #store_in_disgnostic(name,place_id,address)
    elif(x=='diagnostics'):
        print('diagnostics caught %s'%name)
        #store_in_diagnostic(name,place_id,address)
    elif(x=='Diagnostic'):
        print('diagnostic caught %s'%name)
        #store_in_diagnostic(name,place_id,address)
    else:
        return 0

    return 1

def check_name(name,place_id,address):
	try:
                chk_name=name
		checked_name=[]
                start_check=chk_name.split()
		for x in start_check:
                    if(check_hospital(x,chk_name)):
                        store_in_hospital(name,place_id,address)
                        break
                    elif(check_pharmacy(x,chk_name)):
                        store_in_pharmacy(name,place_id,address)
                        break
                    elif(check_diagnostic(x,chk_name)):
                        store_in_diagnostic(name,place_id,address)
                        break
                    else:
			checked_name.append(x)
	
	        if(checked_name==start_check):
			 store_in_hospital(name,place_id,address)
		else:
		    print('name_check worked')
            
	except Exception as e:
		print e
        
        return 1        


def store_in_db(name,place_id,address):
	try:
                global s_name,s_place_id,s_address
                s_name=name
                s_place_id=place_id
                s_address=address
		if(check_name(s_name,s_place_id,s_address)):
                      print('Done')  
		#	store_in_hospital(name,place,address)

		else:
                    print('Something went wrong in storing')
			
	except Exception as err:
		print(err)
		pass

	
	return 0


#def print_json(result):
#	for r in result:
#		
#		for i in r_list:
#			print i


class ConcatJSONDecoder(json.JSONDecoder):
    def decode(self, s, _w=WHITESPACE.match):
       s_len = len(s)
       objs = []
       end = 0
       while end != s_len:
            obj, end = self.raw_decode(s, idx=_w(s, end).end())
            end = _w(s, end).end()
            objs.append(obj)
       return objs

#def  write_to_csv():



def parse_results(result):
	r_list=json.load(result, cls=ConcatJSONDecoder)
	for i in r_list:
	   r_dict=i
	   res_list=r_dict['results']
	   for a in res_list:
		   latitude=str(a['geometry']['location']['lat'])
		   longitude=str(a['geometry']['location']['lng'])
		   name=str(a['name'])
		   place_id=str(a['place_id'])
		   vicinity=str(a['vicinity'])
                   print("calling store_in_DB for {0},{1}".format(name,place_id))
		   store_in_db(name,place_id,vicinity)


parse_results(result)
db.commit()
cursor.close()
db.close
			






