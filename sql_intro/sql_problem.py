import hashlib
import sqlite3

def connect():
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.arraysize = 20
    return cursor

def result_to_str(results):
    row_strings = [ "|".join([str(col) for col in row]) for row in results ]
    out_string = "\n".join(row_strings)
    return out_string

def generate_result_hash(soln_query, cursor):
    cursor.execute(soln_query)
    answers = cursor.fetchmany()

    answer_str = result_to_str(answers)
    digest = hashlib.md5(answer_str).hexdigest()

    return digest


def check_solution(problem, result_str):
    digest = hashlib.md5(result_str).hexdigest()
    return problem['soln_hash'] == digest
