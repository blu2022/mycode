#!/usr/bin/env python3

char_name= input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n>")

char_stat= input("What statistic do you want to know about? (real name, powers, archenemy)\n>")

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }


print(char_name)
print(char_stat)
print(marvelchars[char_name][char_stat])

print(f"{char_name}'s {char_stat.title()} is {marvelchars[char_name][char_stat].title()}")