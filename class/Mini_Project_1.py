#!/usr/bin/env python3

# Topic: Bai is looking for a new job. 
# Most of jobs require Bai to relocate. 
# How does Bai make his decision for relocation?

round = 0           # integer round initiated to 0

while True:        # sets up an infinite loop condition
    round += 1     # increase the round counter
    print("Will Bai accept the relocation from a new job?\n")

    # How is the income tax rate level in your state as of Jan 2022?
    # https://taxfoundation.org/publications/state-individual-income-tax-rates-and-brackets/
    # 0-5% low 5%-8% medium 8%-14% high
    Stateincometax= float(input("Please input income tax rate (by %):\n>"))
    
    print("\n"*2)
    # What is the measure of state sales tax rate as of Jan 2022?
    # https://taxfoundation.org/2022-sales-taxes/
    # 0-5% low 5%-8% medium 8%-14%  high  
    Statesalestax= float(input("Please input state sales tax rate (by %):\n>"))
    
    # Sum of State income tax and Sales tax
    Statetaxburden= float(Stateincometax + Statesalestax)

    print("\n"*2)
    # Type the median home price 
    # https://worldpopulationreview.com/state-rankings/median-home-price-by-state
    Median_Home_Price= input("Please input median home price ($):\n>")

#   if function
    if float(Statetaxburden) <= 13 and float(Median_Home_Price) <= 300000: #logic to check if given data meet the conditions
        answer1= input('Is it CONUS?(Y or N)\n>') 
        answer1= answer1.upper()
        if answer1 == "N":
            print('Bai does not want to go OCONUS. Bai will refused this relocation!\n')
            break             # break statement escapes the while loop
        elif answer1 == "Y":     
            print('Bai will accept this relocation!')
            break
        else:
            print('This is an invalid answer. Please restart the script.')
            break             
    elif round == 3:        # logic to ensure round has not yet reached 3
        print(f'Either tax burden of {float(Statetaxburden)} % or home price of {float(Median_Home_Price)} is too high!\nBai will refuse to relocate!\n\n Sorry, you run out of chances. Please restart the script if you want.\n\n')
        break             
    else:                 # if answer was wrong, and round is not yet equal to 3
        print(f'Either tax burden of {float(Statetaxburden)}% or home price of {float(Median_Home_Price)} is too high!\nBai will refuse to relocate!\n\n')
        answer2= input('Do you want to try again?(Y or N)\n>')
        answer2= answer2.upper()
        if answer2 == "N":
            break
        elif answer2 != "Y":
            print('This is an invalid answer. Please restart the script.')
            break
        else:
            print('Let\'s try again!\n')