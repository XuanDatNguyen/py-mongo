from pymongo import MongoClient

PASSWORD = "AjqnIWIG9EtT5GDV"

client = MongoClient(
    F"mongodb+srv://james:{PASSWORD}@cluster0.3jh1mek.mongodb.net/?retryWrites=true&w=majority")

students = client.my_db.students
