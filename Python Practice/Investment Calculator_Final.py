# Kiwisaver Investment Calculator

# Defining our variables
principle = 0
rate = 0
time = 0

def interest_rate(strategy): # Defining our strategy values for calculations later
    rates = {
        1: ("Conservative", 0.04),
        2: ("Standard", 0.06),
        3: ("Growth", 0.08),
    }
    return rates[strategy]  # Returns the defined/dictionary value


# Calculator code

while True:  # Program start. The whole calculator is running in an outer loop of "while True." corresponding to lines 105-113. 
             # The condition is also True when you first boot up the program.
    print("Welcome to the KiwiSaver Investment Calculator.")  # Welcome message

    while True:  # Prompt for principle value input. "while" runs this loop until a condition has been satisfied with a valid input.
        try:
            principle = float(input("Please enter the investment principle amount: $"))
            if principle >= 1: # This if statement works with the "while True" statement if the value entered is correct
                print(f"You have entered ${principle:.2f}.") # Confirmation of value entered
                break # breaks the loop to continue the program
            else: # if the "if" condition isn't met, it runs the else condition. 
                print("Please enter a valid investment amount (1 or greater).") 
        except ValueError: # This condition protects the code crashing if someone enters an incorrect value. 
            print("Please enter a valid number. (Example: 1000)") # prompts the user for correct value

    while True: # "while" runs this loop until a condition has been satisfied with a valid input.
        try:
            time = int(input("Please enter your investment term (years): "))
            if 1 <= time <= 45: # the time input value must be between 1 and 45.
                print(f"You've selected {time} years as your investment term.") # Confirmation message embedded as an f string using their input value in the printed message.
                break # exits the "while" loop because the input value is valid
            else: #runs this condtion because the input value is not valid
                print("The value entered must be between 1 and 45.")
        except ValueError: # This function picks up on an incorrect input value (! or K) as the input question asks for an integer.
            print("You can only enter whole numbers. Please try again.") #prompts the user for correct value

    # --- Strategy Comparison Summary ---
    all_strategies = [1, 2, 3] # This is now referring back to lines 8-14 where we defined the strategies above, encased in a list.
    print()
    print("---------- Investment Comparison Summary ----------")
    print()
    print(f"\n{'Strategy':<16} {'Rate':>6} {'Final Balance':>16} {'Total Interest':>15}") # This section prints the first table, comparing the strategies and their investment return amounts in $.
    print("-" * 57)

    for s in all_strategies: # running calculations based on the assigned values of the investment strategies and the two input values (principle, years)
        strategy_name, annual_rate = interest_rate(s)
        total = principle * pow((1 + annual_rate), time)
        growth = total - principle
        print(f"{strategy_name:<16} {str(int(annual_rate*100))+'%':<7} {'$'+f'{total:,.2f}':<16} {'$'+f'{growth:,.2f}':<15}") # using the :.2f function to truncate the return values to 2 decimal places for finance.
                                                                                                                              # {str(int)} converts the integers and values into printable strings for the output
    print("-" * 57) # printing "-" 57x as decorative text.

    # --- Ask the user for a breakdown first before selecting a strategy to display breakdown results ---
    while True: # This creates a y/n logic answer to tell the code whether or not to execute the breakdown segment. 
        annual_breakdown = input("\nWould you like a year-by-year breakdown? (Y/N): ").strip().upper()
        if annual_breakdown in ("Y", "N"):
            break
        print("Please enter Y / N")

    if annual_breakdown == "Y": # nested inside the "breakdown" loop - triggered by "y"

        # --- Strategy Selection only shown if breakdown requested ---
        print("\nSelect a strategy to break down:")
        print("1. Conservative (4%)")
        print("2. Standard (6%)")
        print("3. Growth (8%)")

        while True: # This is the breakdown triggered by the Y/N selection above. This asks the user to select the strategy which will be broken down.
            try:
                strategy = int(input("Choose an option (1-3): "))
                if strategy in (1, 2, 3):
                    strategy_name, annual_rate = interest_rate(strategy)
                    print(f"You selected the {strategy_name} investment strategy.")
                    break
                else:
                    print("Please choose a valid option (1-3).")
            except ValueError: #this is a failsafe incase the user enters and incorrect value. This is so the program doesn't break.
                print("You have entered an invalid value. Please select again.")

        total = principle * pow((1 + annual_rate), time) # calculation for the total variable

        print(f"\n{'Year':<8} {'Balance':<15} {'Interest Earned':<18} {'Total Growth':<15}") # This prints the table to display the broken down output
        print("-" * 60)

        for year in range(1, time + 1): # breakdown calculation which is then reiterated each year/period to show compound interest
            balance = principle * pow((1 + annual_rate), year)
            interest_earned = balance - principle * pow((1 + annual_rate), year - 1)
            total_growth = balance - principle
            print(f"{year:<8} {'$'+f'{balance:,.2f}':<16} {'$'+f'{interest_earned:,.2f}':<19} {'$'+f'{total_growth:,.2f}':<15}")

        print("-" * 60)
        print(f"\nFinal Balance ({strategy_name}): ${total:,.2f}.")

    else:
        print("No breakdown selected.")

    # Asks user if they'd like to re-use the calculator.
    while True:
        again = input("Would you like to use the calculator again? Y/N: ").strip().lower() # Strip and Lower automatically format the user answer to work as an input

        if again == "y":
            break  # breaks the inner loop to restart the program. Resets the values to 0 so it can rerun the calculations.
        elif again == "n":
            print()
            print("Thank you. Goodbye.")
            exit()  # Ends the program
        else:
            print("Please enter Y / N") # prompting user for correct input