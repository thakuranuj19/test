class Car:
	def __init__(self,regno,color,age):
		self.color =  color
		self.regno = regno
		self.age = age


	def __repr__(self):
		return "Car [registration_number=" + self.regno + ", color=" + self.color + "]"

	def __str__(self):
		return "Car [registration_number=" + self.regno + ", color=" + self.color + "]"
