import httplib
import urllib
import urllib2
import json
import sys
import requests
from pprint import pprint
#import mongoengine
#from mongoengine import*
#from schema import*
import time
import test
#import DBstore
import csv
import os


def get_bounds(location):
    global Coordfinder,maxlat,maxlng,minlat,minlng
    try:
        params={'address':location, 'key':'AIzaSyCiDyQDBM4827gmqXSDo6X816toHPQ71xU'}
        if(location):
            try:
                CoordFinder=requests.get('https://maps.googleapis.com/maps/api/geocode/json?', params=params)
                if CoordFinder.ok:	
                    r=CoordFinder.json()
                    maxlat=str(r['results'][0]['geometry']['bounds']['northeast']['lat'])
                    maxlng=str(r['results'][0]['geometry']['bounds']['northeast']['lng'])
                    minlat=str(r['results'][0]['geometry']['bounds']['southwest']['lat'])
                    minlng=str(r['results'][0]['geometry']['bounds']['southwest']['lng'])
            except Exception as e:
                print (e)
    except Exception as e:
        print ('please enter a valid address[%s]'%e)

    return maxlat,maxlng,minlat,minlng     


#def write(result_list,*vartuple):
#    print('Creating the result file') 
#        
#    try:
#       connect('raw')
#       print ('Connected to the database.')
#       for i in result_list:
#            post=Hospital(name=result_list[i].get('results').get('name'))
#            address=Address(address=result_list[i].get('results').get('vicinity'))
#            address.location=result_list[i].get('results').get('geometry',{}).get('location').get('lng',None), result[i].get('geometry',{}).get('location').get('lat',None)
#	    post.id=result_list[i].get('results').get('geometry',{}).get('id')
#            post.save()
#
#    except Exception as r:
#        print('Something went wrong! can\'t tell what?[%s]'%r)           
	           	
def sav_json(response):
    try:
        if(response.status_code==200):
            if(os.path.exists('/home/akhil/Documents/Ginger/response_diagnostic.txt')):
                fp=open('response_diagnostic.txt','a')
                fp.write(response.content)
            else:
                fp=open('response_diagnostic.txt','w+')
                fp.write(response.content)
    
        else:
            return 0
    except Exception as e:
        print e


def url(lat,lng, page_token = None):
    global count,result_list,response
    result_list=[]
    params={'key': 'AIzaSyAtoajHNUWTNc3cHCHYE5a9v1JY3gk0ALc','radius':'1000',
            'types':'diagnostic centre'}
    #print ('all ok till here')
    if page_token:
        params.update(page_token = page_token)
    try:
        #print('good here too')
        if(count<10):
            response=requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?"\
                    +"&location="+lat+','+lng, params=params)
            if response:
                print('these are the params',params)
                print response.url
                print ('number of requests [%d]' %count)
                count+=1
                result=response.json()
                if result.get('results',[]):
                    print ('got the result')
                    #pprint(result)
                
                else:
                    print ('empty result')
                    
                status=str(result.get('status',None))
                print("the status is %s" %status)
                if (status=='OK'):
                    sav_json(response)
                    page_token= result .get('next_page_token',None)
                    print('------------page_token:[%s]'%page_token)
                    result_list.append(result)
                    #for r in result_list:
                    #    print ("this is the list:%s" %r)
                        

                    if page_token:
                        print('page token found----------[%s]'%type(page_token))
                        time.sleep(600)
                        for r in url(lat,lng,page_token = str(page_token)): 
                            result_list.append(r)
                            
            else: 
                response=''
        else:
            print ("count exceeded [%d]" %count)
            return result_list,response
            exit(1)

    except Exception as a:
        print ('error here [%s]'%a)
    return result_list,response

def run_ginger():
    global count
    count=0
    get_bounds('kachiguda')
    new_coords=test.bounds_to_coords(maxlat,maxlng,minlat,minlng)
    for x in new_coords:
        if (count<10):
            lat=str(x.get('lat',None))
            lng=str(x.get('lng',None))
            print('calling url for %s,%s'%(lat,lng))
            print count
            url(lat,lng)


#def write_into_csv(result_list):
#    global res_list
#    res_list=result_list
#    f=open('result_obj.txt','w')
#    with open('result_obj.csv','r+') as csvfile:
#        result_write=csv.writer(csvfile, delimiter=' ',
#                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
#        for x in res_list:
#            x_list=str(x.get('results'))
#            result_write.writerow(x_list)
#            f.write(x_list)
#            print x_list




run_ginger()       
#write_into_csv(result_list)



        

