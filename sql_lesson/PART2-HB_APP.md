Connecting Python to SQL
========================
To integrate with Python, we need to use the sqlite3 module to connect to our database. It behaves very similarly to interfaces for other SQL implementations, so it is a good starting point.

Open up hackbright\_app.py. Inside, you'll find a partial implementation of a database-backed application built off the database we built earlier.

Code Walkthrough
----------------
Using SQL through Python is not too different from doing it directly through the sqlite app, but there are some things we must observe.

### Step 1 -- Database Connection
The very first thing we must do is connect to the database and get a 'cursor'. A cursor is very similar to a file handle. For now, it is simply the mechanism that we use to interact with the database, to 'execute' our queries.

On line 16, you can see how a connection is made:

    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

### Step 2 -- Executing a Query
Given a cursor, we can use it to execute a query. On line 7, we can see the query we want to execute. A few things to notice, we don't need a semicolon when we execute a query string. Also, where we would normally have a filter for our where clause, we have a question mark.

    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""

The question mark is a placeholder. We'll use the same query over and over, each time to get the details of different students. The only thing that changes between each query is the 'WHERE github =' part of the query. When we execute the query on the next line, we fill in the question mark with an actual value. This is very much like the '%' substitution of Python strings.

    DB.execute(query, (github,))

It's important, even though we only have a single value we're substituting into the query, the sqlite3 module demands we pack it into a tuple when we do the substitution.

### Step 3 -- Fetching Rows
After we've executed the query, we need to fetch rows out of the table one at a time. We can do that by calling the .fetchone method on line 9. This returns a row as a tuple:

    row = DB.fetchone()

The tuple contains the values for each of the columns we selected:

    # Example
    print row
    ("Christian", "Fernandez", "chriszf")

### Step 4 -- Cleanup
Like files, we have to close our connection to our database when we're done. On quitting, we call the close method on the connection. Here, we do that on line 33:

    CONN.close()

Adding Data
-----------
Now that we can query for data, we need to be able to add more data to the system. We will walk you through the process of allowing the user to add a student.

### Step 1 -- Adding a new command
First, we'll add another command to our system by modifying our if statement in our main loop. The syntax for our 'new student' command will be as follows:

    HBA Database> new_student Bartholomew MacGillicuddy bartmac

To do this, change the if statement at line 28 to read:

    if command == "student":
        get_student_by_github(*args) 
    elif command == "new_student":
        make_new_student(*args)

We also need to make a function 'make\_new\_student'.

### Step 2 -- Inserting Data
Like the select statement before, we need to execute an INSERT statement, but there are quirks. First, we draw out our template for the INSERT, then fill the values when we execute it:

    def make_new_student(first_name, last_name, github):
        query = """INSERT into Students values (?, ?, ?)"""
        DB.execute(query, (first_name, last_name, github))

At this point, we've sent our data to the database, but it's not yet 100% persisted to the hard drive. We can still back out. We say that we're in the middle of a transaction. At this point, we can tell sqlite to abandon our changes, if we decide that we're inserting bad data. This is called a rollback. However, we're pretty confident our data is good, so we can go ahead and commit. Add the next lines:

        CONN.commit()
        print "Successfully added student: %s %s"%(first_name, last_name)

Much like github, this says to sqlite, yes, we're happy with our data, save it forever. Notice that we are committing on the database connection, and not the cursor.

Expansion
---------
The next step is to make the program do more. We need to:

* Add a student
* Query for projects by title
* Add a project
* Query for a student's grade given a project
* Give a grade to a student
* Show all the grades for a student

All these things you should try on your own. Try to implement as many of these as you can. You will probably find the sqlite3 module documentation helpful: http://docs.python.org/library/sqlite3.html
