from mongoengine import *
import datetime

class Address(EmbeddedDocument):
   address=StringField()
   location=PointField()
     
    
class Website(EmbeddedDocument):
   url=URLField(StringField)	
   

class Specialty(EmbeddedDocument):
   speciality = StringField(max_length=200, required=True)  

class Fecilities(EmbeddedDocument):
   fecility = StringField()
   

class Prices(EmbeddedDocument):
   price=IntField(required=True)
   

class Rating(EmbeddedDocument):	
   rating=DecimalField()

class Hospital(Document):
    name = StringField(max_length=200, required='True')
    address = ListField(EmbeddedDocumentField(Address))
    geo_loc = ListField(PointField(EmbeddedDocumentField(Address)))
    url = ListField(URLField(EmbeddedDocumentField(Website)))
    speciality = ListField(EmbeddedDocumentField(Specialty))
    fecility = ListField(EmbeddedDocumentField(Fecilities))   
    price = ListField(IntField(EmbeddedDocumentField(Prices)))
    rating = ListField(DecimalField(EmbeddedDocumentField(Rating)))
    date_modified = DateTimeField(default=datetime.datetime.now)
    id=StringField(required='true')


