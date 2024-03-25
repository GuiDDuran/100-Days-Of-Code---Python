############DEBUGGING#####################

# Describe Problem
#def my_function():
#  for i in range(1, 21):  # It wasn't including the 20, it was only going until 19.
#    if i == 20:
#      print("You got it")
#my_function()

# Reproduce the Bug
#from random import randint
#dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(0, 5)  # We had to fix the range, to make sure that all the dices were included.
#print(dice_imgs[dice_num])

# Play Computer
#year = int(input("What's your year of birth?"))
#if year > 1980 and year < 1994:
#  print("You are a millenial.")
#elif year >= 1994:  # I just changed the condition, including the 1994
#  print("You are a Gen Z.")

# Fix the Errors
# age = int(input("How old are you?"))  # I turned it into an integer.
# if age > 18:
#   print(f"You can drive at age {age}.")  # I had to put it into the if statment and also tranform into an f string sentence.

#Print is Your Friend
#pages = 0
#word_per_page = 0
#pages = int(input("Number of pages: "))
#word_per_page = int(input("Number of words per page: "))  # It had two equal signs and by using the print statments I could find the issue.
#total_words = pages * word_per_page
#print(f"pages = {pages}")
#print(f"word_per_pages = {word_per_pages}")
#print(total_words)

#Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)  # It had to be inside the for loop.
#   print(b_list)

# mutate([1,2,3,5,8,13])