
import random
digits = list(range(10))
random.shuffle(digits)
number=digits[:3]

def check(n) :
	if number[0]==n[0] and number[1]==n[1] and number[2]==n[2] :
		return "correct guess"
	elif number[0]==n[0] or number[1]==n[1] or number[2]==n[2] :
		return "digit is correct and at the right position"
	else :
		for i in number :
			if i==n[0] or i==n[1] or i==n[2] :
				return "digit is correct but at the wrong position"

	return "digits are incorrect"
c=0
while(True):
	c+=1
	g = input("What is your guess? ")
	guess=[]
	guess.append(g/100)
	guess.append((g%100)/10)
	guess.append(g%10)
	s=check(guess)
	print(s)
	if s == "correct guess":
		break
print("you solved in {} attempt").format(c)
