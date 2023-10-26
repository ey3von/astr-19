import numpy as np 
import sys

def f(x): 
	return(x**3 + 8)


def main():
	x = 9
	print(f(9))

	if (f(9) >  27):
		print("YAY!")

if __name__=="__main__":
	main()
	

