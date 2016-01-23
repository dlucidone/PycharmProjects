class Parent():

    def Print_last_name(self):
        print('roberts')

class Child(Parent):

    def Print_first_name(self):
        print('bucky')

    def Print_last_name(self):
        print('Snitlzberg')


bucky = Child()
bucky.Print_first_name()
bucky.Print_last_name()