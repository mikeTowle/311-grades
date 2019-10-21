

import sys, collections


def determine_grade(a,c,score):
	grades = calculate(a,c)
	for key in sorted(grades.keys()):
		if(score >= grades[key]):
			print("\nYour Score: " + str(score) + " = " + key)
			break



def calculate(a, c):
	difference = ((a-c)/2)
	third = difference/3
	b = c + difference
	grades = collections.OrderedDict()

	print("A : " + str(a))
	grades["A"] = a
	print("A-: " + str(a-third))
	grades["A-"] = a-third
	print("B+: " + str(b+third))
	grades["B+"] = b+third
	print("B : " + str(b))
	grades["B"] = b
	print("B-: " + str(b-third))
	grades["B-"] = b-third
	print("C+: " + str(c+third))
	grades["C+"] = c+third
	print("C : " + str(c))
	grades["C"] = c
	return grades


def main(argv):

	if(len(argv) == 2):
		calculate(int(float(argv[0])), int(float(argv[1])))
	elif(len(argv) == 3):
		determine_grade(int(float(argv[0])), int(float(argv[1])), int(float(argv[2])))
	else:
		print 'grades.py <A> <C>'
		sys.exit()

	


if __name__ == "__main__":
   main(sys.argv[1:])