from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
Database = ""

connection_string = f"""mongodb+srv://shaurabhsaha:{password}@tutorial.bsuy9e6.mongodb.net/?retryWrites=true&w=majority"""

client = MongoClient(connection_string)

dbs = client.list_database_names()
print(dbs)

test_db = client["test"] # client.test
# ['test', 'admin', 'local']

collections = test_db.list_collection_names()
print(collections)
# ['test']

def insert_test_doc():
    collection = test_db.test
    test_document = {
        "name": "SS",
        "type": "Test"
    }
    # collection.insert_one(test_document)
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id) # 643a6c11957cc5925b92ee62 --> BSON object



production = client.production # Creates DB id not exist
person_collection = production.person_collection # creates collection if not exists

def create_documents():
    first_names = ["Tim","Sarah","Jennifer","Jose","Brad","Allen"]
    last_names = ["Ruscica","Smith","Bart","Cater","Pit","Geral"]
    ages = [21,40,23,19,34,67]

    docs = []

    for first_name,last_name,age in zip(first_names,last_names,ages):
        doc = {"first_name":first_name, "last_name":last_name, "age":age}
        # person_collection.insert_one(doc)
        docs.append(doc) 
    
    person_collection.insert_many(docs)

printer = pprint.PrettyPrinter()
 
def find_all_people():
    people = person_collection.find()

    for person in people:
        printer.pprint(person)

def find_tim():
    tim = person_collection.find_one({"first_name":"Tim"})
    printer.pprint(tim)

def count_all_people():
    # count = person_collection.find().count()
    count = person_collection.count_documents(filter={})
    print("Number of people:",count)

def get_person_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)
    person = person_collection.find_one({"_id":_id})
    printer.pprint(person)


def get_age_range(min_age, max_age):
    query = {"$and": [
            {"age": {"$gte":min_age}},
            {"age": {"$lt":max_age}}
        ]}
    
    people = person_collection.find(query).sort("age")
    for person in people:
        printer.pprint(person)

def project_columns():
    columns = {"_id":0,"first_name":1,"last_name":1}
    people = person_collection.find({}, columns)
    for person in people:
        printer.pprint(person)

def update_person_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)

    all_updates = {
        "$set" : {"new_field": True},
        "$inc": {"age":1},
        "$rename": {"first_name":"first","last_name":"last"}

    }
    person_collection.update_one({"_id":_id},all_updates)

    # person_collection.update_one({"_id":_id},{"$unset":{"new_field":{}}})


def replace_one(person_id):
    from bson.objectid import ObjectId
    _id = ObjectId(person_id)

    new_doc = {
        "first_name": "new first name",
        "last_name": "new last name",
        "age": 100
    }

    person_collection.replace_one({"_id":_id},new_doc)

insert_test_doc()
create_documents()
find_all_people()
find_tim()
count_all_people()
get_person_by_id("643a6e241912dda2456a6370")
get_age_range(20,35)
project_columns()
update_person_by_id("643a6e241912dda2456a636e")
replace_one("643a6e241912dda2456a636e")
