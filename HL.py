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

def int_check(questionint, low=None, high=None, exit_code=None):

    while True:
            
        if low is None and high is None:
            error = "Please enter an integer"

        elif low is not None and high is None:
            error = (f"Please enter an integer that is more than or equal to {low}")

        else:
            error = (f"Please enter an integer that is between {low} and {high}. (Inclusive)")


        while True:
            responseint = input(questionint).lower()

            if responseint == exit_code:
                return responseint

            try:
                responseint = int(responseint)

                if low is not None and responseint < low:
                    print(error)

                elif high is not None and responseint > high:
                    print(error)

                else:
                    return responseint

            except ValueError:
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
guess = ""

want_instructions = string_checker("Do you want to see the instructions? ")
if want_instructions == "yes":
    instruction()

wanted_rounds = int_check("\nHow many rounds? (Press <enter> for infinite): ", low=1, exit_code="")

if wanted_rounds == "":
    mode = "infinite"

low_num = int_check("Low Number? ")
high_num = int_check("High Number? ", low=low_num+1)

while rounds_played < round_number or mode == "infinite":
