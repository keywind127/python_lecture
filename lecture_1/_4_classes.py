
## example 1

class User:
    EMPTY_NAME = ""
    def __init__(self, name):
        self.name = self.verify_name(name)

    def __repr__(self):
        return self.name
    
    @classmethod
    def verify_name(cls, name):
        if name != cls.EMPTY_NAME:
            return name
        return ""
    
class Student(User):
    def __init__(self, name, sid):
        super().__init__(name)
        self.sid = sid

    @property
    def capped_name(self):
        return self.name.capitalize()
    
    @property
    def upper_name(self):
        return self.name.upper()
    
    @property
    def lower_name(self):
        return self.name.lower()
    
student = Student("Kevin", 127)

print(student)

## example 2: property method to concatenate student name and ID

class User:
    EMPTY_NAME = ""
    def __init__(self, name):
        self.name = self.verify_name(name)

    def __repr__(self):
        return self.name
    
    @classmethod
    def verify_name(cls, name):
        if name != cls.EMPTY_NAME:
            return name
        return ""
    
class Student(User):
    def __init__(self, name, sid):
        super().__init__(name)
        self.sid = sid

    @property
    def capped_name(self):
        return self.name.capitalize()
    
    @property
    def upper_name(self):
        return self.name.upper()
    
    @property
    def lower_name(self):
        return self.name.lower()
    
    # implement your code here
    # :)
    # :)
    @property
    def student_info(self):
        return f"{self.name}{self.sid}"

student = Student("Kevin", 127)

print(student.student_info)
