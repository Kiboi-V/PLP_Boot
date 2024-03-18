
class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def introduce(self):
        return f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}."

# Create an instance of the Person class
p1 = Person('Kiboi', 30, 'male')

# Call the introduce method to display the person's information
print(p1.introduce())