import random
# use split string method to split names stored in the list
names_string = input("Hi!, type in your names, separated by a comma. ")
names = names_string.split(", ")

#get the number of items in your list
x = len(names)
#get random number between 0 and length minus 1
random_index = random.randint(0, x-1)
payer = names[random_index]

print("The person paying the bill is " + payer + "." + " Thank you!")