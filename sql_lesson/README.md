SQL and Relational Databases
============================
We'll be building a database that stores a list of students and their student projects. There are many ways we can do this, but by 'modeling' our data appropriately, it becomes easier to manipulate. The difficulty in using SQL and databases comes not from accessing the data, but from modeling the data in a way that is easy to access.

Start by cloning this repository, then go into the project directory and type the following at your prompt:

    sqlite3 hackbright.db

At the prompt, enter the following commands to make the output a little prettier:

    sqlite> .mode columns
    sqlite> .header on

Step 1: The student table
--------------------------------------
The first thing we need to do is be able to store our students. To do that, we create a 'student' table. It will look something like this:

    Table "Students"
    first_name | last_name | github
    -----------+-----------+----------
    Charles    | Ruhland   | cruhland
    Christian  | Fernandez | chriszf

We define a table by declaring what the names of the columns are and what data type we can put into them. SQL data types largely map directly to standard Python data types. Here, the python 'string' datatype maps to the sql 'varchar' datatype. One quirk here is that we have to say explicitly up front the maximum length of every string we'll ever use. This is hard to predict, but it's harder to expand the field later to allow bigger strings, so we pick a reasonable, oversized default. Enter the following command in your sqlite console to create the table:

````sql
CREATE TABLE Students (first_name varchar(30), last_name varchar(30), github varchar(30));
````

Right now, we've just created the table and it's empty. We need to **insert** data into it.
````sql
INSERT INTO Students (first_name, last_name, github) VALUES ("Charles", "Ruhland", "cruhland");
````
This inserts the first row into the table named 'Students', which we created above. Try inserting the second row yourself.

If the VALUES in your insert statement exactly match the order and number of columns in the table definition, we can be lazy and leave that section off:

    INSERT INTO Students VALUES ("Charles", "Ruhland", "cruhland");


Step 2: Getting our data back
-----------------------------
We've put our data in the table, so we're assured it's "stored" or "persisted" on disk for retrieval later. To do that, we use a 'select' statement.

A select statement lets us choose some combination of rows and columns out of our table. First, we see how to select _all_ of our rows and columns. Try the following command.

    SELECT * From Students;

We can also select individual columns from the table:

    SELECT last_name FROM Students;

We can also select multiple columns in any order:

    SELECT github, first_name FROM Students;

You can also select which rows you want. We use a 'WHERE' clause. For example, if we want all of the data for 'Christian', we can do the following:

    SELECT * FROM Students WHERE first_name="Christian";

We can filter on any value in our table. The following command gives the same search result:

    SELECT * FROM Students WHERE github="chriszf";

Now, we can combine the two concepts to get specific combinations of rows and columns out of our table:

    SELECT first_name, last_name FROM Students WHERE github="cruhland";

Before continuing on, insert your own rows into the table, and try selecting different rows and columns from your new data.

Step 3: The project table
-------------------------
Now, we need a table to store all the projects that the students will be doing. One important note here is that this table does not tell us which student did which project. It is simply a record of all the projects that everyone _can_ do.

    Table "Projects"
    title  | description                                   | max_grade
    -------------------------------------------------------------------
    Markov | Tweets generated from Markov chains           | 50
    Pyglet | Object-oriented game programming using Pyglet | 100 

We'll create a table as before, with the following command:

    CREATE TABLE Projects (title varchar(30), description TEXT, max_grade INT);

And again, we'll populate the table with some data with the 'INSERT' command:

    INSERT INTO Projects (title, description, max_grade) VALUES ("Markov", "Tweets generated from Markov chains", 50);
    INSERT INTO Projects (title, description, max_grade) VALUES ("Pyglet", "Object-oriented game programming using Pyglet", 100);


Step 3b: Primary Keys
---------------------
Let's run one of those project insert statements again:

    INSERT INTO Projects VALUES ("Markov", "Tweets generated from Markov chains", 50);

Now run your SELECT to look at the Projects table.  Oh no!  A duplicate entry has been entered for the Markov project!  We probably didn't want that.  Why in the world did you listen to me when I told you to run that insert again?!

