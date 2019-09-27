class Student:
	
	def __init__(self):
		self.id = None
		self.marks = None
		self.age = None
	
	def setDetails(self, i, marks, age):
		self.id = i
		self.marks = marks
		self.age = age
	
	def getDetails(self):
		return "Id:"+str(self.id)+ "\n" + "Marks:"+str(self.marks) + "\n" + "Age:"+str(self.age)

	def validateMarks(self):
		return self.marks >= 0 and self.marks <= 100

	def validateAge(self):
		return self.age >= 20

	def checkQualification(self):
		if self.validateMarks() and self.validateAge():
			return self.marks >= 65
		else:
			return False

if __name__ == "__main__":
	n = int(input("Enter the number of students "))
	students = []
	for i in range(n):
		students.append(Student())
	
	for i in range(n):
		print("Enter the details of student "+str(i+1))
		ide = int(input("Id:"))
		marks = int(input("Marks:"))
		age = int(input("Age:"))
		students[i].setDetails(ide, marks, age)
		
	for i in range(n):
		if students[i].checkQualification():
			print("Student with below details is eligible ")
			print(students[i].getDetails())
		else:
			print("Student with below details is ineligible ")
			print(students[i].getDetails())
