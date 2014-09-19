Skills 3: Telemarketer Script Revisited
=======

Introduction
--------
If you recall from [Homework 7](https://github.com/hackbrightacademy/Homework/tree/master/Homework07), our telemarketing team uses a script to call customers for a promotion. The 'call.py' script used a pair of .csv files to get the data on the customers and the orders.

Now, we can harness the power of databases to do things the "right" way! We're going to create a database based on the csv files from the homework and update the 'call.py' script so that it connects to our new database.

* Create a new database with tables to hold customers and orders
* Write a python script to load the data from the CSV files and INSERT it into your database
* Copy the call.py script from the homework and update it to connect to the database and find the next customer to call
* Update the database to mark customers as "called" with the current date.

Some hints to get you started:

* Refer back to [SQL lesson](https://github.com/hackbrightacademy/sql_lesson) for how to create a table and insert into it.
* Write a separate script to "seed" your database. Don't be afraid to delete your database if you get something wrong.
* When you get to querying for your next customer, start by ignoring the part about 20 watermelons, and just return any customer.


Extra Credit
-------------

* Update your script to only return customers who have ordered more than 20 watermelons.
* Have your get_next_customer() function return the customer data as an instance of a Customer class.
* Update your script so it returns customers who have not been called in the last 30 days. (THIS IS HARD, AND MAY REQUIRE REFORMATTING YOUR DATABASE)


