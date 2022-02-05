from pymongo import MongoClient
import certifi

def get_db_handle():
    url = "mongodb+srv://Goopboss:12345@cluster0.o4rex.mongodb.net/sample_airbnb?retryWrites=true&w=majority"
    ca = certifi.where()
    client = MongoClient(url, tlsCAFile=ca)

    db_handle = client.sample_airbnb.listingsAndReviews

    return db_handle