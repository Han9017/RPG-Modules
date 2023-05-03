#-----------------------------------------------------------------------------
#    File name: RPG-Module
#    Author: Han Wang
#    Date created: 3/26/2023
#    Date last modified: 3/30/2023
#    version 3
#-----------------------------------------------------------------------------
'''   Description: Adventure Games'''
#-----------------------------------------------------------------------------
import map

#Create a variable "row" with a value of 0
row = 0  
col = 0

#Create a list called inventory
inventory = []

playing = True

# tile information
#Create a list called tile
#The first assignment is "start", which means that tile[0] is "start", 
#and so on
#Description about objects "Holy Sword", "Holy Sword", and "Holy Armor".
objects = {
          "Holy Sword" : {"Description" : "You found a shining sword inserted"
                          +" in a stone. That should be the Holy Sword.",
                     "Status" : "in stone",
                     "Location": [2, 1], 
                     "Action" : ["take", "leave"],
                     "Requirement" : ["key", None, None]
                    },
         "Holy Sword" : {"Description" : "You found a box, opened it, and" 
         +" found a very beautiful helmet.",
                   "Status" : "in box",
                   "Location" : [0, 1],
                   "Action" : ["take", "leave"],
                   "Requirement" : [None, None]
                  },
          "Holy Armor" : {"Description" : "You notice that there seems to be"
          +" light in front of you, and after walking over, you find armor on"
          +" the scorched ground.",
                   "Status" : "on ground",
                   "Location" : [3, 3],
                   "Action" : ["take", "leave"],
                   "Requirement" : [None, None]
                  }
          }
          
#Description about npc "Little Demon Legion", "Eric", and "Injured Old Man".
npcs = {
          "Little Demon Legion" : {"Description" : "Disgusting things, but it"
          +" seems that I need some more lethal weapons to defeat them.",
                     "Status" : "screaming",
                     "Location": [4, 1], 
                     "Action" : ["fight", "leave"],
                     "Requirement" : [None, None]
                    },
          "Eric" : {"Description" : "He has an evil energy, and that energy"
          +" continues to grow.",
                   "Status" : "in sky",
                   "Location" : [4, 4],
                   "Action" : ["fight", "leave"],
                   "Requirement" : [None, None]
                  }, 
          "Injured Old Man" : {"Description" : "I can't believe there are" 
          +" still living humans here.",
                   "Status" : "in room",
                   "Location" : [2, 0],
                   "Action" : ["talk", "leave"],
                   "Requirement" : [None, None]
                  }
          }


# Functions ------------------------------------------------------------------
def walkto():
  global playing, row, col, max_row, max_col
  orientating = playing
  while orientating:
   print("Choose a direction: ")
   canUp = False
   canDown = False
   canRight = False
   canLeft = False

#Player Movement Instructions
   if row > 0:
     canUp = True
     print("you can go up - type:'up'")

   if row < max_row:
     canDown = True
     print("you can go down - type:'down'")

   if col < max_col:
     canRight = True
     print("you can go right - type:'right'")

   if col > 0:
     canLeft = True
     print("you can go left - type:'left'")
   orientating = False

#Create a variable called "waychoice" and assign it to user input 
#(input(f"Choice: ")), then change the user input to lowercase (.lower())
   waychoice = input("Choice: ").lower()
   if waychoice == "up" and canUp:
        row = row - 1 
     
   elif waychoice == "down" and canDown:
        row = row + 1

   elif waychoice == "right" and canRight:
        col = col + 1
     
   elif waychoice == "left" and canLeft:
        col = col - 1
   elif waychoice == "quit":
        playing = False

   else:
        print("There's no road there, only the sea.")
        waychoice = True 


def Inspectplace1():
    global row, col, inventory, objects
    found_object = False
    location_description =  map.map[row][col]
    for object in objects:
        object_row = objects[object]["Location"][0]
        object_col = objects[object]["Location"][1]
        if object_row == row and object_col == col:
             print(f"{objects[object]['Description']}")

      
