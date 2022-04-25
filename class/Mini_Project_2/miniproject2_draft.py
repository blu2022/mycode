#!/usr/bin/python3
import sys
import os
import random
import time

delay = 1.0

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Adventure Game
==================
Instruction: You are in the center from the beginning.
You can move north/south/west/east to find a way to escape.
hint: Water kills fire.
      fire kills zoobie.
      sword kills zobbie and warrior.
      A good potion will never be green.
      
Commands:
  go [direction]
  get [item]
  use [item]
  teleport
  help
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  time.sleep(delay)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print(f"You see {rooms[currentRoom]['item']}")
  print("---------------------------")
  if "teleport" in rooms[currentRoom]: 
    print("\nA teleport station has been found!")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'center' : {
                  'north' : 'north',
                  'south' : 'south',
                  'east' : 'east',
                  'west' : 'west',
                  'item' : ['water', 'knife'],
                  'desp' : 'You are in the center which is the starting point.' 
                },

            'north' : {
                  'south' : 'center',
                  'item' : ['fire', 'water', 'knife'],
                  'desp' : 'You are in the north'
                },
            'south' : {
                  'north' : 'center',
                  'east' : 'field',
                  'teleport' : 'east',
                  'item' : ['red potion', 'green potion', 'knife'],
                  'desp' : 'You are in the south.'
               },
            'west' : {
                  'east' : 'center',
                  'item' : ['knife', 'sword', ],
                  'teleport' : 'basement',
                  'desp' : 'You are in the west.'
                }, 
            'east' : {
                  'west' : 'center',
                  'east' : 'field',
                  'teleport' : 'basement',
                  'target' : 'warrior',
                  'desp' : 'You are in the east. A warrior appears in front of you.\nHe\'s trying to stop you from passing.'
                },
            'field' : {
                  'west' : 'east',
                  'target' : 'zoobie'
                  'You are on the field now. A zoobie is running to you and trying to bite you!'
            }

            
         }

#start the player in the center
currentRoom = 'center'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('Please type your command\n>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)
  os.system('clear') # clear the screen
  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1].lower() == ('item' or 'target' or 'teleport'):
        print('Invid command. Try to use another command.')
    elif move[1].lower() in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
      if 'desc' in rooms[currentRoom]:
        print(rooms[currentRoom]['desc'])

      if currentRoom == 'basement':
        if 'knife' in inventory:
          print("You are in the basement but the door is locked.\nBut it looks like you are able to unlock the door.")
        else:
          print('15 days later, a dead body was found in a basement...GAME OVER!')
          break
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')
  

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if move[1] in inventory:
      print(f"You already have a {move[1]}!")
    elif 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      rooms[currentRoom]['item'].remove(move[1])
      #del rooms[currentRoom]['item'][move[1]]

      
      if 'fire' in inventory and 'water' in inventory:
        print('The fire has disappeared.')
        inventory.remove('fire')

    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  #if they type 'use' 
  if move[0] == 'use' :
    if move[1] == 'teleport' and (rooms[currentRoom] == 'west' or 'east'):
      currentRoom = 'basement'
    elif move[1] in inventory:
      if 'knife' in inventory:
        if move[1] == 'knife' and rooms[currentRoom] == 'basement':
          currentRoom == 'center'
          print("You have successfully escaped from the basement!\nType \status to check your location.")
            
      elif 'target' not in rooms[currentRoom]:
        print(f'You cannot use {move[1]} when there is no target.')
      else: 
        print(f'You choose to use {move[1]}.')
        if inventory[move[1]] != 'knife' or 'sword':
          del inventory[move[1]]
          if move[1] == 'green potion':
            print('Your are tallow-faced, pressing your neck with both hands, and fell so suffocated.\nYou are dead...GAME OVER!')
            break
          elif move[1] == 'red potion':
            print('You suddenly feel energized...\nCongratulation! You have gained the power of mind control!')
    else:
      print(f"{move[1]} is not in your inventory!")
  


  ## Define how a player can win or lose
  if 'zoobie' in rooms[currentRoom] and ('fire' or 'sword' not in inventory):
    print('You are eaten by zoobie! GAME OVER!')
    break

  if rooms[currentRoom] == 'field' and ('zoobie' not in rooms[currentRoom]):
    print('Congrats! You have succesfully escaped. YOU WIN!')
    break

  ## If a player enters a room with a warrior
  if 'target' in rooms[currentRoom] and 'warrior' in rooms[currentRoom]['target']:
    action1= input('The warrior apprears. Are you taking actions? (yes or no)\n>').lower()
    if action1 == 'yes':
      action2== input('what are you going to do? (use an item)').lower()
      if move[0] == 'use' and move[1] == 'sword':
        win_chance= random.randiant(1,2)
        if win_chance == 1:
          print('You are killed by the warrior! GAME OVER!')
        else:
          currentRoom= 'field'
          print('You have moved forward to the field!')
    elif action2 == 'no': 
      rooms[currentRoom]= 'center'
      print('The warrior kicked you back to the center room!')
    else:
      print('This is not a valid option!')
    # If a player enters a room with a zoobie
  elif 'target' in rooms[currentRoom] and 'zoobie' in rooms[currentRoom]['target']:
    action3= input('D')
    print('The zoobie has bited you... GAME OVER!')
    break





  elif move[0] == 'help':
    showInstructions()
    

  elif move[0] in ['q', 'quit]']:

    print("Are you sure you want to quit? Yes/No")
    quit_query = input('>')
    if quit_query.lower() in ['y', 'yes']:
      print("Thanks for playing!")
      sys.exit()
    else:
        pass