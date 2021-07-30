from art import logo

# addition function
def add(num1, num2):
    return num1 + num2

# subtraction function
def subtract(num1, num2):
    return num1 - num2

# multiplacation function
def multiply(num1, num2):
    return num1 * num2

# division function
def divide(num1, num2):
    return num1 / num2

# dictionary to assign each symbol to it's operator name
operator_functions = {
  "+": add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide
  }

# claculator function
def calculator():
  print(logo)
  first_num = float(input("What is the first number?: "))
  # print each operator symbol for options after inputting the first number
  for sym in operator_functions:
      print(sym)
  keep_going = True

  while keep_going:
    operation = input("Pick an operation: ")
    second_num = float(input("What is the next number?: "))
    # set calc_function variable to the name of the operator symbol
    calc_function = operator_functions[operation]
    # user operator name to call the function with the numbers and set it in variable answer
    answer = calc_function(first_num, second_num)

    print(f"{first_num} {operation1} {second_num} = {answer}")
    
    # ask if the user would like to continue calculating or start a new calculation
    yes_no = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if yes_no == 'y':
      first_num = answer
    # stop the loop and restart the program
    else:
      keep_going = False
      calculator()
# original function call
calculator()
