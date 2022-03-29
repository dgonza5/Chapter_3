# grade = 90
# condition = grade >=90
# if condition:
#     print("your grade is A") # execute when true
# else: 
#     print ("Your grade is not A") # execute when false

# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))
# try:
#     print("1", isinstance(num1, str))
#     print("2", isinstance(num2, str))
#     if isinstance(num1,str) or isinstance(num2, str):
#         print("Data type not allowed! Please specify numeric value.")
#     else:
#         if num1 > num2:
#             largerVal = num1
#         else:
#             largerVal = num2
#         print("The larger value is " + str(largerVal)) 
# except: 
#     print("Data not allowed!")


# if num1 > num2:
#     largerVal = num1
# else:
#     largerVal = num2
#     print("The larger value is " + str(largerVal)) 

# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")

# answer = eval(input("How many gallons does a ten-gallon hat hold?"))
# if (.5 <= answer <= 1):
#     print("Good, ", end="")
# else:
#     print("no, ", end="")
# print("it holds about 3/4 of a gallon.")

# def is_greater_than10():
#     answer = eval(input("How many gallons does a ten-gallon hat hold"))
#     if answer > 10:
#         return True
#     return False 

# first_num = eval(input("Enter first number: "))
# second_num = eval(input("Enter second number: "))
# third_num = eval(input("Enter third number: "))

# max = first_num

# if second_num > max:
#     max = second_num
# if third_num > max:
#     max = third_num
# print("The largest numberof the three number is: " + str(max) + ".")

# numbers = [1, 20, 90]

# print(max(numbers))

# numbers = []
# first_num = eval(input("Enter first number: "))
# second_num = eval(input("Enter second number: "))
# third_num = eval(input("Enter third number: "))
# numbers.append(first_num)
# numbers.append(second_num)
# numbers.append(third_num)

# print("The largest of the three number is " + str(max(numbers)) + ".")

# msg = "The largest of the three number is " + str(max(numbers)) + "."
# print(msg)

## Interpret weather beacon. 
# Obtain color and mode.
# color = input("Enter a color (BLUE or RED): ")
# mode = input("Enter a mode (STEADY or FLASHING): ")
# color = color.upper()
# mode = mode.upper()

# # Analyze responses and display weather forecast. 
# result = ""
# if color == "BLUE":
#     if mode == "STEADY":
#         result = "Clear View."
#     else:   # mode is FLASHING
#         result = "Clouds Due."
# else:   # color is RED
#     if mode == "STEADY":
#         result = "Rain Ahead."
#     else:   # mode is FLASHING
#         result = "Snow Ahead."
# print("The weather forecast is", result)

# ## Evaluate profit. 
# # Obtain input from user. 
# costs = eval(input("Enter total costs: "))
# revenue = eval(input("Enter total revenue: "))

# # Determine and display profit or loss. 
# if costs == revenue:
#     result = "Break even."
# else:
#     if costs < revenue:
#         profit = revenue - costs 
#         result = "Profit is ${0:,.2f}.".format(profit)
#     else:
#         lost = costs - revenue
#         result = "Loss is ${0:,.2f}.".format(loss)
# print(result)


# ## Evaluate profit. 
# # Obtain input from user. 
# costs = eval(input("Enter total costs: "))
# revenue = eval(input("Enter total revenue: "))

# # Determine and display profit or loss. 
# if costs == revenue:
#     print("Break even.")
# result = "is ${0:,.2f}".format(revenue - costs)
# if (revenue - costs) < 0:
#         print("Loss " + result)
# print("Profit " + result)


## Determine the larger of two numbers.
# Obtain the two numbers from the user. 

# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))

# # Determin and display the larger value. 

# if num1 > num2:
#     print("The larger value is", str(num1) + ".")
# elif num2 > num1:
#     print("The larger value is", str(num2) + ".")
# else: 
#     print("The two values are equal. ")

## Bestow graduation honors. 
# Request grade point average. 

# gpa = eval(input("Enter your GPA: "))

# # Determine if honors are warranted.

# if gpa >= 3.9:
#     honors = " summa cum laude."
# elif gpa >= 3.6:
#     honors = " magna cun laude."
# elif gpa >= 3.3:
#     honors = " cum laude."
# else:
#     honors = "."

# # Display conculsions 

# print("You graduated" + honors)

# ## Request two numbers and find thier sum. Validate the input.
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")

# # Display sum if enteries are vaild. Otherwise, inform the user where invalid enteries are made. 

# if num1.isdigit() and num2.isdigit():
#     print("The sum is", str(eval(num1) + eval(num2)) + ".")
# elif not num1.isdigit():
#     if not num2.isdigit():
#         print("Neither entry was a proper number. ")
#     print("The first entry was not a proper number.")
# print("The second entry was not a proper number.")

## Illustrate Boolean values. 
if 7:
    print("A nonzero number is true.")
else:
    print("The number zero is flase.")
if []:
    print("A nonempty list is a true.")
else:
    print("An empty list is false.")
if ["Spam"]:
    print("A nonempty list is true.")
else:
    print("The empty list is false. ")