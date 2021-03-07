class Student:
    def passorfail(self):
        if self.mark >=40:
            return True
        else:
            return False

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark


student = Student("aju", 60)
print(student.name)
jayicho = student.passorfail()
print(jayicho)

