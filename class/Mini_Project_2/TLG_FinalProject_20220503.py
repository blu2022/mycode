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
    #os.execv(sys.executable, ['python3'] + sys.argv)
    os.execl(sys.executable, 'python3', __file__, *sys.argv[1:])

def cutezombie():
    print('''
      
                                .....            
                               C C  /            
                              /<   /             
               ___ __________/_#__=o             
              /(- /(\_\________   \              
              \ ) \ )_      \o     \             
              /|\ /|\       |'     |             
                            |     _|             
                            /o   __\             
                           / '     |             
                          / /      |             
                         /_/\______|             
                        (   _(    <              
                         \    \    \             
                          \    \    |            
                           \____\____\           
                           ____\_\__\_\          
                         /`   /`     o\          
                         |___ |_______|.. 
      
      '''
)
  
def decision():
  
    cutezombie()
    print("\nYou took too long! The zombie ate your brains!")
    os._exit(os.X_OK)
  
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
                  'item' : ['water', 'knife', 'gold bar', 'cigarette'],
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
                  'desc' : 'A warrior appears in front of you.\nHe blocks the only road to the east.\nYou must either convince him or defeat him to pass.'
                },
            'field' : {
                  'west' : 'east',
                  'target' : 'zombie',
                  'item':[],
                  'desc': 'You are on the field now. \nA zombie is running to you and trying to bite you!\nYou don\'t have too much time to react!'
                },
            'basement' : {  
                  'item': [],           
                  'target': [],
                  'desc': 'You cannot see anything in a dark basement.'
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

  
  if move[0] == 'go':
        if move[1] == 'item' or move[1] == 'desp' or move[1] == 'target' or move [1] == 'teleport': 
          print('invalid command! Please type again!') 
        elif 'target' in rooms[currentRoom] and 'warrior' in rooms[currentRoom]['target']:
            if currentRoom == 'east' and move[1] == 'east':
                print_slow('The warrior does not allow you to pass!')
            elif currentRoom == 'east' and move[1] == 'west':
                currentRoom = rooms[currentRoom][move[1]]
            else:
              pass
        elif 'target' in rooms[currentRoom] and 'zombie' in rooms[currentRoom]['target']:
            if currentRoom == 'field':
              print_slow('find a way to kill the zombie!')
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
            
      if 'target' not in rooms[currentRoom]: #and "potion" not in move[1]:
          print(f'You cannot use {move[1]} when there is no target.')

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
        
  if currentRoom == 'east' and 'target' in rooms[currentRoom] and 'warrior' in rooms[currentRoom]['target']:
          
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

  elif 'target' in rooms[currentRoom] and 'zombie' in rooms[currentRoom]['target']:

      S = threading.Timer(8.0, decision)
      S.start()
      if move[0] == 'use':
        if 'fire' in inventory and move[1] == 'fire':
          S.cancel()
          print("There is a zombie here! You toss fire in its face and watch the ghoul burn!\nYOU WIN!")
          os._exit(os.X_OK)
          break
        if "sword" in inventory and move[1] == 'sword':
          S.cancel()
          print("You lop off its head with your sword!\nYOU WIN!")
          os._exit(os.X_OK)
          #break
        if "red potion" in inventory and move[1] == 'red potion':
          print("You have gain the power of mind control! However, the zoobie does not have mind.\nYou are eaten by zombie! GAME OVER!")
          os._exit(os.X_OK)
          #break
      if 'fire' not in inventory and 'sword' not in inventory and 'red potion' not in inventory:
          
          cutezombie()
          print('\nYou are eaten by zombie! GAME OVER!')
          os._exit(os.X_OK)
          #break

  
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