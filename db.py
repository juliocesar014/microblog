from pymongo import MongoClient

client = MongoClient('mongodb+srv://julio-microblog:julio-microblog@cluster0.r1we7ef.mongodb.net/test')
db = client.microblog
