
# num = 0 # iterator / incrementor
# while num <= 5:
#     print("Hello World! " + str(num))
#     num += 1 # same thing as i = i + 1



# ## Movie Quotations
# from http.client import responses


# print("This program displays a famous movie quoation.")
# responses = ('1', '2', '3')
# response = '0'
# while response not in responses:
#     response = input("Enter 1, 2, or, 3: ")
#     if response == '1':
#         print("Plastics.")
#     elif response == '2':
#         print("Rosebud.")
#     elif response == '3':
#         print("That's all folks.")



# count = 0
# total = 0
# print("(Enter -1 to terminate program)")
# num = eval(input("Enter a nonnegative number: ")) # 5 
# min = num
# max = num
# while num != -1:
#     count += 1 
#     total += num 
#     if num < min: 
#         min = num 
#     if num > max: 
#         max = num
#     num = eval(input("Enter a nonnegative number: ")) # 5    
# if count > 0:
#     print("Min: ", str(min))
#     print("Max: ", str(max))
#     print("Average: ", str(total/ count))
# else:
#     print("No nonnegative numbers were entered")


# list1 = [300, 1, 2, 3, 60]
# list1.sort() # [1, 2, 3, 60, 300]
# list1[0] #1 - lowest number in the list
# list1[-1] # 300 - largest number in the list

# i = 0
# balance = eval(input("Enter initial deposit: "))
# rate = eval(input("Enter the annual rate of return: "))
# while balance < 1000000: 
#     balance += .04 * balance # balance = (balance * .04)
#     i += 1
# print("In ", str(i), "years you will have a million dollars")

# list1 = []
# while True:
#     num = eval(input("Enter a nonnegative number: "))
#     if num == -1:
#         break # Immediately terminate the 
#     list1.append(num)

# print(list1)

""""
Display facts about the United States
"""

print("Enter a number from the menu to obtain a fact")
print("about the United States or to exit the program. \n")
print("1. Captial")
print("2. National Bird")
print("3. National Flower")
print("4. Quit\n")
while True:
    num = int(input("Make a selection from the menu: "))
    if num == 1:
        print("Washington, DC is the captial of the United States. ")
    elif num == 2:
        print("The American Bald Eagle is the national bird. ")
    elif num == 3:
        print("The Rose is the national flower.")
    elif num == 4:
        break