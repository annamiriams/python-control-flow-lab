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

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    age = input('Enter your age to see if you\'re old enough to vote: ')
    voting_age = 18
    
    if age.isalpha():
        print('Oops! Looks like you entered a non-numeric value. Try adding a valid age next time.')
    elif int(age) <= 0:
        print('Oops! Try adding a valid age next time.')
    elif int(age) >= voting_age:
        print('Looks like you\'re old enough to vote!')
    elif int(age) > 0 and int(age) < voting_age:
        print('You\'ve still got a few years before you can vote!')
    else:
        print('There was an error. Please try again!')

# Call the function
check_voting_eligibility()

# https://www.w3schools.com/python/ref_func_int.asp

#-----------------------------------------------------------------------------------------------------

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_age_input = input('Input a dog\'s age: ')
    
    if dog_age_input.isalpha():
        print('Oops! Make sure to enter a number for your dog\'s age. Try again!')
    else: 
        dog_age = int(dog_age_input)
        
        if dog_age < 0:
            print('Oops! Make sure to enter a valid age. Try again!')
        elif dog_age <= 2:
            print(f'The dog\'s age in dog years is {dog_age * 10}.')
        else:
            print(f'The dog\'s age in dog years is {20 + ((dog_age - 2) * 7)}.')

# Call the function
calculate_dog_years()

#-----------------------------------------------------------------------------------------------------

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    
    # Original code
    # temp_gage = input('Is it cold outside?: ').lower()
    # if temp_gage =='yes':
    #     is_cold = True
    # elif temp_gage == 'no':
    #     is_cold = False
    # else: 
    #     print('Make sure to answer "yes" or "no."')
        
    # rain_gage = input('Is it raining outside?: ').lower()
    # if rain_gage == 'yes':
    #     is_raining = True
    # elif rain_gage == 'no':
    #     is_raining = False
    # else: 
    #     print('Make sure to answer "yes" or "no."')
        
    # if is_cold and is_raining:
    #     print('Wear a waterproof coat.')
    # elif is_cold and not is_raining:
    #     print('Wear a warm coat.')
    # elif not is_cold and is_raining:
    #     print('Carry an umbrella.')
    # else:
    #     print('Wear light clothing.')
        
    # Refactored code:
    possible_answers = ['yes', 'no']
    temp_gage = input('Is it cold outside?: ').lower()
    rain_gage = input('Is it raining outside?: ').lower()
    
    if (temp_gage not in possible_answers) or (rain_gage not in possible_answers):
        print('Oops! Make sure to only answer "yes" or "no." Try again!')
    elif temp_gage == 'yes' and rain_gage == 'yes':
        print('Wear a waterproof coat.')
    elif temp_gage == 'yes' and rain_gage == 'no':
        print('Wear a warm coat.')
    elif temp_gage == 'no' and rain_gage == 'yes':
        print('Carry an umbrella.')
    else:
        print('Wear light clothing.')

# Call the function
weather_advice()

#-----------------------------------------------------------------------------------------------------

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    
    while True:
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month = input('Enter the month of the year (Jan - Dec) (or "quit"): ').capitalize()
        
        if month == 'Quit':
            print('See ya!')
            break
        elif month not in months:
            print('Oops! That isn\'t a valid month. Try again!')
            break
        else:
            day_input = input('Enter the day of the month: ')
        
        if day_input.isalpha():
            print('Oops! Make sure to enter a number for the day. Try again!')
            break
        else: 
            day = int(day_input)
            
            if day < 1 or day > 31:
                print('Oops! That day is out of the expected range. Try again!')
            else: 
                
                # Original code:
                # if (month == 'Jan') or (month == 'Feb'):
                #     print(f'{month} {day} is in winter.')
                # elif (month == 'Dec') and (day >= 21):
                #     print(f'{month} {day} is in winter.')
                # elif (month == 'Mar') and (day <= 19):
                #     print(f'{month} {day} is in winter.')
                    
                # if (month == 'Apr') or (month == 'May'):
                #     print(f'{month} {day} is in spring.')
                # elif (month == 'Mar') and (day >= 20):
                #     print(f'{month} {day} is in spring.')
                # elif (month == 'Jun') and (day <= 20):
                #     print(f'{month} {day} is in spring.')
                    
                # if (month == 'Jul') or (month == 'Aug'):
                #     print(f'{month} {day} is in summer.')
                # elif (month == 'Jun') and (day >= 21):
                #     print(f'{month} {day} is in summer.')
                # elif (month == 'Sep') and (day <= 21):
                #     print(f'{month} {day} is in summer.')
                    
                # if (month == 'Oct') or (month == 'Nov'):
                #     print(f'{month} {day} is in fall.')
                # elif (month == 'Sep') and (day >= 22):
                #     print(f'{month} {day} is in fall.')
                # elif (month == 'Dec') and (day <= 20):
                #     print(f'{month} {day} is in fall.')
          
                # Refactored code using 'in' and fewer duplicate prints:
                if ((month in ['Jan', 'Feb']) or
                    (month == 'Dec') and (day >= 21) or
                    (month == 'Mar') and (day <= 19)):
                    print(f'{month} {day} is in winter.')
                
                if ((month in ['Apr', 'May']) or
                    (month == 'Mar') and (day >= 20) or
                    (month == 'Jun') and (day <= 20)):
                    print(f'{month} {day} is in spring.')
                
                if ((month in ['Jul', 'Aug']) or 
                    (month == 'Jun') and (day >= 21) or 
                    (month == 'Sep') and (day <= 21)):
                    print(f'{month} {day} is in summer.')
                    
                if ((month in ['Oct', 'Nov']) or 
                    (month == 'Sep') and (day >= 22) or 
                    (month == 'Dec') and (day <= 20)):
                    print(f'{month} {day} is in fall.')
                    
# Call the function
determine_season()
