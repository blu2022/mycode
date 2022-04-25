#!/usr/bin/env python3


#part1
with open("345-0.txt", "r") as Dracula:
    round = 0
    with open("vampytimes.txt", "w") as Dracula2:
    # part2
        for line in Dracula:
    
        #print(line, end="")
        # part3 & part4
            if "vampire" in line.lower():
            #print(line, end="")
            #part6
            
                Dracula2.write(line)
                round += 1
                
#part5
print(round)


        