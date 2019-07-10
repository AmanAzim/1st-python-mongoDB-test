import pymongo

#Creating Database
myclient=pymongo.MongoClient('mongodb://localhost:27017/')
mydb=myclient['mymongodatabase']

#checking if database exists
print(myclient.list_database_names())

#######################################################################
#creating first collection
mycol=mydb["customers"]

#checking if the collection exists
print(mydb.list_collection_names())
#######################################################################

#inserting first record/document in the collection
mydict={"name":"Aman", "Age":31}
x=mycol.insert_one(mydict)
print(x)
print('the inserted id=',x.inserted_id)

#insert multiple records/documents
mylist1 = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
x=mycol.insert_many(mylist1)
print('the inserted id=',x.inserted_ids)

#insert documents with specified ids into a new collection
mycol=mydb["clients"]

mylist2 = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
x=mycol.insert_many(mylist2)
print('the inserted id=',x.inserted_ids)

#######################################################################
#check if the collection is created
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")

#checking if database created
dblist=myclient.list_database_names()
if 'mymongodatabase' in dblist:
    print('database exists')