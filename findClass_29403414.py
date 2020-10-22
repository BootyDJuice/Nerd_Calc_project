# Author: Semen Mordovin
# ID: 29403413
# Start Date: 06/04/2019
# Last Modification Date: 11/04/2019

""" Importing random library to apply random numbers for our student score to
check number of class occurrences
"""

import random

"""Main function which divides student score into different classes, according
to our requirements. Using fop loop and lists to work with data. if  conditions
is to check necessary conditions for list of Student Scores"""

def countStudentClass(studentScore_list):
	if len(studentScore_list) < 1:
		print("Please add at least 1 item into the list")
		return 0
	
	nerdCount_list = [0] * 7
	
	if len(studentScore_list) > 1:
		for item in studentScore_list:
			if item == 0:
				nerdCount_list[0] += 1
			if 10 > item >= 1:
				nerdCount_list[1] += 1
			if 100 > item >= 10:
				nerdCount_list[2] += 1
			if 500 > item >= 100:
				nerdCount_list[3] += 1
			if 1000 > item >= 500:
				nerdCount_list[4] += 1
			if 2000 > item >= 1000:
				nerdCount_list[5] += 1
			if item >= 2000:
				nerdCount_list[6] += 1
	return nerdCount_list


"""Random.sample used here with range of 0 - 5000 to generate random numbers
for student score. Number of 10 students have received their Nerd Scores for the
sake of this task. Main constructor presented via template"""

if __name__ == '__main__':
	#test cases
	#studentScore_list = []  #
	#output should be [0, 0, 2, 0, 1, 1, 0]

	studentScore_list = 9


	print("There is a number of student Nerd Scores and the number of each \
	class appearances")
	print(studentScore_list)
	print(countStudentClass(studentScore_list))

