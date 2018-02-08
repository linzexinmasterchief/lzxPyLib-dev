def isPositive(num = 0.0):
	return num > 0

def isZero(num = 0.0):
	return num == 0

def isNegetive(num = 0.0):
	return num < 0

def compare(firstNum = 0.0, secondNum = 0.0):
	if firstNum > secondNum:
		return 1
	elif secondNum > firstNum:
		return 2
	else:
		return -1