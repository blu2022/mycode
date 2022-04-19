#!/usr/bin/env python3

# https://github.com/csfeeser/Python/blob/master/challenges/DAY%201%20CONTENT-%20chal02.md

# list1
icecream= ["indentation", "spaces"] 

# list2:
tlgstudents= ["Akino", "Bai", "Carlos", "Dalton", "Dan", "Edith", "Ethan", "Isaiah", "J", "Jessica", "John", "Justin", "Khalil", "Nikk", "Ramesh", "Scotty", "Sergio", "Shawn"]

# Append the integer (INTEGER, not string!) 4 to the list icecream.
icecream.append(4)

# print to check
print(icecream, "to append 4 to the list")

# Include an input asking for a number between 0 and 14. 
# Use this number to identify one of the students from the tlgstudents list!
stdnumber= int(input("Please pick a student number: "))
if(stdnumber > 17):
    print("The number has to be between 0 to 17!")
elif(stdnumber < 0):
    print("The number has to be between 0 to 17!")
else:
    print(f"{tlgstudents[stdnumber]} always uses {icecream[2]} {icecream[1]} to indent!")
