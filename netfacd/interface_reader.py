#!/usr/bin/env python3

import netifaces

# print(netifaces.ifaddresses("ens3"))

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

def fnetifaces(ip, mac):
    adapter_num= input("Please enter the adapter number: ")
    print(f"MAC: {(netifaces.ifaddresses(str(adapter_num))[netifaces.AF_LINK])[0]['addr']}") # Prints the MAC address
  
    print(f"IP: {(netifaces.ifaddresses(str(adapter_num))[netifaces.AF_INET])[0]['addr']}") # Prints the IP address

fnetifaces(ip, mac)
