""" Title: hoitenga_usersp2.py
    Author: Jennifer Hoitenga
    Date: July 5, 2023
    Description: Exercise 7.3 Python with MongoDB
    Sources Used:
    Learn Python in One Hour by Programming with Mosh YouTube
    WEB 335 Python Guide
"""

#Import the MongoClient
from pymongo import MongoClient

# Importing Date and Time
import datetime

# Build a connection string
client = MongoClient('mongodb+srv://web335_user:s3cr3t@bellevueuniversity.g473hiy.mongodb.net/web335DBretryWrites=true&w=majority')
db = client['web335DB']
print(client)

# Add a blank line for readability
print()

# Create a new user document
jennifer = {
    "firstName": "Jennifer",
    "lastName": "Hoitenga",
    "employeeId": "867",
    "email": "jen@hotmail.com",
    "dateCreated": datetime.datetime.now()
}

# Inserting the new document into the database
jenniferUserId = db.users.insert_one(jennifer).inserted_id

# Display the newly created document
print(db.users.find_one({"employeeId": "867"}))

# Add a blank line for readability
print()

# Update the email address of the document
db.users.update_one(
    {"employeeId": "867"},
    {"$set": {"email": "jen@yahoo.com"}}
)

# Display the updated document
print(db.users.find_one({"employeeId": "867"}))

# Add a blank line for readability
print()

#Delete the document
result = db.users.delete_one({"employeeId": "867"})

#Prove the document was deleted
print(db.users.find_one({"employeeId": "867"}))
