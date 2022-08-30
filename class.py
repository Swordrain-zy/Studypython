#class define:
class Student:
    '''define a class "Student".'''
    pass
#instance:
s1=Student()#s1 is an instance of Stduent class

#add attribute in class:
class Stduent:
    count=0
    def __init__(self,ID,Name,gender='male'):
        self.Name=Name
        self.ID=ID
        self.gender=gender
s1=Student('zhangyu','1610320','male')#student information

#class attibute and ins attribute:
class Stduent:
    count=0#count is a class attribute
    def __init__(self,ID,Name,gender='male'):
        self.Name=Name
        self.ID=ID
        self.gender=gender#Name ID&gender are ins attribute
        Student.count+=1

#class method&ins method:
class Stduent:
    count=0
    def __init__(self,ID,Name,gender='male'):
        self.Name=Name
        self.ID=ID
        self.gender=gender
        Student.count+=1
    #methods:   
    def display_count(self):
        print("number of stduents:%d"%Student.count)
    #ins method
    @classmethod
    def class_dislay_count(cls):
        print("number of students:%d"%cls.count)
    #class method
    @staticmethod
    def static_display_count():
        print("number of stduents:%d"%Student.count)
    #static method:
    #using of method:
    s1=Student('zyh','1610320414','male')
    s1.display_count()#ins method
    Student.class_display_count()#class method
    Student.static_display_count()#static method

#class inheritance:
class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
#then define a new type student, which inherits attributes of Person:
class Student(Person):
    #Student is a subclass of Person.
    def __init__(self, name, gender, score, ID):
        super(Student,self).__init__(name,gender)#super function to use the function in Superclass
        #or:Person.__init__(self,name,gender)
        self.score=score
        self.ID=ID
        #score&&ID are attributes which added in Student class.

p1=Person('Tom','Male')
s1=Student('Kate','Female',98,'1610320')

#multiple inhertance:
#if class B&C inhert class A, class D inhert B&C
#then class D has all attributes & methods  from class A B&C

#class members' access control:
class Person:
    def __init__(self,name):
        self.name=name#public attribute
        self._title='Mr.'#protect attribute
        self.__salary=200000#private attribute
        pass

#polymorphism-superclass and subclass use same method name but different ways
class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def who_are_you(self):
        return'I am a Person, my name is %s.'%self.name

class Student(Person):
    def __init_(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score=score
    def who_are_you(self):
        return'I am a student, my name is %s.'%self.name

class Teacher(Person):
    def __init__(self,name,gender,course):
        super(Teacher,self).__init__(name,gender)
        self.course=course
    def who_are_you(self):
        return'I am a teacher, my name is %s.'%self.name

p1=Person('Tim','Male')
s1=Student('Bob','Male',98)
t1=Teacher('Lily','Female','History')
object_list=[p1,s1,t1]
for obj in object_list:
    print(obj.who_are_you())

#special method of class:
#1.__str__:
class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def __str__(self):
        return'Name:%s,Gender:%s'(self.name,self.gender)
p1=Person('Bob','male')
print(p1)

#2.__add__:
class Time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __str__(self):
        return"%.2d:%.2d:%.2d"%(self.hour,self.minute,self.second)
    def time_to_sec(self):
        minutes=self.hour*60+self.minute
        seconds=minutes*60+self.second
        return seconds
    def sec_to_time(self,seconds):
        minutes=seconds/60
        self.second=seconds%60
        self.minute=minutes%60
        self.hour=minutes/60
    def __add__(self,other):
        time=Time()
        seconds=self.time_to_sec()+other.time_to_sec()
        time.sec_to_time(seconds)
        return time

t1=Time(8,15)
t2=Time(1,30)
t3=t1+t2
print(t3)

