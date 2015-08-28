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
#import place_id_details

def get_pincodes(placeid):
	global result,pincode
	try:
                print('get_pincodes got called with place_id %s'%placeid)
		params={'placeid':placeid, 'key':'AIzaSyCiDyQDBM4827gmqXSDo6X816toHPQ71xU'}
                print  params
		if(placeid):
			try:
                                print ('fetching the pincodes')
                                result=requests.get('https://maps.googleapis.com/maps/api/place/details/json?', params=params)
                                print('got the pincodes')
				#print result
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
        
        if(pincode):
            return pincode
        else:
            return 0

#get_pincodes('ChIJUWvMDIuDyzsRRtSN6WL8mcE')



		
