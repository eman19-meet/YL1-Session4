תclass Animal(object):
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
a.make_sound()
a.sound_X()

class Person(object):	
	def_init_(self,name,age,city,gender,favorate_brakefast,favorate_sport):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
		self.favorate_brakefast=favorate_brakefast
		self.favorate_sport=favorate_sport
		
	def brakefast(self):
		print(self.name + "is eating his/her favorate brakefast, which is: " +self.favorate_brakefast)
	def sport(self):
		print(self.name + "is playing " + self.favorate_sport)

p = Person("eman",15,"kfar kanna", "female")
p.brakefast()
p.sport()

class Song(object):
	def_init_(self,lyrics[]):
		self.lyrics[]=lyrics[]
		
	#not sure about the sing_me_a_song !!!!
	def sing_me_a_song(self):
		for i in range(len(lyrics)):
			print(lyrics[i])
			
flower_song = Song("Roses are red,", "Violets are blue,", "I wrote this poem for you.")
flower_song.sing_me_a_song()
		
