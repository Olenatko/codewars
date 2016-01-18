'''class Person:
  def __init__(self, name, other_name):
    self.name = name
    self.other_name = other_name

  def greet(self):
    return "Hi {0}, my name is {1}".format(self.other_name, self.name)
print(Person('Olia', 'Vika').greet())'''

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self, other_name):
    return "Hi {0}, my name is {1}".format(other_name, self.name)
print(Person('Olia').greet('vika'))

