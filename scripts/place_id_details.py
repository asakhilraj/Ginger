import pincodes
import MySQLdb
import re

db=MySQLdb.connect("localhost","root","javabean22","SINGULARITY")
cursor=db.cursor()

def get_entity_id(name,place_id):
	try:
		if(name=='hospital'):
			sql_query2=('SELECT `id` FROM `hospital` WHERE `place_id`=%s')
			cursor.execute(sql_query2,(place_id,))
			x=cursor.fetchone()
			entity_id=x
	        elif(name=='pharmacy'):
			sql_query3=('SELECT `id` FROM `pharmacy` WHERE `place_id`=%s')
			cursor.execute(sql_query3,(place_id,))
			x=cursor.fetchone()
			entity_id=x
		elif(name=='diagnostic_center'):
			sql_query2=('SELECT `id` FROM `diagnostic_center` WHERE `place_id`=%s')
			cursor.execute(sql_query2,(place_id,))
			x=cursor.fetchone()
			entity_id=x
		else:
			print('can not understand name %s'%name)
		
		if(entity_id==None):
			entity_id=cursor.fetchone()
		else:
			pass

        
	except Exception as err:
		print err
        return entity_id

def get_address_id(entity_id,name):
	try:
		if(name=='hospital'):
			sql_query2=('SELECT `id` FROM `hospital_address` WHERE `hospital_id`=%s')
			cursor.execute(sql_query2,(entity_id,))
			x=cursor.fetchone()
			address_id=x
	        elif(name=='pharmacy'):
			sql_query3=('SELECT `id` FROM `pharmacy_address` WHERE `pharmacy_id`=%s')
			cursor.execute(sql_query3,(entity_id,))
			x=cursor.fetchone()
			address_id=x
		elif(name=='diagnostic_center'):
			sql_query2=('SELECT `id` FROM `diagnostic_address` WHERE `diagnostic_id`=%s')
			cursor.execute(sql_query2,(entity_id,))
			x=cursor.fetchone()
			address_id=x
		else:
			print('can not understand name %s'%name)
		
		if(address_id==None):
			address_id=cursor.fetchone()
		else:
			pass
        
	except Exception as err:
		print err
        return address_id
	



def get_place_id(name):
	try:
		global place_id,entity_id,address_id
		print('fetching place_ids for %s'%name)
		if(name=='hospital'):
			sql_query=('SELECT `place_id` FROM `hospital`')
		elif(name=='pharmacy'):
			sql_query=('SELECT `place_id` FROM  `pharmacy`')
		elif(name=='diagnostic_center'):
			sql_query=('SELECT `place_id` FROM `diagnostic_center`')
		else:
			print('Didn\'t get the name %s'%name)
		
		print(sql_query,name) 
		cursor.execute(sql_query,)
		place_tuple=cursor.fetchall()
		for x in place_tuple:
			place_id=''.join(x)
			#m=re.search(r'\s+',place_id_old.unicode_markup)
			#place_id=m.group()
			str(place_id)
			print('place_id=%s'%place_id)
			pincode=(pincodes.get_pincodes(place_id))
			if(pincode):
			#	r=result.json()
			#	last_key=r['result']['address_components']
			#	x=len(last_key)-1
			#	pincode=int(r['result']['address_components'][x]['long_name'])
			#	print ('pincode %d'%pincode)
				entity_id=(get_entity_id(name,place_id))
				address_id=(get_address_id(entity_id,name))
				print('entity_id={0},address_id={1}' .format(entity_id,address_id))
				try:
					if(name=='hospital'):
						sql_query2=('INSERT INTO `hospital_location`(`hospital_address_id`,`pincodes`) VALUES (%s,%s)')
					elif(name=='pharmacy'):
						sql_query2=('INSERT INTO `pharmacy_location`(`pharmacy_address_id`,`pincodes`) VALUES (%s,%s)')
					elif(name=='diagnostic_center'):
						sql_query2=('INSERT INTO `diagnostic_location`(`diagnostic_address_id`,`pincodes`) VALUES (%s,%s)')
					else:
						print('Didn\'t get the name %s'%name)
					
					print (sql_query2,(address_id,(pincode,)))
					cursor.execute(sql_query2,(address_id,pincode))
				except Exception as err:
					print err
			        
				print('NEXT')

			else:
				print('something went wrong with pincodes %s'%result)
	except Exception as e:
		print e


get_place_id('diagnostic_center')
db.commit()
cursor.close()
db.close()

