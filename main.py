def convert_to_math(num_input1, num_input2, operator_input):
  if operator_input == '+':
      sub_total = num_input1 + num_input2
  elif operator_input == '-':
      sub_total = num_input1 - num_input2
  elif operator_input == '/':
      sub_total = num_input1 / num_input2
  elif operator_input == '*':
      sub_total = num_input1 * num_input2
  return sub_total

running = True
use_total_as_first_number = False
total = 0

while running:
  if not use_total_as_first_number:
      first_number = float(input("What's your first number? \n"))
  else:
      first_number = total

  while True:
      operator = input("+ - / * \nChoose an operator \n")
      if operator in ['+', '-', '/', '*']:
          break  # Exit the loop if input is valid
      else:
          print("Invalid operator.\n")

  second_number = float(input("What's your second number? \n"))

  total = convert_to_math(first_number, second_number, operator)
  print(total)

  user_input = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation. ")
  if user_input == 'y':
      use_total_as_first_number = True
  elif user_input == 'n':
      use_total_as_first_number = False
      running = False
