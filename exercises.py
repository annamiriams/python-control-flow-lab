# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

#-----------------------------------------------------------------------------------------------------

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    # Refactored original check for vowels with this list.
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    while True: 
        letter = input('Enter a letter (or "quit"): ').lower()

        if letter == 'quit':
            print('See ya!')
            break
        elif not letter.isalpha():
            print(f'{letter} is not a letter. Please try again.')  
        elif len(letter) != 1:
            print('Looks like you entered more than one letter. Try again!')
        
        # This works but seems a little ridiculous...
        # elif ('a' in letter) or ('e' in letter) or ('i' in letter) or ('o' in letter) or ('u' in letter):
        # Refactored:
        elif letter in vowels:
            print(f'The letter {letter} is a vowel.')
        else: 
            print(f'The letter {letter} is a consonant.')
    
# Call the function
check_letter()

# https://stackoverflow.com/questions/32792554/how-do-i-provide-error-checking-to-ensure-user-input-only-allows-letters-and-pro

# https://brainly.com/question/22294497

#-----------------------------------------------------------------------------------------------------
