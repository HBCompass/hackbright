Skills 3: Telemarketer Script Revisited
=======

Introduction
--------
If you recall from [Homework 7](https://github.com/hackbrightacademy/Homework/tree/master/Homework07), our marketing department is running a promotion for
all customers who have placed an order for over 20 Watermelons.

They want to make sure all eligible customers know about it, so
they've asked the Telemarketing Department to start placing calls.

In [Homework 7](https://github.com/hackbrightacademy/Homework/tree/master/Homework07), the 'call.py' script used a pair of .csv files to get the data on the customers and the orders.

Now, we can harness the power of databases to do things the "right" way!  Update the 'call.py' script.  Some functions have been placed in the script to give you a general idea of the flow we are looking for.

Some hints to get you started:

* The database relationships are:
** customers have orders
** orders have order_items (An order may be for more than one type of melon)

* Start by writing the query to just return one customer record, then expand it to filter for only the customers who have ordered over 20 melons.

* The database does not currently have a field to track the last time a customer was called.  You'll have to add it.

