from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", items = {
                         "medallion":  Item("medallion", "heavy gold coin"),
                         "spear":  Item("spear", "very powerful long weapon")
                     }),

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
    room_items = player.current_room.items
    player_items = player.items
    print(f"{player.name} is in the", player.current_room.name)
    print("\n", player.current_room.description)
    print("\n" + player.name + "'s inventory")
    if len(player_items) > 0:
        for i in player_items:
            print(player_items[i])
    print("\nItem's in " + player.current_room.name)
    if len(room_items) > 0:
        for i in room_items:
            print(room_items[i])
    print("\n What would you like to do?")

    command = input("[n] North, [e] East, [s] South, [w] West, [get/take (item)] Pick up Item, [drop (item)] Drop Item, [q] Quit Game\n").split(" ")

    if len(command) > 1:
        if command[0] == "get":
            player_items[command[1]] = room_items[command[1]]
            room_items.pop(command[1])
        elif command[0] == "take":
            player_items[command[1]] = room_items[command[1]]
            room_items.pop(command[1])
        elif command[0] ==  "drop":
            room_items[command[1]] = player_items[command[1]]
            player_items.pop(command[1])
        else:
            print("Please take or drop an item.")

    else:
        if command == "q":
            print("You've done all you can do here. Go rest and resume your adventure at a later time.")
            break

        if command == "n":
            print("You proceed north.")
            if player.current_room.n_to is None:
                print("The way is shut, it is kept by those who are dead. The way is shut.")
            else:
                player.current_room = player.current_room.n_to

        elif command == "e":
            print("You travel east.")
            if player.current_room.e_to is None:
                print("The way is shut, it is kept by those who are dead. The way is shut.")
            else:
                player.current_room = player.current_room.e_to

        elif command == "s":
            print("You move south.")
            if player.current_room.s_to is None:
                print("The way is shut, it is kept by those who are dead. The way is shut.")
            else:
                player.current_room = player.current_room.s_to

        elif command == "w":
            print("You journey west.")
            if player.current_room.w_to is None:
                print("The way is shut, it is kept by those who are dead. The way is shut.")
            else:
                player.current_room = player.current_room.w_to

        else:
            print("You cannot travel on that plane of existence!")