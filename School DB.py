class Teacher:
    def __init__(self, name, Class,NOP ):
        self.name = name
        self.Class = Class
        self.NOP = NOP
        
    def class_Teacher(self):
        return'{} {}'.format(self.name, self.Class, self.NOP)
    
t1 = Teacher('Sir Micheal',' 1','36')
t2 = Teacher('Madam Gifty',' 5','89')
t3 = Teacher('Sir Micheal',' 1','36')
t4 = Teacher('Sir Micheal',' 1','36')
t5 = Teacher('Sir Micheal',' 1','36')
t6 = Teacher('Sir Micheal',' 1','36')


class Student(Teacher):
    def __init__(self, name, Class, age,PC):
        self.name = name
        self.Class = Class
        self.age = age
        self.PC= PC

s1 = Student('Emily', '4' , '10','O2456328')
s2 = Student('Paul', '6' , '13','0592069096')
   



print(f"class teacher :{t1.name}, Class : {t1.Class}, Number of pupils : {t1.NOP}")
print(f"Student Name : {s2.name}, Class :{s2.Class}, Age: {s2.age}, Contact : {s2.PC}")
