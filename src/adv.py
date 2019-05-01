from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", [Item('sword', 'weathered and rusty')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('torch', 'recently extinguished'), Item('key', 'quite old')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('scroll', 'to have a faded map on it')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('coin', 'patinaed')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('shovel', 'covered in fresh dirt'), Item('coin', 'patinaed')]),
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

player = Player('Guybrush Threepwood', room['outside'].name)

def current():
    for i in room:
        if player.current_room == room[i].name:
            print(f'You have entered the {room[i].name}. {room[i].description}\n')
            for item in room[i].items:
                print(f'You notice a {item.name}, which looks {item.description}.')
            return room[i]

def move(current_room, make_move):
    moving = make_move + '_to'
    destination = getattr(current_room, moving)
    player.current_room = destination.name
    return player

def initiate():
    print(f'Welcome, {player.name}!\n')

    while True:
        start_location = current()
        cmd = input('\n<== Choose a direction: [n] North [s] South [e] East [w] West or [q] Quit ==>\n')
        if cmd == 'q':
            print(f'\nSee you next time, {player.name}!')
            break
        elif cmd == 'n' or cmd == 's' or cmd == 'e' or cmd == 'w':
            try:
                move(start_location, cmd)
            except AttributeError:
                print('That way is blocked. Try another direction.')
        else:
            print('Invalid command')

initiate()

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


