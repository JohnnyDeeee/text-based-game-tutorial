import time

# The different tiles that make up our world
# Each tile is represented by a string
# This we can say that
# 'x' is grass
# 'y' is a path
# 'iX' is a item with index X
world = [
    ('x', 'x', 'x', 'y', 'x', 'x', 'x'),
    ('x', 'x', 'x', 'y', 'x', 'x', 'x'),
    ('x', 'y', 'i1', 'y', 'y', 'i0', 'y'),
    ('x', 'x', 'x', 'y', 'x', 'y', 'y'),
    ('x', 'x', 'x', 'x', 'x', 'x', 'x'),
]

# These are all the items you can use in your world
# Each item has a
# name: The name of the item, ex "Sword"
# amount: How much of these items will be added to your inventory, ex 1
# message: The message that is shown when you pickup the item, ex "You found a brand new sword!"
items = [
    ("Sword", 1, "You found a brand new sword!"),
    ("Coins", 30, "You found a stack of coins!")
]

# This array holds all your items you have picked up
# When an item is added, it will just add the "name"
# of the item to this array
# So when you pick up 30 coins, it will add 30x the string "Coins"
# to this array
inventory = []

# These are your starting coordinates
# Each x/y coordinate represents the index of a tile
# inside your "world" variable
start_pos_x = 0
start_pos_y = 3

# These variables keep track of your current position
# Because we start at start_pos_x,start_pos_y
# we can already set our current_pos to those coordinates
current_pos_x = start_pos_x
current_pos_y = start_pos_y


# This function will move you 1 tile
# in the specified direction
# The directions you can use are
# "up"
# "down"
# "left"
# "right"
# You call it like this:
# move("right")
# This will move you 1 tile to the right in the world
def move(_direction):
    global current_pos_x, current_pos_y

    if _direction == "up":
        if (current_pos_x - 1) < 0:
            print("Oops! You can't go that way")
        else:
            current_pos_x -= 1
    elif _direction == "down":
        # We use len() - 1, because len(world) does not start at 0
        if (current_pos_x + 1) > (len(world) - 1):
            print("Oops! You can't go that way")
        else:
            current_pos_x += 1
    elif _direction == "left":
        if (current_pos_y - 1) < 0:
            print("Oops! You can't go that way")
        else:
            current_pos_y -= 1
    elif _direction == "right":
        # We use len() - 1, because len(world) does not start at 0
        if (current_pos_y + 1) > (len(world[current_pos_x]) - 1):
            print("Oops! You can't go that way")
        else:
            current_pos_y += 1


# This function will do specific actions
# for specific tiles
# If you step on a "iX" tile (X can be a number)
# it will add the item from the item array to
# your inventory and print out the "message"
# defined with the item
def checkTile():
    tile = world[current_pos_x][current_pos_y]
    if tile.startswith('i'):
        item = items[int(tile.strip('i'))]
        print(item[2])
        addToInventory(item[0], item[1])


# This function will add an item to your
# inventory X amount of times
# You call it like this:
# addToInventory("Coins", 12)
# This will add 12 "Coints" to your inventory
def addToInventory(item_name, item_amount):
    for i in range(0, item_amount):
        inventory.append(item_name)
    print("{}x {} have been added to your inventory!".format(item_amount, item_name))
    time.sleep(1)  # We sleep here for a second, so it is easier to notice the print from above ^


# This just prints a welcome screen
# Tip: Use an empty print() to print
# a blank line
print("====================================")
print("Welcome to my first text based game!")
print("I hope you like it, enjoy")
print("====================================")
print()

# This is called the main game loop
# It will run forever (until you stop the program)
# In here we tell the user what actions he can do
# And every action we check the tile he's on
# If he is on a special tile, we execute a special
# action through checkTile()
while True:
    print("Your current position is [x:{}, y:{}] and your tile character is [{}]".format(current_pos_x, current_pos_y,
                                                                                         world[current_pos_x][
                                                                                             current_pos_y]))  # Debug
    print("You can move 'up', 'down', 'left', 'right'")
    direction = input("Which way do you want to go? ")
    print()
    move(direction)
    checkTile()
    print()
