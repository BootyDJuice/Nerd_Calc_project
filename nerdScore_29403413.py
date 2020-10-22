# Author: Semen Mordovin
# ID: 29403413
# Start Date: 06/04/2019
# Last Modification Date: 11/04/2019

""" Importing math library to use ia square operation in our Nerd Score formula
"""

import math

"""This is the main function to calculate our Nerd Score, using x, y,z as a 
possible user inputs for our Fandom Score, Hobbies Score and Number of Sports 
played. Creating a,b,c, square variables to simplify calculation of a Nerd 
Score Square. if statements for checking. Return Score if conditions are met"""

def calculateSkillEquation(FandomScore, HobbiesScore, SportsNum):
	x = FandomScore
	y = HobbiesScore
	z = SportsNum
	a = y ** 2
	b = a * 42
	c = z + 1
	square = b // c
	skillScore = x * (math.sqrt(square))
	mistake_one = "Fandom Score can nto be less or equal to zero!"
	mistake_two = "Hobbies Score should be multiplies of 4 and not equal to 0"
	mistake_three = "Number of sport played must be positive"
	if x <= 0:
		return mistake_one
	if y % 4 != 0 or y == 0:
		return mistake_two
	if z <= 0:
		return mistake_three
	return skillScore


"""Main constructor presented via template"""

if __name__ == '__main__':

	FandomScore, HobbiesScore, SportsNum = 1, 4, 1  # Can apply different
	# numbers for checking

	print(calculateSkillEquation(FandomScore, HobbiesScore, SportsNum))
