/**
	Title: projections.js
    Author: Professor Krasso
    Date: June 21, 2023
    Description: Experiment with building and executing queries in MongoDB.
    Sources Used:
    MongoDB Query Guide
 */

// Writing a query to add a new user to the user's collection.
db.users.insertOne({
  firstName: 'Béla',
  lastName: 'Bartók',
  employeeId: '1013',
  email: 'bvjbartok@gmail.com',
  dateCreated: new Date(),
});

// Writing a query to update Mozart's email address to mozart@me.com.
db.users.updateOne(
  { _id: ObjectId('6488eeab3a72dab146fd71d3') },
  { $set: { email: 'mozart@me.com' } }
);

// Writing a query to prove Mozart's email address was updated.
db.users.findOne({ lastName: 'Mozart' });

// Writing a query to list all documents & using projections to only display firstName, lastName and email fields.
db.users.find({}, { firstName: 1, lastName: 1, email: 1 });
