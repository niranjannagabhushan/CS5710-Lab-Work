

from datetime import date

class Person(object):
    
    def __init__(self, name): 
        """
        name, string
        birthday, instance of datetime.date
        Creates a person setting self's name attribute to
        the value of the name argument, and birthday to None.
        """
        self.name = name
        self.birthday = None

    def setBirthday(self, birthday):
        """
        birthday, an instance of datetime.date
        Sets self's birthday attribute to birthday
        """
        
        if not isinstance(birthday , date):
            raise TypeError('Birthday must be a date object')
        self.birthday = birthday
            
    def getBirthday(self):
        """
        Returns self's birthday attribute
        """
        self.birthday = birthday

    def getName(self):
        """
        Returns self's name attribute
        """ 
        return self.name
    
    def getAge(self):
        """
        Returns self's current age in years.
        Hint: Use date.today().year to get the year of today, and
        the year attribute of birthday to get the birthday's
        year. Return the difference between the two. 
        """ 
        if self.birthday == None:
            raise ValueError('Birthday not set')
        return date.today().year - self.birthday.year
    
    def __lt__(self, other):
        """
        Returns True if self's name is lexicographically
        less than other's name, and False otherwise.
        Implementing this method will enable sorting of lists
        comprised of instances of this class.
        """
        return self.name < other.name
    
    def __str__(self):
        """
        Returns self's string representation 
        combining the values of self's name and 
        birthday attributes. 
        A possible return value could look like 
        '(Person:<self.name>:<self.birthday>)' 
        as in '(Person:John Doe:1999-09-09)'.
        """ 
        return f'(Person : {self.name} : {self.birthday})'

if __name__ == '__main__':
    
    # Create an instance of Person
    p = Person("Tom Cruise")
    
    # Set birthday attribute    
    p.setBirthday(date(1962, 7, 3))
    
    # Outputs the string representation of p
    # as determined by your __str__() method code
    print(p)
    
    # Tom Cruise is 56 years old
    print(p.getName(), "is", p.getAge(), "years old")

    # Create a list of Person objects initialized with the 
    # given names and default birthdays
    plist = [Person("John Doe"), Person("Jane Smith"), 
    		 Person("Sheldon Cooper"),
             Person("Jason Bourne"), Person("Anna Gillian")]
    
    # Sorts list in the order consistent with < 
    # as determined by your __lt__() method logic.
    # Sorting of a list (or any other iterable type)
    # is automatically enabled provided its instances
    # implement the __lt__() method.
    plist.sort() 

    # Uses list comprehension (for/in inside list brackets []) 
    # to create a list of string representations
    # out of the Person objects stored in plist, 
    # and prints the resulting list.
    # This is more compact than printing in a loop though
    # not as efficient since a new copy of the list is created.
    str_list = [str(p) for p in plist]
	
	# Should output a list of stringified Person instances
    # sorted in the lexicographical order of their names.
    print(str_list)
    
    print(type(p) == object)
    print(isinstance(p, object))
    
    from datetime import date

    try:
        x = Person("Eve Polastri")
        bday = date(1983 , 4 , 10)
        x.setBirthday(bday)
    except TypeError as e:
        print("Type error occurred", e)




def getBirthday(self):
    print(self.birthday) 
    return self.birthday