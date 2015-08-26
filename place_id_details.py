import pincodes
import MySQLdb

db=MySQLdb.connect("localhost","root","javabean22","SINGULARITY")
cursor=db.cursor()

def get_entity_id(name,place_id):
	try:
		if(name=='hospital'):
			sql_query2=('SELECT `id` FROM `hospital` WHERE `place_id=%s`')
			cursor.execute(sql_query2,(place_id,))
			x=cursor.fetchone()
			entity_id=x
	        elif(name=='pharmacy'):
			sql_query3=('SELECT `id` FROM `pharmacy` WHERE `place_id=%s`')
			cursor.execute(sql_query3,(place_id,))
			x=cursor.fetchone()
			entity_id=x
		elif(name=='diagnostic'):
			sql_query2=('SELECT `id` FROM `diagnost_center` WHERE `place_id=%s`')
			cursor.execute(sql_query2,(place_id,))
			x=cursor.fetchone()
			entity_id=x
		else:
			print('can not understand name %s'%name)
        
	except Exception as err:
		print err
        return entity_id

def get_address_id(entity_id,name):
	try:
		if(name=='hospital'):
			sql_query2=('SELECT `id` FROM `hospital_address` WHERE `hospital_id=%s`')
			cursor.execute(sql_query2,(entity_id,))
			x=cursor.fetchone()
			address_id=x
	        elif(name=='pharmacy'):
			sql_query3=('SELECT `id` FROM `pharmacy_address` WHERE `pharmacy_id=%s`')
			cursor.execute(sql_query3,(entity_id,))
			x=cursor.fetchone()
			address_id=x
		elif(name=='diagnostic'):
			sql_query2=('SELECT `id` FROM `diagnost_address` WHERE `diagnostic_id=%s`')
			cursor.execute(sql_query2,(entity_id,))
			x=cursor.fetchone()
			address_id=x
		else:
			print('can not understand name %s'%name)
        
	except Exception as err:
		print err
        return address_id
	



def get_place_id(name):
	try:
		global place_id,entity_id,address_id
		sql_query=('SELECT `place_id` from %s')
		cursor.execute(sql_query,name)
		place_list=cursor.fetchall()
		for x in place_list:
			place_id=''.join(x)
			result=(get_pincodes(place_id))
			if result.ok:
				r=result.json()
				last_key=r['result']['address_components']
				x=len(last_key)-1
				pincode=int(r['result']['address_components'][x]['long_name'])
				print ('pincode %d'%pincode)
				entity_id=(get_entity_id(name,place_id))
				address_id=(get_address_id(entity_id))




