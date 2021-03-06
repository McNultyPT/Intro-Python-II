from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

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

# list of items

item = {
    'sword': Item('sword', 'weathered and rusty'),
    'torch': Item('torch', 'recently extinguished'),
    'scroll': Item('scroll', 'to have a faded map on it'),
    'coin': Item('coin', 'patinaed'),
    'shovel': Item('shovel', 'covered in fresh dirt')
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

# Adds items to rooms

room['outside'].items = [item['sword']]
room['foyer'].items = [item['torch']]
room['overlook'].items = [item['scroll'], item['coin']]
room['narrow'].items = [item['coin']]
room['treasure'].items = [item['shovel'], item['coin']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Guybrush Threepwood', room['outside'].name)

# Print current room and items
def current():
    for i in room:
        if player.current_room == room[i].name:
            print(
                f'\nYou have entered the {room[i].name}. {room[i].description}')
            for x in room[i].items:
                print(f'\nYou notice a {x.name}, which looks {x.description}.')
            return room[i]

# move player
def move(current_room, make_move):
    new_room = make_move + '_to'
    destination = getattr(current_room, new_room)
    player.current_room = destination.name
    return player

# start loop
def initiate():
    print(f'\nWelcome, {player.name}!')

    while True:
        start_location = current()
        cmd = input('\n<== Movement: North [n] South [s] East [e] West [w], Pickup [p] or Drop item [d], Inventory [i] or Quit [q] ==>\n').split()
        cmd_one = cmd[0]
        cmd_two = cmd[-1]

        # quit
        if cmd_one == 'q':
            print(f'\nSee you next time, {player.name}!')
            break
        # move
        elif cmd_one == 'n' or cmd_one == 's' or cmd_one == 'e' or cmd_one == 'w':
            try:
                move(start_location, cmd_one)
            except AttributeError:
                print('\nThat way is blocked. Try another direction.')
        # pickup item
        elif cmd_one == 'p':
            for x in room:
                room_items = room[x].items
                for i in room_items:
                    if i.name == cmd_two:
                        player.inventory.append(i.name)
                        room_items.remove(i)
                        print(f'\nYou pick up a {i.name}.')
                    break
                else:
                    print('\nThat item does not exist.')
        # drop item
        elif cmd_one == 'd':
            player_items = player.inventory
            for i in player_items:
                if i == cmd_two:
                    player.inventory.remove(i)
                    print(f'\nYou drop a {i}.')
                    break
                else:
                    print('\nYou do not have that item in your inventory.')
        # check inventory
        elif cmd_one == 'i':
            items = player.current_inventory()
            if len(items) != 0:
                print(f'\nCurrent inventory: {items}.')
            else:
                print('\nYour inventory is empty.')
        else:
            print('\nPlease enter a valid command.')


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
