Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> 
>>> def roll(sides=6) :
	num_rolled = random.randint(1,sides)
	return num_rolled

>>> def main() :
	sides = 6
	rolling = True
	while rolling:
		roll_again = input("Ready to roll? ENTER=Roll. Q=Quit. ")
		if roll_again.lower() != "q":
			num_rolled = roll(sides)
			print("You rolled a", num_rolled)
		else:
			rolling = False

			
>>> print("Thanks for playing! You were on a roll!")
Thanks for playing! You were on a roll!
>>> 
>>> main()
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 4
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 1
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 2
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 3
Ready to roll? ENTER=Roll. Q=Quit. q
>>> q
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    q
NameError: name 'q' is not defined
>>> main()
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 3
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 1
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 5
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 2
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 6
Ready to roll? ENTER=Roll. Q=Quit. q
>>> main()
Ready to roll? ENTER=Roll. Q=Quit. NameError: name 'q' is not defined
You rolled a 3
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 2
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 6
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 1
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 3
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 5
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 4
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 3
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 6
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 1

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 3
Ready to roll? ENTER=Roll. Q=Quit. 

You rolled a 6

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 4

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 5
Ready to roll? ENTER=Roll. Q=Quit. 

You rolled a 3

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 1

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 3

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 2

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 5

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 6

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a
 2

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 2

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 2

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 6
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 6
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 2

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 5

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 2
Ready to roll? ENTER=Roll. Q=Quit. 

You rolled a
 3

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 4

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 2

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 1

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a
 6
Ready to roll? ENTER=Roll. Q=Quit. 

You rolled a 3

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 4

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 6
Ready to roll? ENTER=Roll. Q=Quit. 

You rolled a 2

Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 4
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 1
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 3
Ready to roll? ENTER=Roll. Q=Quit. 
You rolled a 4
Ready to roll? ENTER=Roll. Q=Quit. Q
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 



>>> 
>>> 


>>> 


>>> 

>>> 

>>> 

>>> 

>>> 


>>> 
>>> 

>>> 


>>> 

>>> 

>>> 

>>> 


>>> 
>>> 

>>> 


>>> 


>>> 
>>> 
>>> 
