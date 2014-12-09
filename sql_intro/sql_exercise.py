#!/bin/env python

import os
import sql_problem
import readline
import sys
import pickle
import sqlite3

# File to store the student's answers
ANSWER_FILE = 'answers.sql'
answers = {}


def show_problem(problem, problem_num):
    print "\nProblem %d"%problem_num
    print "----------------\n"
    print problem['instruction']

def intro():
    print """\

Hackbright Academy - Introductory SQL Exercise 
----------------------------------------------

You will write a series of SQL queries accomplishing different tasks. 
Each problem will include a link to a SQLZoo tutorial that illustrates 
the concepts required, as well as a link to syntax reference for the 
kind of query you'll be doing.

Type '.help' without quotes for a list of the available commands.

It will be helpful to refer to the list of tables, found by typing in '.tables',
or viewing the schema of a given table, (ex: .schema orders) while formulating
your queries. If you get very stuck each problem includes a hint on how to
formulate your query, accessed by typing '.hint'.
"""
    print ""
    

def repl(cursor, problem, problem_num):
    raw_input("[ Press Enter to continue ]")
    show_problem(problem, problem_num)

    while True:
        try:
            line = raw_input("SQL [%d]> " % problem_num)
        except EOFError:
            # End of File reached, exit
            sys.exit(0)

        line.strip()
        
        if not line:
            continue

        tokens = line.split()

        if tokens[0] in ["q", "exit", "quit", ".quit", ".exit"]:
            sys.exit(0)

        elif tokens[0] in [".problem", "problem", ".p"]:
            show_problem(problem, problem_num)

        elif tokens[0] in [".hint", "hint"]:
            print problem['hint']

        elif tokens[0] in [".tables", ".table", "tables"]:
            tables(cursor)

        elif tokens[0] in [".schema", "schema"]:
            schema(tokens, cursor)

        elif tokens[0] in [".help", ".h", "help", "?", ".?"]:
            help()

        elif tokens[0] in [".next", ".skip", "next", "skip"]:
            print "Skipping problem %d" % problem_num
            return

        else:
            result = execute(line, problem, cursor)
            if result:
                answers[problem_num] = line
                show_success(line)
                save_answers()
                return

def show_success(line):
    print "\n\tCorrect!"
    print "\t",line
    print "\tMoving on...\n"

def execute(line, problem, cursor):
    try:
        cursor.execute(line)
        results = cursor.fetchmany() 
    except sqlite3.OperationalError, e:
        print "There was a problem with your sql syntax:\n\n\t%s\n"%e
        return

    result_str = sql_problem.result_to_str(results)
    print result_str

    return sql_problem.check_solution(problem, result_str)


def tables(cursor):
    query = """select name from sqlite_master where type='table';"""
    try: 
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.OperationalError, e:
        print "There was a problem getting the table list:\n\n\t%s\n"%e
        return

    results.remove((u"alembic_version",))

    output = sql_problem.result_to_str(results)
    print "The following tables are available:\n", output

def help():
    print """
The following commands are available:

    .help    - Display this message
    .hint    - Show a hint about how to formulate the query
    .next    - Skip the current problem
    .problem - Show the current problem statement
    .quit    - Quit the program
    .schema <table_name> - Show the schema used to define a given table
    .tables  - Show all the tables available in the database

Any other commands will be interpreted as a SQL query and executed against the
problem set database.
"""


def schema(tokens, cursor):
    if len(tokens) < 2:
        print "Please indicate a table name"
        return

    table_name = tokens[1]
    query = """select sql from sqlite_master where type='table' and name=?""";
    try: 
        cursor.execute(query, (table_name,))
        results = cursor.fetchall()
    except sqlite3.OperationalError, e:
        print "There was a problem getting the table schema:\n\n\t%s\n"%e
        return

    output = sql_problem.result_to_str(results)
    if not output:
        print "No such table: %s"%table_name
        return

    print output

def load_problems():
    with open("problem_set.pickle") as f:
        return pickle.load(f)

# if an answers file already exists, load it
def load_answers():
    if not os.path.isfile(ANSWER_FILE):
        return

    with open(ANSWER_FILE, 'r') as f:
        probnum = 0
        query = ''

        line = f.readline()

        while line:
            line = line.strip()

            # Check for a comment
            if line[0:10] == '-- Problem':
                probnum = line[11:]
                try:
                    probnum = int(probnum)
                except:
                    pass

                answers.setdefault(probnum, '')

            # Check for SQL statement
            elif line != '' and probnum > 0:
                if answers.get(probnum) != '':
                    answers[probnum] += "\n";
                answers[probnum] += line;

            # print "read: ", line
            line = f.readline()

    # print "answers"
    # print answers


# Save student answers to a file
def save_answers():
    with open(ANSWER_FILE, 'w') as f:
        for key in sorted(answers.keys()):
            f.write("-- Problem %s\n" % key)
            f.write("%s\n\n" % answers.get(key, ''))


def main():
    # Connect to SQLite
    cursor = sql_problem.connect()
    problems = load_problems()
    load_answers()
    
    # Display Into Message
    intro()
    
    for idx, problem in enumerate(problems):
        repl(cursor, problem, idx+1)

if __name__ == "__main__":
    main()
