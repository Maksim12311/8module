import sqlite3
from datetime import datetime

conn = sqlite3.connect('db5.sqlite')
cursor = conn.cursor()


cursor.execute("CREATE TABLE Students (id int, firstname Varchar(32), lastname Varchar(32), age int, city Varchar(32))")

cursor.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)", [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'), (3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')])


cursor.execute("CREATE TABLE Courses (id int, name Varchar(32), date_start date, date_end date)")

cursor.execute("CREATE TABLE Student_courses (student_id int,course_id int)")


cursor.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)", [(1, 'python', '2021-07-21', '2021-08-21'), (2, 'java', '2021-07-13', '2021-08-16')])


cursor.executemany("INSERT INTO Student_courses VALUES (?, ?)", [(1, 1), (2, 1), (3, 1), (4, 2)])
conn.commit()

cursor.execute("SELECT * FROM Students WHERE age > 30")
print(cursor.fetchall())
cursor.execute("SELECT Students.* FROM Students JOIN Student_courses ON Students.id = Student_courses.student_id JOIN Courses ON Student_courses.course_id = Courses.id WHERE Courses.name = 'python'")
print(cursor.fetchall())
cursor.execute("SELECT Students.* FROM Students JOIN Student_courses ON Students.id = Student_courses.student_id JOIN Courses ON Student_courses.course_id = Courses.id WHERE Courses.name = 'python' AND Students.city = 'Spb'")
print(cursor.fetchall())
conn.close()