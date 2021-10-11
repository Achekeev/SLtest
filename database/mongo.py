from pymongo import MongoClient


try:
    client = MongoClient("mongodb://mongodb:27017/")
    #     host="localhost:27017",
    #     serverSelectionTimeoutMS=3000,  # 3 second timeout
    #     username="admin",
    #     password="admin",
    #     connect=False,
    # )
    print(f"Connected to {client}")
    db = client.sltest
    server_type = client.server_info()

except:
    print("Connection rejected")