No problem, we'll just delete that extra project.  DELETE works just like a SELECT, but without the column names.  The FROM and WHERE clauses are the same.  In fact, it's good practice to run a SELECT to see what rows your query matches before we run the delete.  

Ok, so we just need to write a SELECT statement to find our extra row.  How the heck do we do that?  The data is the same in both rows.  Hmmm... badness.  If only we had a way to uniquly identify each row of our table.   It'd also be nice if the database would prevent us from duplicating ourselves.  Lucky for us, databases can do this with something called PRIMARY KEYs.

If we identify a column in our table as a PRIMARY KEY column, the database will make sure that any data entered into this column is unqiue across all the rows of the table.  Numbers make really good primary keys and we can even let the database handle creating the keys for us.  If we add the AUTOINCREMENT keyword, the database will use the next available largest integer as the primary key for the table if we leave it out of our INSERT statement:

    CREATE TABLE Projects (id INTEGER PRIMARY KEY AUTOINCREMENT, title varchar(30), description TEXT, max_grade INT);

You'll have to "DROP TABLE Projects" before you can recreate the table.  WARNING: DROP TABLE will delete the table and all your data!  Run with care!

Now run the INSERTs again (leave off the new id column) and see what happens.

    INSERT INTO Projects (title, description, max_grade) VALUES ("Markov", "Tweets generated from Markov chains", 50);
    INSERT INTO Projects (title, description, max_grade) VALUES ("Pyglet", "Object-oriented game programming using Pyglet", 100);

Now SELECT from the table and notice that each row has been assigned an id.

Come up with three more projects and insert them into the table.


Step 4: Advanced Querying
-------------------------
Now that we have numeric data in the table, we can do more interesting things with our SELECT statement on our Projects table. We can do numerical comparisons:

    SELECT title, max_grade FROM Projects WHERE max_grade > 50;

Additionally, we can compose WHERE clauses together, joined with the 'OR' and 'AND' operators. This next line selects the title, and maximum possible grade from our project list where the maximum grade is between 50 and 100:

    SELECT title, max_grade FROM Projects WHERE max_grade > 50 AND max_grade < 100;

This next statement selects all the projects where the maximum grade is less than 25 or more than 75, but not in between:

    SELECT title, max_grade FROM Projects WHERE max_grade < 25 OR max_grade > 75;

Lastly, we can dictate in which order the results are returned to us by adding an 'ORDER' clause to our SELECT statement:

    SELECT * FROM Projects ORDER BY max_grade;

This orders the results by the max\_grade column, in numerical ascending order.

To review, the exact syntax of a select statement looks like this:

    SELECT column_list, separated_by, commas WHERE some_condition=True ORDER BY a_column;

Practice some selects as before, with different grade ranges and different row orderings.

Step 5: Linking the Tables Together
-----------------------------------
We have two tables, 'Students' and 'Projects', and so far they are completely unrelated. One table is simply a list of students, and the other is a list of projects. We need a way to indicate that a student has completed a project and has received a grade. To do that, we need a new table called 'Grades' that JOINs the two tables together.

    Table 'Grades'
    student_github  | project_title | grade
    ---------------------------------------
    chriszf         | Markov        | 10
    chriszf         | Pyglet        | 2 
    cruhland        | Markov        | 50
    cruhland        | Pyglet        | 100

Construct the CREATE TABLE statement on your own, using the previous examples as a template. The 'student\_github' column should be the same size and type as the 'github' column in the 'Students' table. The 'project\_title' should similarly matched to the 'title' column in the 'Projects' table.

** Create the table before moving on **

Reading this table, we can see that the student with the github account 'chriszf' has completed the project with the title 'Markov' for a total grade of 10. He has also completed the project entitled 'Pyglet' for a measly two points.

The student with the github account 'cruhland' on the other hand, is doing much better with his projects, scoring 50 and 100 on each.

The command to insert the first row is written as such:

    INSERT INTO Grades VALUES ("chriszf", "Markov", 10);

Before moving on, insert the remaining rows into the Grades table, as well as adding some of your own.

