from peewee import *

conn = SqliteDatabase('DB_Students2.sqlite')

class Students(Model):
	id1 = PrimaryKeyField(column_name = 'id1')
	name = CharField(column_name = 'name')
	surname = CharField(column_name = 'surname')
	age = IntegerField(column_name = 'age')
	city = CharField(column_name = 'city')

	class Meta:
		database = conn

class Courses(Model):
	id1 = PrimaryKeyField(column_name = 'id1')
	name = CharField(column_name = 'name')
	time_start = CharField(column_name = 'time_start')
	time_end = CharField(column_name = 'time_end')

	class Meta:
		database = conn

class Student_courses(Model):
	student_id = ForeignKeyField(Students)
	course_id = ForeignKeyField(Courses)

	class Meta:
		database = conn

Students.create_table(), Courses.create_table(), Student_courses.create_table()

Courses.insert_many([{'id1': 1, 'name': 'python', 'time_start': '21.07.21', 'time_end': '21.08.21'},
                     {'id1': 2, 'name': 'java', 'time_start': '13.07.21', 'time_end': '16.08.21'}]).execute()

Students.insert_many([{'id1': 1, 'name': 'Max', 'surname': 'Brooks', 'age': 24, 'city': 'Spb'},
	                  {'id1': 2, 'name': 'John', 'surname': 'Stones', 'age': 15, 'city': 'Spb'},
	                  {'id1': 3, 'name': 'Andy', 'surname': 'Wings', 'age': 45, 'city': 'Manhester'},
	                  {'id1': 4, 'name': 'Kate', 'surname': 'Brooks', 'age': 34, 'city': 'Spb'}]).execute()

st_select = Students.select()
cr_select = Courses.select()

Student_courses.insert_many([{'student_id': st_select[0], 'course_id': cr_select[0]},
                             {'student_id': st_select[1], 'course_id': cr_select[0]},
                             {'student_id': st_select[2], 'course_id': cr_select[0]},
                             {'student_id': st_select[3], 'course_id': cr_select[1]}]).execute()

for name in Students.select().where(Students.age > 30):
    print("1)", name.name, name.surname, "- Старше 30 лет.")

for python in Students.select().join(Student_courses).where(Student_courses.course_id == 1):
    print("2)", python.name, python.surname, "- Изучает python.")

for spb in Students.select().join(Student_courses).where(Student_courses.course_id == 1, Students.city == 'Spb'):
    print("3)", spb.name, spb.surname, "- Из СПБ.")