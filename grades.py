

import sys, getopt


def calculate(a, c):
	difference = ((a-c)/2)
	third = difference/3
	b = c + difference

	print("A : " + str(a))
	print("A-: " + str(a-third))
	print("B+: " + str(b+third))
	print("B : " + str(b))
	print("B-: " + str(b-third))
	print("C+: " + str(c+third))
	print("C : " + str(c))


def main(argv):
	if(len(argv) != 2):
		print 'grades.py <A> <C>'
		sys.exit()

	calculate(int(argv[0]), int(argv[1]))


if __name__ == "__main__":
   main(sys.argv[1:])