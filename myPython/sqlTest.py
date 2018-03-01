from sqlobject import *
import sys,os

db_filename=os.path.abspath('data.db')
if os.path.exists(db_filename):
    print db_filename + " exists"
    os.unlink(db_filename)
# mysql://user:password@host/database
# mysql://host/database?debug=1
# postgres://user@host/database?debug=&cache=
# postgres:///full/path/to/socket/database
# postgres://host:5432/database
# sqlite:///full/path/to/database
# sqlite:/C:/full/path/to/database
# sqlite:/:memory:    
connection_string = 'sqlite:' + db_filename
connection = connectionForURI(connection_string)
sqlhub.processConnection = connection

class Person(SQLObject):

    personID=IntCol(alternateID=True,dbName='person_ID')
    firstName = StringCol()
    middleInitial = StringCol(length=1, default=None)
    lastName = StringCol()
    age = IntCol(default=30)
    addresses = MultipleJoin('Address',joinColumn='person_ID_FK')
    
class Address(SQLObject):
    
    street = StringCol()
    city   = StringCol()
    state = StringCol(length=5,default=None)
    persons = ForeignKey("Person", dbName = 'person_ID_FK')    
    
Person.createTable()
Address.createTable()
Address._connection.debug = True
Person(personID=1,firstName="Wang",lastName="Hui")
Li=Person(personID=2,firstName="Li",lastName="Hui")
Address(street="Shanghai Street",city='Beijing',persons=2)
Address(street="Suzhou Street",city='Shsanghai',persons=2)
print Li.addresses[0].city 
print Li.id
print Li 
print Li.addresses
print "\n"
Person(personID=3,firstName="Wang",lastName="Long")

wang = Person.selectBy(firstName="Wang")
print wang
wanglist = list(wang)
for item in wanglist:
    print item.firstName,item.lastName

li = Person.byPersonID(1)
print li.id,li.personID,li.firstName
print Person.byPersonID(2).addresses