Even though there's no physical link between the tables, we have columns in the 'Grades' table that correspond to columns in the other two tables. Furthermore, the values in these columns refer to values in the other tables. We can use this to 'JOIN' the data across the columns.

Step 6: Joining Stuff
---------------------
If we wanted to find the first name, last name, project title, and project grade for a particular student, we cannot currently SELECT it out of any one table. That information is actually spread across three tables.

    The data we want:
    first_name | last_name | project_title | grade | max_grade
    ----------------------------------------------------------
    Christian  | Fernandez | Markov        | 10    | 50
    Christian  | Fernandez | Pyglet        | 2     | 100 

We'll build this query in pieces. First, we'll select the first\_name and last\_name out of the students table.

    SELECT first_name, last_name FROM Students WHERE github = "chriszf";

We'll call this **Query 1**.

Next, we'll select the grade, project and github for a student from the 'Grades' table.

    SELECT project_title, grade FROM Grades WHERE student_github = "chriszf";

This is **Query 2**.

Last, we need to select the project title and maximum grade from the 'Projects' table, **Query 3**.

    SELECT title, max_grade FROM Projects;

Now, we need _some_ way to mush all three queries together into a single query. That mechanism is called a JOIN. In rough terms, when we join two tables, we say that some column A in table 1 corresponds to some column B in table 2, and we should line them up. As an example, if we want to connect Students to Grades, we join _on_ the common column between them: the github column.

    SELECT * FROM Students INNER JOIN Grades ON (Students.github = Grades.student_github);

Notice now, the output shows the grades for a given Student on the same row as their first name. Next, we want to limit the columns. As we construct our query this time, we need to say which column comes out of which table. We use the dot notation for this:

    ex:
    Students.first_name
    Grades.project_title
    
Adding that restriction in, our query is getting hard to read, so we can split it across multiple lines as we type it in:

    SELECT Students.first_name, Students.last_name, 
           Grades.project_title, Grades.grade
    FROM Students
    INNER JOIN Grades ON (Students.github = Grades.student_github);


Next, we want to get the max\_grade out of the Projects table, as in Query 3. Again, we can stack joins on top of each other. In this case, the common data is in the 'title' column in the Projects table, and needs to be joined on the 'project\_title' column in the Grades table. First, we select everything to make sure it all lines up:

    SELECT *
    FROM Students
    INNER JOIN Grades ON (Students.github = Grades.student_github)
    INNER JOIN Projects ON (Grades.project_title = Projects.title);

We can add in a WHERE clause to show only the lines for the student with the github 'chriszf':

    SELECT *
    FROM Students
    INNER JOIN Grades ON (Students.github = Grades.student_github)
    INNER JOIN Projects ON (Grades.project_title = Projects.title)
    WHERE github = "chriszf";

Now that everything looks good, we once again filter down to only the columns we want. For the final step, write the query that selects only the columns that match our example table above:

    first_name, last_name, project_title, grade, max_grade

Now, try selecting the rows for different users in our system.

Step 7: Views
-------------
A curious property of relational databases is that our data is tabular, and when we extract different cross-sections of the data as above, the results are _also_ tabular. Even though it's not actually a table, we can use something called a VIEW to pretend the results of a particular query are a table. We can then select and join on this virtual table as if it were a real one.

Try creating these two views to produce a report card 'table':

    -- Join student names with project ID and grade using GitHub id as key
    CREATE VIEW GradesView AS
    SELECT Students.first_name, Students.last_name, Grades.project_title, Grades.grade
    FROM Students
    INNER JOIN Grades ON (Students.github=Grades.student_github);

    -- Join previous view with Projects to create nice looking "report card"
    CREATE VIEW ReportCardView AS
    SELECT GradesView.first_name, GradesView.last_name, Projects.title, GradesView.grade, Projects.max_grade
    FROM GradesView
    INNER JOIN Projects ON (GradesView.project_title=Projects.title);

Now, we can use ReportCardView as if it were a regular table.

    SELECT * from ReportCardView;

Play around with selecting and joining different data in your tables, and coming up with different views.

Once you finish this part, open up [part 2](https://github.com/hackbrightacademy/sql_lesson/blob/master/PART2-HB_APP.md)
