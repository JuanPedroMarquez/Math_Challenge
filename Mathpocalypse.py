# This script is a math test generator that will create a list of mathematical problems that you must solve in the shortest time possible.
import random
import time

# PARAMETERS OF THE PROBLEM
## These are the operations that the script will use to generate the problems
Operators = ["+", "-", "*", "**"] # List of operators: sum, subtraction, multiplication and power

## These are the minimum and maximum numbers that will appear in the problems
minimum_operand = 0 # Minimum value of the operands in common operations
maximum_operand = 100 # Maximum value of the operands in common operations
maximum_power_operand = 5 # Maximum value of the opperands in powers
maximum_multiplication_operand = 15 # Maximum value of the opperands in multiplication
number_of_problems = 15 # Number of problems to solve

# FUNCTION TO GENERATE A PROBLEM
## This function generates a problem with random numbers and operators. It returns the expression and the answer.
## It also reduces the maximum value of the operands in some cases to avoid huge numbers and make the problems easier.
def generate_problem():
    operator = random.choice(Operators) # Choose a random operator from the list

    if operator == "**": # If the problem is a power, we reduce both maximum opperands to avoid huge numbers and make the problem easier

        left = random.randint(minimum_operand, maximum_power_operand) # Generate a random number between the minimum and maximum value
        right = random.randint(minimum_operand, maximum_power_operand) # Generate a random number between the minimum and maximum value
    
    elif operator == "*": # If the problem is a multiplication, we reduce one of the opperands for the same reason
        left = random.randint(minimum_operand, maximum_operand)
        right = random.randint(minimum_operand, maximum_multiplication_operand)
    
    else: # In the rest of the cases, we generate the numbers between the normal minimum and maximum values
        left = random.randint(minimum_operand, maximum_operand) # Generate a random number between the minimum and maximum value
        right = random.randint(minimum_operand, maximum_operand) # Generate a random number between the minimum and maximum value

    expression = str(left) + " " + operator + " " + str(right) # Create the expression showed to the user
    answer = eval(expression) # Solve the problem.
    return expression, answer # Return the expression

# SARTING THE TEST
wrong_exercises = 0 # Variable to store the number of wrong exercises
input("Press any key to start the trial! You may use paper and pen if you want") # Wait for the user to press any key
print()
print("------------ Good luck! ------------") 
print()
start_time = time.time() # Start the timer

for i in range(number_of_problems): # Loop to generate as many numbers as indicated in the parameters of the test
    expression, answer = generate_problem() # Call the function to generate a problem
    while True: # While the answer is not correct, keep asking the same question
        attempt = input("Problem number " + str(i+1) + ": How much is " + expression + " ? Answer: ") # Print the question and wait for the user to input the answer
        if attempt == str(answer): # If the answer is correct, break the while loop and generate next problem
            break
        else: # In bad attempts, the wrong exercises counter is increased by 1
            wrong_exercises += 1

end_time = time.time() # Stop the timer
test_time = end_time - start_time # Calculate the time spent to solve the problems as the differences between the finish and the start

print()
print("------------ Finished! ------------")
print()

# FINAL RESULTS
print("Nice work! You finished the test in", round(test_time, 2), "seconds! That's", round(test_time/number_of_problems, 2), "seconds per problem! You got", wrong_exercises, "failed attempts") # Print the results