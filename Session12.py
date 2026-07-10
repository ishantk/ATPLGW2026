"""
    1. Register on MongoDB Atlas (GCP/AWS/Azure)
    2. MongoDB User -> ROLE ->Admin
    3. IP Whitelisiting -> 0.0.0.0/0
    4. Create DataBase with a collection
    5. pip install "pymongo[srv]" (ensure 1. internet 2. your venv selected)
    6. Run the sample code
"""


from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://atpl:atpl@cluster0.eh8zx.gcp.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)