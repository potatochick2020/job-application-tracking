from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):
    client = MongoClient("mongodb+srv://dev:lVS0YnayIPiz9e6C@cluster0.y71di.mongodb.net/?retryWrites=true&w=majority")
    db_handle = client[db_name]
    return db_handle, client
def get_collection_handle(db_handle,collection_name):
    return db_handle[collection_name]