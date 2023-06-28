""" Title: hoitenga_usersp1.py
    Author: Jennifer Hoitenga
    Date: 04/23/2023
    Description: Exercise 6.3 Python with MongoDB
"""

""" Import the MongoClient """
from pymongo import MongoClient

""" Build a connection string """
client = MongoClient('mongodb+srv://web335_user:s3cr3t@bellevueuniversity.g473hiy.mongodb.net/web335DBretryWrites=true&w=majority')
print(client)

""" Adding a blank line for readability."""
print()

""" Configure a variable to access the web335 database """
db = client['web335DB']

""" Display all documents in the user collection. """
print('Display all documents in the users collection:')
for user in db.users.find():
    print(user)

""" Adding a blank line for readability."""
print()

""" Display a document where the employeeId is 1011. """
print('Display Employee ID 1011:')
print(db.users.find_one({'employeeId': '1011'}))

""" Adding a blank line for readability."""
print()

""" Display a document where the lastName is Mozart. """
print('Display user with the lastName of Mozart:')
print(db.users.find_one({'lastName': 'Mozart'}))