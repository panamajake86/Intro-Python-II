from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player("Eamon", room["outside"])

while True:
    print(f"{player.name} is in the", player.current_room.name)
    print("\n", player.current_room.description)
    #if len(items) > 0:
     #   for i in items:
      #      print(i)
    print(items)
    print("\n Where would you like to go?")

    command = input("[1] North\t [2] East\t [3] South\t [4] West\t1 [9] Quit Game \n")

    if command == "9":
        print("You've done all you can do here. Go rest and resume your adventure at a later time.")
        break

    if command == "1":
        print("You proceed north.")
        if player.current_room.n_to is None:
            print("The way is shut, it is kept by those who are dead. The way is shut.")
        else:
            player.current_room = player.current_room.n_to

    elif command == "2":
        print("You travel east.")
        if player.current_room.e_to is None:
            print("The way is shut, it is kept by those who are dead. The way is shut.")
        else:
            player.current_room = player.current_room.e_to

    elif command == "3":
        print("You move south.")
        if player.current_room.s_to is None:
            print("The way is shut, it is kept by those who are dead. The way is shut.")
        else:
            player.current_room = player.current_room.s_to

    elif command == "4":
        print("You journey west.")
        if player.current_room.w_to is None:
            print("The way is shut, it is kept by those who are dead. The way is shut.")
        else:
            player.current_room = player.current_room.w_to

    else:
        print("You cannot travel on that plane of existence!")