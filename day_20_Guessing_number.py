# Create a guessing number game where the user have to guess the correct number under following conditions
'''
Max number of guesses should be 9 
print the number of guesses left 
Number of guesses he took to finish 
'''
n = 18
number_of_guesses = 1
while(number_of_guesses < 9):
    guess_number = int(input("Enter the number of your choice"))
    if guess_number > n:
        print("Number too high.....Please input a lower number")
    elif guess_number < n:
        print("Number too low....Please input a higher number")
    else:
        print("congrats!!! You won the game")
        break
    print(f" The number of guesses left are {9-number_of_guesses}")
    number_of_guesses = number_of_guesses+1
if(number_of_guesses > 9):
    print("Game is Over ")
