class Student:
  def __init__(self,name,roll_number,cgpa):
    self.name = name 
    self.roll_number = roll_number
    self.cgpa = cgpa
def sort_students(students_list):
  sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
  return sorted_students
students =[
  Student("jamuna","A123",7.8),
  Student("kiruthi","A124",8.6),
  Student("priya","A125",8.7),
  Student("hindu","A126",8.8),
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA:{},".format(student.name,student.roll_number,student.cgpa))