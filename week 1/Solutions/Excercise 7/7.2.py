
# Ask the user to enter an input
input = input("Enter an input: ")

# Use an if-elif-else statement to check the input
if input.isdigit():
  # Convert the input to an integer
  n = int(input)
  # Check the sign of n
  if n > 0:
    # Print n is positive
    print(f"{n} is positive")
  elif n < 0:
    # Print n is negative
    print(f"{n} is negative")
  else:
    # Print n is zero
    print(f"{n} is zero")
elif input.isalpha():
  # Print string is not a number
  print("String is not a number")
else:
  # Print invalid input
  print("Invalid input")
