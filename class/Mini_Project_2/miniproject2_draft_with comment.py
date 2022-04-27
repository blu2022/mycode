#!/usr/bin/python3
import sys
import os
import random
import time
from pyfiglet import figlet_format
import threading

# search from here http://www.figlet.org/examples.html 
def bannershow():
    print("\n")
    print(figlet_format("Adventure", font = "ogre"))

bannershow()

def print_slow(text, delay = 0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def print1(text1, delay = 0):
    print("\n" + text1)
    time.sleep(delay)

def restart():
    sys.stdout.flush()
    os.execl(sys.executable, 'python', __file__, *sys.argv[1:])


def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    t= 10
    countdown(int(t))  
    print('You are eaten by zombie! GAME OVER!')
  

delay = 0

def showInstructions():
  print1('''
RPG Adventure Game
==================
Instruction: You are in the center from the beginning.
You can move north/south/west/east to find a way to escape.
hint: Water kills fire.
      fire kills zombie.
      sword kills zobbie and warrior.
      A good potion will never be green.
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
  print_slow('You are in the ' + currentRoom)
  print_slow('Inventory : ' + str(inventory))
  if "item" in rooms[currentRoom]:
    print_slow(f"You see {rooms[currentRoom]['item']}")
  print("---------------------------")
  if "teleport" in rooms[currentRoom]: 
    print_slow("\nA teleport station has been found!")
    
inventory = []

rooms = {
            'center' : {
                  'north' : 'north',
                  'south' : 'south',
                  'east' : 'east',
                  'west' : 'west',
                  'item' : ['water', 'knife'],
                  'desc' : 'You are in the center room which is the starting point.\nThere are four doors on each side: North, South, West, East.' 
                },
            'north' : {
                  'south' : 'center',
                  'item' : ['fire', 'water', 'knife'],
                  'desc' : 'You are in a cold environment. It\'s probably not gonna be a good idea to stay too long.'
                },
            'south' : {
                  'north' : 'center',
                  'east' : 'field',
                  'teleport' : 'east',
                  'item' : ['red potion', 'green potion', 'knife'],
                  'desc' : 'You see two potions on a table. One is red, and another one is green.\nThe red one smells like lavender while the green one smells a little stink.'
               },
            'west' : {
                  'east' : 'center',
                  'item' : ['knife', 'sword', ],
                  'teleport' : 'basement',
                  'desc' : 'There is a knife right next to the teleport station.\nIt looks like someone dropped it before.\nOn the other side, you find a sword, which looks a little blunt but still sharp enough to cut meat'
                }, 
            'east' : {
                  'west' : 'center',
                  'east' : 'field',
                  'teleport' : 'basement',
                  'target' : 'warrior',
                  'desc' : 'A warrior appears in front of you.\nHe\'s trying to stop you from passing.'
                },
            'field' : {
                  'west' : 'east',
                  'target' : 'zombie',
                  'desc': 'You are on the field now. A zombie is running to you and trying to bite you!'
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
    # CHAD CHANGE: redundant to use move[1].lower(), already did that on line 90
      
        if move[1] == 'item' or move[1] == 'desp' or move[1] == 'target' or move [1] == 'teleport': 
          print('invalid command! Please type again!')
        elif move[1] in rooms[currentRoom]:
          currentRoom = rooms[currentRoom][move[1]]
          if 'desc' in rooms[currentRoom]: 
                print1(rooms[currentRoom]['desc'], 1)
        else:
          print('You can\'t go that way!')        

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
      inventory -= [move[1]]
      print(move[1] + 'dropped!')
      rooms[currentRoom]['item'].append(move[1])
    else:
      print('You do not have this item!')  

  if move[0] == 'use' :
  # CHAD NOTE: a lot of this code was redundant (already covered elsewhere in the script) so I removed it.
  
        if move[1] == 'teleport':
            currentRoom = 'basement'

        elif move[1] == 'green potion':
            print('Your are tallow-faced, pressing your neck with both hands, and fell so suffocated.\nYou are dead...GAME OVER!')
            break
            
        elif move[1] == 'red potion':
            print('You suddenly feel energized...\nCongratulation! You have gained the power of mind control!')
                
        else:
            print(f"{move[1]} is not in your inventory!")
     
  if currentRoom == 'basement':
        if 'knife' in inventory:
          print("You are in the basement but the door is locked.\nBut it looks like you are able to unlock the door.")
          currentRoom == 'center'
        else:
          print('15 days later, a dead body was found in a basement...GAME OVER!')
          break
        
  if 'fire' in inventory and 'water' in inventory:
        print('The fire has disappeared.')
        inventory.remove('fire')
    
  if 'target' in rooms[currentRoom] and 'warrior' in rooms[currentRoom]['target']:
          if 'red potion' not in inventory or 'sword' not in inventory:
            currentRoom= 'center'
            print('The warrior kicked you back to the center room!')
          if move[0] == 'go':
            if move[1] == 'east':
                print('Warrior block the only road to the east.\nYou must either get permission from him or defeat him.')
          if move[0]== 'use':
            if 'sword' in inventory and move[1] == 'sword':
               win_chance= random.randint(1,2)
               if win_chance == 1:
                   print('You are killed by the warrior! GAME OVER!')
                   break
               else:
                 currentRoom= 'field'
                 print('You have defeated the warrior and escaped to the field!')

  if 'target' in rooms[currentRoom] and 'zombie' in rooms[currentRoom]['target']:
      if 'fire' in inventory and move.lower() == 'use fire':
          print("There is a zombie here! You toss fire in its face and watch the ghoul burn!")
          del rooms[currentRoom]['target']
      elif "sword" in inventory and move.lower() == 'use sword':
          print("There is a zombie here! You lop off its head with your sword!")
          del rooms[currentRoom]['target']
      elif "red potion" in inventory and move.lower() == 'use red potion':
          print("You have gain the power of mind control! However, the zoobie does not have mind.")
          
      elif 'fire' not in inventory and 'sword' not in inventory and 'red potion' not in inventory:
          print('You are eaten by zombie! GAME OVER!')
          break
    
  if currentRoom == 'field' and 'target' not in rooms[currentRoom]:
    print('Congrats! You have successfully escaped. YOU WIN!')
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