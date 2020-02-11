import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://dbUser:dbUserPassword@cluster0-5nzly.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["testdb"]
collection = db["testCollection"]

post0 = {"_id": 0, "className": "sampleClass", "startTime": "12:00 PM", "professor": "sampleProfessor", "building": "Bascom Hall", "choice": 'g'}
post1 = {"_id": 1, "className": "sampleClass", "startTime": "12:00 PM", "professor": "sampleProfessor", "building": "Bascom Hall", "choice": 'm'}
post2 = {"_id": 2, "className": "sampleClass", "startTime": "12:00 PM", "professor": "sampleProfessor", "building": "Bascom Hall", "choice": 'b'}

results = collection.find({"choice":'g'}) #returns all results that have choice as 'g', not just one
#print(results) this gives a reference to a cursor object
for result in results:
    #print(result) prints all the data sets from the dictionary, basically the whole post
    print(result["_id"])

oneResult = collection.find_one({"_id":1})
print(oneResult)

collection.delete_one({"_id":2}) #only deletes one, is best to use ID to set
collection.insert_one(post2) #inserts it back in, for testing purposes

collection.delete_many({"className":"sampleClass"}) #empty {} with delete_many() deletes everything
collection.insert_many([post0, post1, post2]) #inserts them all back for testing purposes

collection.update_one({"_id": 2}, {"$set":{"choice":'g'}})
collection.update_many({"professor":"sampleProfessor"}, {"$set":{"building":"Van Vleck Hall"}})

print(collection.count_documents({"choice":'g'})) #prints how many posts/documents are within the collection, empty brackets counts all documents
