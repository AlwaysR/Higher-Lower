import random

def instruction():
    print("""

**** Instructions ****

Good Luck!
""")

def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"
    
    while True:

        user_response = input(question).lower()
        
        for item in valid_ans:
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        print(error)
        print()

def int_check(questionint, error):

    while True:
        try:
            response = input(questionint)
            
            response = int(response)
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            if len(response) == 0:
                return "enter"
            print(error)

#Main code
print()
print("Welcome to the HIGHER or LOWER game!")
print()

#Variables
mode = "normal"
round_number = 0
rounds_wanted_noninfinite = ""
history = []
chicken = "no"
selection = 0

want_instructions = string_checker("Do you want to see the instructions? ")
if want_instructions == "yes":
    instruction()

wanted_rounds = int_check("\nHow many rounds? (Press <enter> for infinite): ", "Please press <enter> for infinite mode or enter a number")

#looping rounds
if wanted_rounds == "enter":
    mode = "Infinite"
    wanted_rounds = 1

else:
    mode = "Normal"
    rounds_wanted_noninfinite = f"of {wanted_rounds}"


while round_number < wanted_rounds or mode == "Infinite":
    print(f"\n*** Round {round_number + 1} {rounds_wanted_noninfinite}| {mode} mode ***\n")

    if selection == "xxx":
        break

    round_number += 1

    round_feedback = ""
    history_item = ""
    history.append(history_item)
if round_number == 0:
    chicken = "yes"
    print("You chickened out and didnt play any rounds in infinite mode.")

if chicken == "no":
    display_history = string_checker("Do you want to see your game history? ")
    if display_history == "yes":
        print("Statistics:")


    print("Thank you for playing!")
