#!/usr/bin/python3
import sys
import os
import random
import time
from pyfiglet import figlet_format
import threading



def print_slow(text, delay = 0.02):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def print1(text1, delay = 0):
    print("\n" + text1)
    time.sleep(delay)

# search from here http://www.figlet.org/examples.html 
def bannershow():
    print("\n")
    print1(figlet_format("Adventure", font = "ogre"), 0.05)

def restart():
    sys.stdout.flush()
    os.execl(sys.executable, 'python3', __file__, *sys.argv[1:])

def decision():
    print("You took too long! The zombie ate your brains!")
    os._exit(os.EX_OK)
    # os._exit will FORCE the program to end!

    S = threading.Timer(10.0, decision)
    # What does the above line mean?
    # threading.Timer is a class object- how it works depends on the two arguments provided:
    # arg 1 (10.0) is the number of seconds until a function is called0
    # arg 2 (decision) is the function that will be called in 10.0 seconds

    S.start()
    # this line STARTS the separate thread!
    # the thread "S" will run simultaneously as more actions
    # below are executed
    #print("PROGRAM TERMINATION\n")  
    #S.cancel()

    print("You're trapped in a room with a zombie!!! You have 3 seconds to figure out what to do before the zombie eats your brains!")


bannershow()

delay = 0

def showInstructions():
  print1('''
RPG Adventure Game
==================
Instruction: You are in the center from the beginning.
You can move north/south/west/east to find a way to escape.
hint: Water kills fire.
      Fire kills zombie.
      Sword kills zombie and warrior.
      Usually, a poisonal potion is green.
      Small size knife cannot kill human or zombie.
Commands:
  go [direction]  ---- go to a direction
  get [item]      ---- obtain an item
  drop [item]     ---- drop an item
  use [item]      ---- use an item
  h or help       ---- review the instruction (inventory check)
  r or restart    ---- restart the game
  q or quit       ---- quit the game
''')

def showStatus():
  print('---------------------------')
  print1('You are in the ' + currentRoom)
  print1('Inventory : ' + str(inventory))
  if "item" in rooms[currentRoom]:
    print1(f"You see {rooms[currentRoom]['item']}")
  print("---------------------------")
  if "teleport" in rooms[currentRoom]: 
    print1("\nA teleport station has been found!")
    
inventory = []

rooms = {
            'center' : {
                  'north' : 'north',
                  'south' : 'south',
                  'east' : 'east',
                  'west' : 'west',
                  'item' : ['water', 'knife', 'sword', 'red potion', 'fire'],
                  'desc' : 'You are in the center room which is the starting point.\nThere are four doors on each side: North, South, West, East.' 
                },
            'north' : {
                  'south' : 'center',
                  'item' : ['fire', 'water', 'knife'],
                  'desc' : 'You are in a cold environment. It\'s probably not gonna be a good idea to stay too long.\nThe knife is small like the size of an index finger'
                },
            'south' : {
                  'north' : 'center',
                  'item' : ['red potion', 'green potion', 'knife'],
                  'desc' : 'You see two potions on a table. One is red, and another one is green.\nThe red one smells like lavender while the green one smells a little stink.\nThe knife is small like the size of an index finger'
               },
            'west' : {
                  'east' : 'center',
                  'item' : ['knife', 'sword', ],
                  'teleport' : 'basement',
                  'desc' : 'There is a knife right next to the teleport station.\nIt looks like someone dropped it before.\nOn the other side, you find a sword, which looks a little blunt but still sharp enough to cut meat.\nThe knife right next to the sword is small like the size of an index finger.'
                }, 
            'east' : {
                  'west' : 'center',
                  'east' : 'field',
                  'teleport' : 'basement',
                  'target' : 'warrior',
                  'item':'',
                  'desc' : 'A warrior appears in front of you.\nhe blocks the only road to the east.\nYou must either convince him or defeat him to pass.'
                },
            'field' : {
                  'west' : 'east',
                  'target' : 'zombie',
                  'item':[],
                  'desc': 'You are on the field now. A zombie is running to you and trying to bite you!'
                },
            'basement' : {  
                  'item': [],           
                  'target': [],
                  'desc': 'You are now locked in a basement. You need to find a way out!'
                }
          }
         
currentRoom = 'center'

showInstructions()

