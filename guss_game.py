# Import the random module and alias it as 'rd'
import random as rd

# Generate a random integer between 1 and 100 and assign it to real_value
real_value = rd.randint(1, 100)
print(real_value)  # Print the real_value (for debugging purposes)

# Initialize the count of guesses to 0
count = 0

# Start an infinite loop for the guessing game
while True:
    # Prompt the user to enter their guess and convert it to an integer
    user_input = int(input("Enter your guess: "))
    
    # Increment the count of guesses
    count += 1
    
    # Check if the user's guess is greater than the real value
    if user_input > real_value:
        print(f"Enter lower value: {user_input}")
    
    # Check if the user's guess is less than the real value
    elif user_input < real_value:
        print(f"Enter higher value: {user_input}")
    
    # If the user's guess is equal to the real value, they've guessed correctly
    else:
        print(f"{user_input} == {real_value}. You've guessed it!")
        break  # Exit the loop

# Print the total number of guesses made
print(f"You've made {count} guesses.")
