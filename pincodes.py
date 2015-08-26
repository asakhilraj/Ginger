import httplib
import urllib
import urllib2
import json
import sys
import requests
from pprint import pprint
import mongoengine
from mongoengine import*
#from schema import*
import time
import test
import place_id_details

def get_pincodes(placeid):
	global result
	try:
		params={'placeid':placeid, 'key':'AIzaSyCiDyQDBM4827gmqXSDo6X816toHPQ71xU'}
		if(placeid):
			try:
				result=requests.get('https://maps.googleapis.com/maps/api/place/details/json?', params=params)
				if result.ok:
					r=result.json()
                                        last_key=r['result']['address_components']
                                        x=len(last_key)-1
                                        pincode=int(r['result']['address_components'][x]['long_name'])
                                        print ('pincode %d'%pincode)


                        except Exception as e:
                            print (e)

        except Exception as e:
            print ('please enter a valid placeid[%s]'%e)

        return result

#get_pincodes('ChIJUWvMDIuDyzsRRtSN6WL8mcE')



		
