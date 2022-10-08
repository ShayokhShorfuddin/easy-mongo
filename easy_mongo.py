import pymongo
from pymongo import MongoClient

# Getting A Cluster
def cluster(url:str, password:str):
    # Replacing the <password> with given password
    url = url.replace("<password>", password)
    
    # Connecting...
    cluster = MongoClient(url)
    return cluster


# Getting A Database From A Cluster
def database(cluster, name:str):
    return cluster[name]


# Getting A Collection From A Database
def collection(database, name:str):
    return database[name]


# Get A List Of Collections In A Database
def collections(database):
    return database.list_collection_names()


# Get Amount (Integer) Of Entires In A Collection
def entires_amount(collection):
    return collection.count_documents({})

# Get All The Entries In A Collection
def inspect(collection):
    result = []
    
    # Gathering All The Entries And Adding..
    for i in collection.find():
        result.append(i)
    
    return result


# Find An Entry Using Given Dict
def search(collection, look_for:dict):
    return collection.find_one(look_for)


# Delete An Entry Using Given Dict
def delete(collection, look_for:dict):
    return collection.delete_one(look_for)


# Delete Multiple Entries Using Given Datas
def bulk_delete(collection, data:list):
    return collection.delete_many(data)


# Delete A Collection
def terminate(database, collection_name):
    return database.drop_collection(collection_name)


# Delete All The Entires In A Collection (But The Collection Itself Won't Delete)
def purify(collection):
    return collection.delete_many({})


# Inserting New Data (Dict) To A Collection
def upload(collection, data:dict):
    return collection.insert_one(data)


# Inserting Multiple Data (Dicts) To A Collection
def upload_all(collection, data:list):
    return collection.insert_many(data)


# Update An Entry Using Given Dict
def update(collection, operator:str , target:dict, update_to:dict):
    # Checking The Given Operator
    
    # Set (Sets the value of a field in a document)
    if operator.lower() == "set":
        return collection.update_one(target, {"$set": update_to})
    
    # More will be added later if necessary


# Update Multiple Entry Using Given Dict
def bulk_update(collection, operator:str , target:dict, update_to:dict):
    # Checking The Given Operator
    
    # Set (Sets the value of a field in a document)
    if operator.lower() == "set":
        return collection.update_many(target, {"$set": update_to})
    
    # More will be added later if necessary





mycls = cluster("mongodb+srv://shay:<password>@cluster0.sltbe.mongodb.net/?retryWrites=true&w=majority", "12345")
mydb = database(mycls, "test")
mycol = collection(mydb, "test")