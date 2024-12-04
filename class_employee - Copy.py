class Employee:
    domains = set()
    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}
    def __init__(self,name,email):
        self.name = name
        self.email = email
        Employee.domains.add(email.partition('@')[2])
    @property
    def email(self):
        pass
    @email.setter
    def email(self, mail):
        domain = mail.partition('@')[2]
        if domain not in Employee.allowed_domains:
            raise RuntimeError('Domain not allowed')
    def display(self):
        print(self.name, self.email)

e1 = Employee('John','john@gmail.com')
e2 = Employee('Jack','jack@yahoo.com')
e3 = Employee('Jill','jill@outlook.com')
e4 = Employee('Ted','ted@yahoo.com')
e5 = Employee('Tim','tim@xmail.com')
