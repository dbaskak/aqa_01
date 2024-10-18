# Employee base class constructor
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Manager class inherits Employee constructor
class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary) # Call Employee's constructo
        self.department = department

# Developer class inherits Employee constructor
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)  # Call Employee's constructor
        self.programming_language = programming_language

# TeamLead class inherits both Manager and Developer constructors
class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department) # Call Manager's constructor
        Developer.__init__(self, name, salary, programming_language) # Call Developer's constructor
        self.team_size = team_size

    def display_info(self):
        """Display team lead's info"""
        print(f"Team Lead: {self.name}, Salary: {self.salary}, Department: {self.department}, "
              f"Programming Language: {self.programming_language}, Team Size: {self.team_size}")


# Create an object of TeamLead and display its info
lead = TeamLead("Jack Black", 200000, "AQA", "Python", 7)
lead.display_info()