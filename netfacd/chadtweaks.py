#!/usr/bin/env python3

import netifaces

# print(netifaces.ifaddresses("ens3"))

print(netifaces.interfaces())

def mac(adapter_name):
    #adapter_num= input("Please enter the adapter number: ")
    print(f"MAC: {netifaces.ifaddresses(adapter_name)[netifaces.AF_LINK][0]['addr']}") # Prints the MAC address
 
def ip(adapter_name):
    print(f"IP: {netifaces.ifaddresses(adapter_name)[netifaces.AF_INET][0]['addr']}") # Prints the IP address

adapter_name= input("Choose an adapter:\n>")

mac(adapter_name)

ip(adapter_name)
