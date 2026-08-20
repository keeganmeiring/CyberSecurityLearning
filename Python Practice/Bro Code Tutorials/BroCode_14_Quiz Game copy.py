# Python Quiz Game

questions = ("How many minutes are there in an hour?: ", # Tuple() (type of list/collection) which cannot change or be edited, whuch functions as our questions database
             "How many legs do dogs have?: ",
             "How many lives do cats have?: ",
             "What is the fastest legal speed limit in NZ?: ",
             "How many meters are in a kilometer?: ")

options = (("A. 20", "B. 23", "C. 30", "D. 60"), # This is the same as "questions" where this tuple() is our correct base for options. These are also a tuple as they cannot be edited.
           ("A. 1", "B. 2", "C. 4", "D. 0"), # each option set is paired as a tuple, within the options tuple.
           ("A. 23", "B. 1", "C. 7", "D. 9"), 
           ("A. 50km/hr", "B. 80km/hr", "C. 110km/hr", "D. 142km/hr"), 
           ("A. 10", "B. 100", "C. 1000", "D. 762"))

answers = ("D", "C", "D", "C", "C") # These are a tuple() because they are the correct answers, in order of the questions, and cannot be edited.
guesses = [] # These guesses will be entered by the user as they're prompted with each question. These are a [list] because they can be appended and edited.
score = 0 # starting score value
question_num = 0 # Starting question value
# True = "Y"

while True:
    for question in questions: 
        print("=" * 20) # "Decorative" text as a divider.
        print(question)
        for option in options[question_num]:
            print(option)
        
        guess = input("Enter (A, B, C, D): ").upper() # .upper converts any text input from the user to upper case so that the input is correct. b -> B and the program recognizes and validates it.
        guesses.append(guess) # Append adds more guesses to the guess list in real time as the user answers questions
        if guess  == answers[question_num]: # if the guess IS the same as the correlating correct answer aligned to the question number.
            score += 1 # += adds each correct score to the score value. Every time a user gets an answer right, it + 1. Or it = to stay the same if the next answer is incorrect, keeping the previous value.
            print("Correct.")
        else: 
            print("That answer is incorrect.")  
            print(f"{answers[question_num]} is the correct answer. ")  # This f string embeds two values together so that it aligns the correct answer to the question, providing feedback to the user.
        question_num += 1 # this incrementally goes through the potential answers to match correctly to the question. Otherwise, it shows the same answer options for every question.
            
        if score == 1: # feedback to the user in real time after each question. 
            print(f"Your total score is: {score}")
        elif score == 2:
            print(f"Your total score is: {score}")   
        elif score == 3:
            print(f"Your total score is: {score}")
        elif score == 4:
            print(f"Your total score is: {score}")
        elif score == 5:
            print(f"Your total score is: {score}. Congratulations! You got all of the questions correct.")  
        else: 
            print("You did not get any correct. Try again.")
   
   # Ask the user if they'd like to replay the quiz
    while True: 
            again = input("Would you like to play again? (Y/N): ").upper()
            if again == "Y":
                break
                question_num = 0
            else:
                print("Thank you for playing. Goodbye.")
                exit()