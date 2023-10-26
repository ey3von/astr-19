#write a python program that declares a class describing your favorite animal

import sys

class Shape:

	def print(self):
		print("My Favorite Animal!")
		print("The infamous fruit bat!")
		print(f"length of arms = {self.arm_length}")
		print(f"length of legs = {self.leg_length}")
		print(f"number of eyes = {self.num_eyes}")

	def __init__(self,alength=30.,llength=4.,neyes=2):
		self.arm_length   = alength
		self.leg_length   = llength
		self.num_eyes     = neyes

def main():
	alength = 30.

	llength = 4.

	neyes = 2

	if(len(sys.argv)>=2):
		alength = float(sys.argv[1])
	if(len(sys.argv)>=3):
		llength = float(sys.argv[2])
	if(len(sys.argv)>=4):
		neyes = int(sys.argv[3])

	my_animal = Shape(alength=alength,llength=llength,neyes=neyes)

	my_animal.print()

	print("Does my animal have a tail?")

	yes = True
	print(yes)

	print("Is my animal furry?")

	yes = True
	print(yes)

if __name__=="__main__":
	main()