/*
 Title: Exercise 4.3 - MongoDB Shell
 Author: Professor Krasso
 Date: June 14th, 2023
 Modified By: Jennifer Hoitenga
 Description: Working with the MongoDB shell to build and execute queries.
 Sources Used: 
 WEB 335 mongosh Guide
 WEB 335 GitHub Repository (user.js script)
*/

// Loading the user.js script from week four of the courses GitHub repository
load("user.js")

// Searching for all of the documents in the user’s collection
db.users.find()

// Searching for all users with an email address of jbach@me.com.
db.users.find({email:"jbach@me.com"})

// Searching for all users with the last name of Mozart.
db.users.find({lastName:"Mozart"})

// Searching for all users with the first name of Richard.
db.users.find({firstName:"Richard"})

// Searching for all users with an employee id of 1010.
db.users.find({employeeId:"1010"})
