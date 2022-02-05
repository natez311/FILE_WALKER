#settings.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv('DB_URL') #create a .env file with your mongodb url to connect and store the variable as DB_URL
# database link
db_client = MongoClient(DATABASE_URL)
# databaseclient on MongoDB
db = db_client["admin"] #set your database name here
collection = db["FILE_DATABASE"] #set your collection name here