while True:
  showStatus()
  
  move = ''

  while move == '':
    move = input('Please type your command\n>')
    move = move.lower().split(" ", 1)

  os.system('clear') 
  if move[0] == 'go':
    # CHAD CHANGE: moved code for specific rooms to later in the code, keep code cleanly modularized
        if move[1] == 'item' or move[1] == 'desp' or move[1] == 'target' or move [1] == 'teleport': 
          print('invalid command! Please type again!') 
        #elif currentRoom == 'east' and move[1] == 'east': 
        elif 'target' in rooms[currentRoom] and 'warrior' in rooms[currentRoom]['target']:
            if currentRoom == 'east' and move[1] == 'east':
              print_slow('The warrior does not allow you to pass!')
            else:
              pass
        elif 'target' in rooms[currentRoom] and 'zombie' in rooms[currentRoom]['target']:
            if currentRoom == 'field':
              print_slow('find a way to kill the zombie!')
        #elif currentRoom == 'field' and 'target' in rooms[currentRoom] and 'zombie' not in rooms[currentRoom]['target']: 
                #print_slow('Congrats! You have successfully escaped. YOU WIN!')
                #break
        elif move[1] in rooms[currentRoom]:
          currentRoom = rooms[currentRoom][move[1]]
        else:
          print('You can\'t go that way!') 
                
  if 'desc' in rooms[currentRoom]: 
      print1(rooms[currentRoom]['desc'], 1)
  # add items to inventory
  if move[0] == 'get' :
    if move[1] in inventory:
      print(f"You already have a {move[1]}!")
    elif move[1] not in inventory and len(inventory) >= 3:
      print('You can not pick up more than 3 items!') 
    elif 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      inventory += [move[1]]
      print(move[1] + ' got!')
      rooms[currentRoom]['item'].remove(move[1])
    else:
      print('Can\'t get ' + move[1] + '!')

  # drop items
  if move[0] == 'drop':
    if move[1] in inventory:
      inventory.remove(move[1])
      print(move[1] + ' dropped!')
      rooms[currentRoom]['item'].append(move[1])
    else:
      print('You do not have this item!')  
 
  # use items

    # The item is not in inventory
  if move[0] == 'use' and move[1] not in inventory: 
      if move[1] == 'teleport' and currentRoom in ['west', 'east']:
          currentRoom = 'basement'
          print_slow('You have been teleported to a basement!\n') 
          if 'desc' in rooms[currentRoom]: 
            print1(rooms[currentRoom]['desc'], 1)  
      else:      
        print(f"{move[1]} is not in your inventory!")

  if move[0] == 'use' and move[1] in inventory:
      print(f'You choose to use {move[1]}.')
      #if currentRoom == "basement" and move[1] == "knife":
          #print("You escape the basement.")
          #currentRoom= "center"
           
    #except for being in basement, you should not be able to use items while there is no target.             
      if 'target' not in rooms[currentRoom]: #and "potion" not in move[1]:
          print(f'You cannot use {move[1]} when there is no target.')
      #if move[1] not in ['knife', 'sword']:
        #inventory.remove(move[1])
      if move[1] == 'green potion':
          inventory.remove(move[1])
          print('Your are tallow-faced, pressing your neck with both hands, and fell so suffocated.\nYou are dead...GAME OVER!')
          break

      
  if currentRoom == 'basement':
      if 'knife' not in inventory and "knife" not in rooms[currentRoom]["item"]:
          print('15 days later, a dead body was found in a basement...GAME OVER!')
          break
      if move[0] == 'use' and move[1] == 'knife':
          print("You have broken the lock with the knife! You are back to the center.")
          currentRoom = 'center'
      else:
          print('You are locked in the basement! Find a way out!')
          pass
  if 'fire' in inventory and 'water' in inventory:
        print('The fire has disappeared.')
        inventory.remove('fire')
  #with warrior in the east
  if currentRoom == 'east' and 'target' in rooms[currentRoom] and 'warrior' in rooms[currentRoom]['target']:
        #print('Warrior block the only road to the east.\nYou must either get permission from him or defeat him.')
        #if move[0] == 'go':
           #if move[1] == 'east':
              #currentRoom= 'east'
              #print('The warrior won\'t allow you to pass!')           
        if move[0] == 'use':
          if 'red potion' in inventory and move[1] == 'red potion':
              print('You suddenly feel extremly energized...\nCongratulation! You have gained the power of mind control!\nThe warrior is told to walked away.')
              time.sleep(5)
              inventory.remove(move[1])
              del rooms[currentRoom]['target']

          if 'sword' in inventory and move[1] == 'sword':
               win_chance= random.randint(1,3)
               if win_chance == 1:
                   print('You are killed by the warrior! GAME OVER!')
                   break
               else:
                 del rooms[currentRoom]['target']
                 print('You have defeated the warrior. You found an exit to the field on the east side!')

          
  #if currentRoom == 'east' and 'warrior' not in rooms[currentRoom]['target']:

  #with zombie in the field
  #how to win
  #if 'target' in rooms[currentRoom] and 'zombie' not in rooms[currentRoom]['target']:
      #if currentRoom == 'field':
        #print('Congrats! You have successfully escaped. YOU WIN!')
        #break

  elif 'target' in rooms[currentRoom] and 'zombie' in rooms[currentRoom]['target']:
    #while move == '':
      #S = threading.Timer(10.0, decision)
      #S.start()
      if move[0] == 'use':
        if 'fire' in inventory and move[1] == 'fire':
          print("There is a zombie here! You toss fire in its face and watch the ghoul burn!\nYOU WIN!")
          break
        if "sword" in inventory and move[1] == 'sword':
          print("There is a zombie here! You lop off its head with your sword!YOU WING!")
          break
        if "red potion" in inventory and move[1] == 'red potion':
          print("You have gain the power of mind control! However, the zoobie does not have mind.\nYou are eaten by zombie! GAME OVER!")
          break
        if 'fire' not in inventory and 'sword' not in inventory and 'red potion' not in inventory:
          print('You are eaten by zombie! GAME OVER!')
          break

  
  elif move[0] in ['h', 'help', 'inv', 'inventory']:
      showInstructions()
  elif move[0] in ['r', 'restart']:
      restart_query = input("Are you sure you want to restart the script? (Y/N)")
      if restart_query.upper() in ['Y', 'YES']:
        restart()
      else: 
          pass
  elif move[0] in ['q', 'quit']:
      print("Are you sure you want to quit? Y/N")
      quit_query = input('>')
      if quit_query.upper() in ['Y', 'YES']:
          print("Thanks for playing!")
          sys.exit()
      else:
          pass