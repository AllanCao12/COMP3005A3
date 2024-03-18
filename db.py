import psycopg2


def getAllStudents():

    con = psycopg2.connect(
    host = "localhost",
    database="a3",
    user="postgres",
    password="franzy613",
    port="5432"
    )
    con.autocommit = True


    cur = con.cursor()

    cur.execute("select * from students")

    rows = cur.fetchall()
    print("Outputting table")
    for r in rows:
        print("id {} fname {} lname {} email {} enrollment date {}".format(r[0], r[1], r[2], r[3], r[4]))
    print("\n")
    cur.close()
    con.close()

def addStudent(first_name, last_name, email, enrollment_date):
    con = psycopg2.connect(
    host = "localhost",
    database="a3",
    user="postgres",
    password="franzy613",
    port="5432"
    )
    con.autocommit = True
    cur = con.cursor()

    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))

    cur.close()
    con.close()

def updateStudentEmail(student_id, new_email):
    con = psycopg2.connect(
    host = "localhost",
    database="a3",
    user="postgres",
    password="franzy613",
    port="5432"
    )
    con.autocommit = True
    cur = con.cursor()

    cur.execute("Update students set email = %s where student_id= %s", (new_email, student_id))

    cur.close()
    con.close()

def deleteStudent(student_id):
    con = psycopg2.connect(
    host = "localhost",
    database="a3",
    user="postgres",
    password="franzy613",
    port="5432"
    )
    con.autocommit = True
    cur = con.cursor()

    cur.execute("delete from students where student_id = %s", (student_id))

    cur.close()
    con.close()


# running the code

# con = psycopg2.connect(
# host = "localhost",
# database="a3",
# user="postgres",
# password="franzy613",
# port="5432"
# )
# con.autocommit = True
# cur = con.cursor()

# create_table = '''
#     CREATE TABLE IF NOT EXISTS students (
#         student_id SERIAL PRIMARY KEY,
#         first_name VARCHAR(50) NOT NULL,
#         last_name VARCHAR(50) NOT NULL,
#         email VARCHAR(50) UNIQUE NOT NULL,
#         enrollment_date DATE
#     )
# '''
# cur.execute(create_table)

# cur.close()
# con.close()

# getAllStudents()

# addStudent('John', 'Doe', 'john.doe@example.com', '2023-09-01')
# addStudent('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01')
# addStudent('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')

# getAllStudents()

# addStudent('Allan', 'Cao', 'allancao@example.com', '2024-03-18')

# getAllStudents()

# updateStudentEmail("1", "john_email@carleton.ca")

# getAllStudents()

# deleteStudent("4")

# getAllStudents()

# deleteStudent("1")

# getAllStudents()

# addStudent('John', 'Doe', 'john.doe@example.com', '2023-09-01')

# getAllStudents()
