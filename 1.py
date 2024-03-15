import sqlite3
from datetime import datetime

conn = sqlite3.connect('db4.sqlite')
cursor = conn.cursor()


cursor.execute("CREATE TABLE Students (id int, firstname Varchar(32), lastname Varchar(32), age int, city Varchar(32))")

cursor.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)", [(1, 'Max', 'Hax', 30, 'Moscow'), (2, 'Victor', 'Nyx', 25, 'Kaliningrad'),(3, 'Igor', 'Lux', 20, 'Saint-Peterburg')])


cursor.execute("CREATE TABLE Courses (id int, name Varchar(32), time_start timestamp, time_end timestamp)")

cursor.execute("CREATE TABLE Student_courses (student_id int,course_id int)")


cursor.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)", [(11, 'Math', datetime.today(), datetime.now()), (12, 'IT', datetime.today(), datetime.now()),(13, 'PE', datetime.today(), datetime.now())])


cursor.executemany("INSERT INTO Student_courses VALUES (?, ?)", [(1, 11), (2, 12), (3, 13)])
conn.commit()

cursor.execute("SELECT * FROM Student_courses WHERE student_id = 1 AND course_id = 11")
print(cursor.fetchall())

conn.close()