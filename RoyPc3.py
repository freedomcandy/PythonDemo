import pymongo

conn = pymongo.MongoClient(host="127.0.0.1", port=27017)
db = conn['RoyDB']
print(db.collection_names())
collect = db['JKXY']
information = {"name": "test001", "age": "25"}
information_id = collect.insert(information)
print(information_id)