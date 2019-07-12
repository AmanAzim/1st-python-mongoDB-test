import pymongo

#Creating Database
myclient=pymongo.MongoClient('mongodb://localhost:27017/')
mydb=myclient['mymongodatabase']

#checking if database exists
print(myclient.list_database_names())

#######################################################################
#creating first collection
mycol1=mydb["customers"]

#checking if the collection exists
print(mydb.list_collection_names())
#######################################################################

#inserting first record/document in the collection
#mydict={"name":"Aman", "Age":31}
#x=mycol1.insert_one(mydict)
#print(x)
#print('the inserted id=',x.inserted_id)

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
#x=mycol1.insert_many(mylist1)
#print('the inserted id=',x.inserted_ids)


#insert documents with specified ids into a new collection#######################################
mycol2=mydb["clients"]

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
#y=mycol2.insert_many(mylist2)
#print('the inserted id=',y.inserted_ids)
#######################################################################
#check if the collection is created
collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection *customers* exists.")
if "clients" in collist:
    print("The collection *clients* exists.")
#checking if database created
dblist = myclient.list_database_names()
if 'mymongodatabase' in dblist:
    print('database exists')

#######################################################################
#find the first document fo the collection mylist
f1=mycol1.find_one()
print(f1)
f2=mycol2.find_one()
print(f2)

#find all
for x in mycol1.find():
    print(x)
for x in mycol2.find():
    print(x)

#find specific fields of the documents/recirds
#IF we want to print specific field then we have to give its value as 1 and all others need to be 0 but we cannot include the name of all other fileds they all will be 0 automatically however we need to include the "_id" field with its value 0 or 1 if we dont include it it will have the value 1 by default thus it will be visible
for x in mycol2.find({},{ "_id": 0, "name": 1}):
  print(x)

for x in mycol2.find({},{ "address": 1 }):
  print(x)

print("\n\n")
#Searching one particular record
for x in mycol2.find({ "address": "Park Lane 38" }):
    print(x)

print("\n\n")
#to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}:
matches1=mycol2.find({ "address": { "$gt": "S" } })
for x in matches1:
    print(x)

print("\n\n")
#Sort the found resulta. The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction):
for x in mycol2.find().sort("name"):
    print(x)
#sort("name", 1) #ascending
#sort("name", -1) #descending
print("\n\n")
for x in mycol2.find({},{"address":0}).sort("name", -1):
    print(x)

#Delete 1 document(first one if found):
print("\n\n")
mycol2.delete_one({ "address": "Mountain 21" })
for x in mycol2.find({},{"address":0}).sort("name", -1):
    print(x)

#delete from  multiple documents where the address field starts with "M" and letters below
print("\n\n")
d=mycol1.delete_many({"address":{ "$gt": "M" } })
#Deleting all the documents from a collection
d=mycol1.delete_many({})
print(d.deleted_count, "documents deleted")

#To fully drop a collection
# mycol1.drop()


