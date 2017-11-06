class Animal(object):
	def_init_(self,sound,name,age,favorite_color):
		self.sound=sound
		self.name=name
		self.age=age
		self.favorate_color=favorite_color

	def eat(self,food):
		print("Yummy!! "+self.name+" is eating "+food)

	def description(self):
		print(self.name+" is "+self.age+" years old, and loves the collor "+self.favorate_color)

	def make_sound(self):
		print(self.sound *3)

	def sound_X(self,x):
		print(self.sound *x)

a = Animal("haha","cat", 4, yellow)
a.eat("meat")
a.description()

class Person(object):	
	def_init_(self,name,age,city,gender):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender

p = Person("eman",15,"kfar kanna", "female")
