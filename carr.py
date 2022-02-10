class car(object):
    condition = "new"
    print(condition)
    
    def __init__(self, model, color, mpg, condition):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.condition = condition
        
    def display_car(self):
        print ("My name is " + self.model + "and I am " + self.color + "my mpg is " + self.mpg)
        
    def drive_car(self):
        print("My car is " + self.condition)
        


my_car = car("Delorean", "silver", "88", "used")
my_car.drive_car()

class elec(car):
    condition = "new"
    print(condition)
    
    def __init__(self, model, color, mpg, condition, battery):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.condition = condition
        self.battery = battery
    
    def display_carr(self):
        print ("My name is " + self.model + "and I am " + self.color + "my mpg is " + self.mpg + "my bat type is " + self.battery)
    
    
    
my_carr = elec(" a ", " b ", " c ","like new", "molten salt")
my_carr.display_carr()

my_carr.drive_car()




    