def Inspectnpc1():    
    global row, col, inventory, npcs
    found_npc = False
    location_description =  map.map[row][col]
    for npc in npcs:
        npc_row = npcs[npc]["Location"][0]
        npc_col = npcs[npc]["Location"][1]
        if npc_row == row and npc_col == col:
            print(f"{npcs[npc]['Description']}")


def MainMenu():
  global playing, objects
  orientating = playing
  while orientating:
    print("Choose to move to another area or look around:")
    Choose = ["walk", "look"]
    for do in Choose:
      print((f"- {do.title()}"))
    userInput = input("You choice: ").lower()
    orientating = False
    if userInput == Choose[0]:
      print("You went to the area ahead")
      walkto()
    
    elif userInput == Choose[1]:
      print("You look around.")
      #Function call----------------------------------------------------------
      Inspectplace1()
      Inspectnpc1()
      #if the user chooses to quit, the game quit
    elif userInput == "quit":
      playing = False
    else:
      print("Invalid input!")
      orientating = True

      
# Main -----------------------------------------------------------------------
print("""Mission Overview (Background Story): You are a super soldier, 
teleported to the island occupied by Eric (Demon, Super Rebel). Eric was
originally a normal person, but he seemed to have made a deal with the devil
and gained very powerful power, and used this power to occupy Paradise Island
in the Pacific Ocean. According to satellite intelligence, he seemed to be 
building an altar. 

Theological experts believe that he does not currently have all the demon 
power, and he needs an altar to transmit all the demon power from hell to 
the real world. Therefore, the major powers of the world united and sent out
troops in order to defeat them. Due to their belittling of the enemy, they 
initially used only conventional military forces, such as infantry, 
helicopters, and landing craft, to capture the island, but no one survived. 

At this time, people began to realize that even though Eric did not gain all
the demon power, it was still more than enough to deal with ordinary mortals.
Therefore, various countries began to use various advanced weapons, such as 
advanced fighter jets, a large number of cruise missiles, high-speed drones,
hypersonic missiles, and even eventually intercontinental missiles with 
nuclear warheads. However, no matter how advanced and fast those weapons 
were, How intelligent and powerful they are, they are all blocked outside 
the island gate by Eric's magical shield created using demon power and the 
hell demon monsters he summons. At this time, the world felt panic, people 
became overwhelmed, and the world fell into chaos and despair. And you, 
perhaps the only person who can save this world, are the last follower of 
the guardian angel of heaven who stays on Earth to protect humanity. 

Looking at the expanding red fog outside the Paradise Island captured by 
satellites in the news, you are also very anxious, because you know that
only magic can defeat magic, and those aircraft and missiles will not have
any effect. You have read the books left by your ancestors and learned some
knowledge about Paradise Island and the power of demons. Paradise Island was
originally a place where angels were buried after the physical death of 
humans. Over time, a large amount of magical energy accumulated here, so Eric
chose to build an altar here because opening the energy transfer door required
a large amount of magical energy. And through learning, you understand that
Eric obtained the authentic 'power of the agent of Satan', which cannot be 
harmed by ordinary magic weapons. He must gather together the 'Holy Sword', 
'Holy Helmet', and 'Holy Armor' made in heaven to defeat him, and it happens 
that they are scattered all over the Island of Paradise.""")
print("Good luck!")

place = ["Start", "A swampy land", "A charred jungle", "Bloody Lake", 
        "Demon Flower Field", "sacrificial altar", "broken church", 
        "land of cracks"]
max_length = len(max(place, key=len)) + 1
#show player map-------------------------------------------------------------

print("+---------------------------------------------------------------------"
+"--------------+")

for mapRow in map.map:
  for mapCol in mapRow:
    print("| {:{}}".format(mapCol, max_length), end="")
  print("|\n+----------------------------------------------------------------"
  +"-------------------+")

while playing:
  location_description = map.map[row][col]
  for tile in map.tiles:
    if tile == location_description:
      print(map.tiles[tile]["Description"])
  
  MainMenu()
