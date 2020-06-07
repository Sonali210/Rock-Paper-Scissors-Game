import random 
print("Let's start the game\n")
while True: 
	print("Enter number: \n\n 1. Rock \n 2. paper \n 3. scissors \n") 
	# take the input from user 
	choice = int(input("User turn: ")) 

	while choice > 3 or choice < 1: 
		choice = int(input("enter valid input\n"))
	if choice == 1: 
		choice_name = 'Rock'
	elif choice == 2: 
		choice_name = 'paper'
	else: 
		choice_name = 'scissors'

	print("your choice is: " + choice_name) 
	print("\nNow its computer turn.......") 

	comp_choice = random.randint(1, 3) 
	
	while comp_choice == choice: 
		comp_choice = random.randint(1, 3) 

	if comp_choice == 1: 
		comp_choice_name = 'Rock'
	elif comp_choice == 2: 
		comp_choice_name = 'paper'
	else: 
		comp_choice_name = 'scissor'
		
	print("Computer choice is: " + comp_choice_name + "\n") 

	# condition for winning 
	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice == 1)): 
		result = "paper"
		
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)): 
		result = "Rock"
	else: 
		result = "scissor"

	# Printing either user or computer wins 
	if result == choice_name: 
		print("You win \n") 
	else: 
		print("Computer wins \n") 
		
	print("Do you want to play again? (Y/N) \n") 
	ans = input() 
	if ans == 'n' or ans == 'N': 
		break
print("\nThanks for playing") 
print("\n;)\n")
import tkinter as tk 
r = tk.Tk() 
r.title(' ') 
button = tk.Button(r, text='EXIT', width=25, command=r.destroy) 
button.pack() 
r.mainloop() 


