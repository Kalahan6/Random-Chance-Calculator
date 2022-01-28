import random

numberOfRolls = 10000

def percentage(part, whole):
  percentage = 100 * float(part)/float(whole)
  return str(percentage) + "%"

def rolldice(numberOfDice, numberOfSides, modifier, successTresshold):
	numberOfSuccesses = 0

	for x in range (0,numberOfRolls):
		success = False
		for y in range (0,numberOfDice):
			result = random.randint(1, numberOfSides)
			if (result + modifier) >= successTresshold:
				success = True
		if success:
			numberOfSuccesses += 1

	print (str(numberOfDice) + "d" + str(numberOfSides) + "+" + str(modifier) + " with a success on " + str(successTresshold) + ": " + str(percentage(numberOfSuccesses, numberOfRolls)) + " success ratio" )


# WRITE rolldice() COMMANDS BELOW

print("\n")
print("1D6 syccess on 4")

rolldice(1,6,0,4)
rolldice(1,6,1,4)
rolldice(1,6,2,4)
rolldice(1,6,3,4)

print("\n")
print("2D6 success on 4")

rolldice(2,6,0,4)
rolldice(2,6,1,4)
rolldice(2,6,2,4)
rolldice(2,6,3,4)

print("\n")
print("3D6 success on 4")

rolldice(3,6,0,4)
rolldice(3,6,1,4)
rolldice(3,6,2,4)
rolldice(3,6,3,4)

print("\n")
print("1D6 syccess on 5")

rolldice(1,6,0,5)
rolldice(1,6,1,5)
rolldice(1,6,2,5)
rolldice(1,6,3,5)

print("\n")
print("2D6 success on 5")

rolldice(2,6,0,5)
rolldice(2,6,1,5)
rolldice(2,6,2,5)
rolldice(2,6,3,5)

print("\n")
print("3D6 success on 5")

rolldice(3,6,0,5)
rolldice(3,6,1,5)
rolldice(3,6,2,5)
rolldice(3,6,3,5)


print("\n")
print("1D6 syccess on 6")

rolldice(1,6,0,6)
rolldice(1,6,1,6)
rolldice(1,6,2,6)
rolldice(1,6,3,6)

print("\n")
print("2D6 success on 6")

rolldice(2,6,0,6)
rolldice(2,6,1,6)
rolldice(2,6,2,6)
rolldice(2,6,3,6)

print("\n")
print("3D6 success on 6")

rolldice(3,6,0,6)
rolldice(3,6,1,6)
rolldice(3,6,2,6)
rolldice(3,6,3,6)