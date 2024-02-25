

from datetime import date
from Person import Person

class Student(Person):
    
    # class variable storing the next student number 
    # to assign (Exercise 9)
    nextStudId = 0 
    
    def __init__(self, name, degree): 
       """
       name, a string
       degree, a string
       Call __init__ of Person to initialise
       the attributes of the superclass followed
       by setting self's degree to the value
       of the degree argument.
       For Exercise 9, add code to 
       assign the student Id as explained
       in Lab 5 worksheet.
       """
       Person.__init__(self,name,degree)
       self.degree = degree
       self.studId = None


    def __init__(self, name , degree):
       Person.__init__(self , name)
       self.degree = degree
       self.studId = Student.nextStudId
       Student.nextStudId += 1

    def getDegree(self):
       """
       Getter method for self.degree
       """
       return self.degree

    def __str__(self):
       """
       Returns self's string representation 
       combining the values of self's name, birthday, and 
       degree attributes. 
       To ensure proper information hiding, 
       use getName() and getBirthday() methods of the parent
       class to retrieve the values of the name and 
       birthday attributes. 
       A possible return value could look like 
       '(Student:<self.name>:<self.birthday>:<self.degree>)' 
       as in '(Person:John Doe:1999-09-09:Data Science)'.
       """ 
       return f'(Student: {self.getName()} : {self.getBirthday()} : {self.degree})'
   
    def getStudId(self): 
        """
        Student Id getter for Exercise 9
        """
        return self.studId
   
class UnderGrad(Student):
    """
    A class representing an 
    undergraduate student.
    It does not add any new attributes
    to or overrides the existing attributes
    of Student. Do not replace pass with anything.
    """
    pass
 
class PostGrad(Student):
    """
    A class representing a postgraduate student.
    Specialises Student by 
    adding a new data attribute thesis_topic
    along with associated getter and setter methods.
    """
    
    def __init__(self, name, degree):
        """
        Call the constructor of Student, then
        set self's thesis_topic attribute
        to None
        """
        super().__init__(name , degree)
        self.thesisTopic = None

        
    def setThesisTopic(self, topic):
        """
        Setter method for self's thesis_topic
        attribute.
        """
        pass
        
    def getThesisTopic(self):
        """
        Getter method for self's 
        thesis_topic attribute
        """
        pass
        
class ExchangeStudent(Student):
    """
    A class representing an exchange student.
    Specialises Student by 
    adding a new data attribute home_school
    and an associated getter method.
    """
 
    def __init__(self, name, degree, home_school):
        """
        Call the constructor of Student, 
        then set self's home_school
        to the value passed in the 
        home_school argument
        """
        super().__init__(name,degree)
        self.homeSchool = homeSchool
        
    def getHomeSchool(self):
        """
        Getter method for self's home_school
        attribute
        """
        pass
    
def print_student_info(person):
        """
        This is a polymorphic function
        that accepts an instance of any person
        as a parameter, and then decides 
        what info to print based on the subtype.
        The output format is detailed in 
        Exercise 11 of Lab 5 worksheet.
        """
        pass
        
        
if __name__ == '__main__':  
    s1 = Student("Anna Gillian", "Data Science")
    s1.setBirthday(date(1973, 1, 1))
    s2 = Student("Leo Di Caprio", "Computer Science")
    print("Student", s1, "with ID", s1.getStudId())
    print("Student", s2, "with ID", s2.getStudId())
    print(s1 < s2)
    print(s2 < s1)
    
    # Tests for print_student_info
    ug = UnderGrad("Carl Smart", "Computer Science")
    pg = PostGrad("Mary Clever", "Information Security")
    pg.setThesisTopic("Secure Deep Learning")
    ex = ExchangeStudent("Will Homesick", "Music", "Ecole Normale")
    tom = Person("Tom Cruise")
    tom.setBirthday(date(1962, 7, 3))
    
    # 1 Carl Smart is an undergrad studying Computer Science
    print_student_info(ug)
    
    # 2 Mary Clever is a postgrad studying Information Security with thesis topic 
    # 'Secure Deep Learning'
    print_student_info(pg)
    
    # 3 Will Homesick is an exchange student from Ecole Normale studying Music
    print_student_info(ex)
    
    # Tom Cruise is 56 years old and is not a student
    print_student_info(tom)
    
    # TypeError
    print_student_info("Sheldon Cooper")