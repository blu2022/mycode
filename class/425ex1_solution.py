#!/usr/bin/env python3
import sys
import time   # fix: need to import a module in order to use it.
# there's nothing wrong with this function, it's just some cool code!

# need to define outside of both functions and before either are defined
num_dict= {"1":"great","2":"awesome","3":"superb"}

def print1by1(text, delay=0.1):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def name_grabber():
    # uh oh! this while loop should force the user to answer again
    # if the user DOESN'T enter a name and DOESN'T pick a number
    # between 1 and 3!
    name = ''
    num = ''
    
    while name == '':
        name= input("What is your name?\n>")
    while num not in num_dict:
        num= input("Pick a number between 1 and 3")
        #if num in num_dict):
    return name, num

def main():
    # two kinds of variables!
    # local and global
    # scope
    # local -- var known only in the function they are defined
    # global -- var known in every part of the code.
    name, num= name_grabber() # HINT: python error tracing doesn't always get the line number correct!
         # hmm, something's missing in that open() function...
    with open("horoscope.txt", "w") as fileobj:  # if there is no "w", it will be "r" by default.
        fileobj.write(f"{name}, I predict today will be {num_dict[num].upper()}!\n")

    # Not an error per se, but it's undesirable that
    # this gets written out with no spaces!
    # Fix the for loop to give a nicer output!
    for x in ["YOUR", "FUTURE", "HAS", "BEEN", "WRITTEN", "TO", "HOROSCOPE.TXT..."]:
        print1by1(x + " ")
    print()
if __name__ == "__main__":
    main()