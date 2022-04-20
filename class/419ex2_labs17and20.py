#!/usr/bin/env python3

pokedex={"Bulbasaur":"Grass/Poison",
         "Squirtle":"Water",
         "Charmander":"Fire"}

print("----add new key pair to dic")
pokedex["Pikachu"] = "Electric"

choice= input("Name a Generation 1 starter Pokemon:\n>")
print(pokedex.get((choice), "Sorry, we don't have any record of that Pokemon!"))

print( pokedex.keys() )
print( pokedex.values() )

Newlist1= (pokedex.keys())
Newlist2= ", ".join(Newlist1)

print("Choices:", Newlist2)
