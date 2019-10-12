# Introduction
In part-1 we will learn how to setup a basic test-base game
with the following features:
- World creation
- Movement through the world
- Inventory (basic)

Result product: https://asciinema.org/a/1A8tJH6oH7ycdPtnKtDdtosvc

# Installation
If you want to run the finished script you can download
the [zip file](https://github.com/JohnnyDeeee/text-based-game-tutorial/archive/master.zip)
from github
or [copy](https://raw.githubusercontent.com/JohnnyDeeee/text-based-game-tutorial/master/part-1/main.py?token=ACEWTOBPISOESEV4FR62RTC5UHZF4)
the script from above.

# Getting started
I recommend using [PyCharm](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)
and [Python 3.7.4](https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe)

# 1.1 - Creating project files
Lets start by creating a new project folder where we can
store our project files.

You can create a new folder anywhere you like and you
may call it whatever you want or if you don't have any
inspiration just call it `test-based-game-tutorial`.

Next thing we need is a script file where we can write
python in. Again it doesn't really matter what you call
it, but most people call their script "main.py" because
that script is going to be started first. (this makes
more sense when you have multiple script files, but it
is still good to practice this)

# 1.2 - Running the script
Now let's put some test code in your python script file
to see if everything is working fine.

Put the following code inside your script file:
```python
print("I am alive!")
```

Now there are a couple ways how you can "run" your
python script. I'll explain the "PyCharm" way and the 
"command-line" way.

## PyCharm way
1. Navigate to `Run -> Edit configurations`
1. Next click the `+` symbol on the top left of the pop-up
1. Choose the `Python` option
1. Give it a name like `Run script`
1. Make sure `script path` points to your python script file
1. Check if your `python interpreter` points to `python 3.7`.
If not, point it to `python.exe` somewhere on your system ([help](https://lmgtfy.com/?q=how+to+find+my+python+interpreter))
1. Click `Apply` and close the window

Now you should see a run configuration in the top right of your
IDE ([screenshot](https://imgur.com/a/Qn2mgQN))

If you click the play button next to it you should see
a command line window starting with the text `I am alive!`

_If not, you fucked up_

## Command-line way
If you have installed Python correctly, you can open
up a terminal and navigate to the folder where your
python script is.

All you have to do next is execute:
```bash
python main.py
```
_main.py is the name of your script file_

If you did everything correctly you should see the text `I am alive!`

# 1.3 - World creation and basic movement
Now let's write some stuff.
We'll start with a simple world where you can walk around in.

Open your python script and paste this code:
```python
world = [
    ('x', 'x', 'x', 'y', 'x', 'x', 'x'),
    ('x', 'x', 'x', 'y', 'x', 'x', 'x'),
    ('x', 'y', 'y', 'y', 'y', 'y', 'y'),
    ('x', 'x', 'x', 'y', 'x', 'y', 'y'),
    ('x', 'x', 'x', 'x', 'x', 'x', 'x'),
]

start_pos_x = 0
start_pos_y = 3

current_pos_x = start_pos_x
current_pos_y = start_pos_y
```

The are some variables we will need for the world and the
movement.

`world`: This is our world, it contains of several `strings`,
but we will call the `tiles` (like a tile of a path).
The variable type is a `2 Dimensinal array`, which is an array
inside another array. As you can see we have the "upper" array
which contains 5 items (every row). Each item is another array
which contains 7 strings. If you want to access a specific tile
you can do it like this
```python
world[x][y]
```
_Where x is your x-coordinate (or index for the upper array)
and y is your y-coordinate (or index for the inner array)_

`start_pos_x`: This is the x-coordinate of your starting position
in the world.

`start_pos_y`: This is the y-coordinate of your starting position
in the world.

`current_pos_x`: This will keep track of your x-coordinate position
when you move around the world.

`current_pos_y`: This will keep track of your y-coordinate position
when you move around the world.

_The `current_pos` variables are initialized with the `start_pos` values
, because that is where we are going to start in the world_

Now we want a function that helps us to "move" through the world.
Copy the following code:
```python
def move(_direction):
    global current_pos_x, current_pos_y

    if _direction == "up":
        current_pos_x -= 1
    elif _direction == "down":
        current_pos_x += 1
    elif _direction == "left":
        current_pos_y -= 1
    elif _direction == "right":
        current_pos_y += 1
```

This function will alter our `current_pos` variable depending
on which direction we tell it to go.
It can be used like this `move("left")`.
So all our "movement" is really just changing the 2 `current_pos`
variables.

Let's create a `game loop` where we can use this function.
Copy the following code:
```python
while True:
    print("Your current position is [x:{}, y:{}] and your tile character is [{}]".format(current_pos_x, current_pos_y,
                                                                                         world[current_pos_x][
                                                                                             current_pos_y]))  # Debug
    print("You can move 'up', 'down', 'left', 'right'")
    direction = input("Which way do you want to go? ")
    print()
    move(direction)
    print()
```

## While loop
We use a `while True` loop, because we want it to run forever
as we are playing our game.

_Normally an "infinite" loop is really dangerous. What can
happen is that the loop will never end and will eat all of
your CPU in doing so. We don't have to worry because we are
waiting for `input` of the user on every iteration_

## Print() and format()
Inside this loop we first print a helper that shows us our
current coordinates an on what tile we are standing.
This uses the `string.format()` function which is very handy
if you want to use variable values inside your `print()`.

Normally you would print something like this
```python
print("Variable var_a has a value of", var_a)
```
But when using more than 1 variable it could becomes a little
hectic
```python
print("Variable", var_name, "has a value of", var_value)
```

To make it easier to read we can use the `format` function
```python
print("Variable {} has a value of {}".format(var_name, var_value))
```
In your string you define spots, where you variable values go,
with `{}`. After that, inside `format()` you define which values
will be shown on that spot.

_We use empty `print()` statements to print a blank line._

## Input()
After our print statements we need to know which direction
the user want to move. We can ask the user for some input by
using the `input()` function.

This function needs a string, which it will print to the screen
so the user can read it. After that the user can type in whatever
he wants and once he presses ENTER, the text that he typed will be
stored in the `direction` variable.

example:
```python
name = input("What is your name? ")
print(name)
```
If i run the script and type in `John` after the question,
it will output the text `John` on the next line once i press
ENTER.

## Move()
After we asked the user for it's direction, we pass that direction
into the `move()` function we created before. This will change our
current coordinates depending on the direction the user chose.

Now you should be able to start your script and walk around your
world!

But once your reach the borders of your world
[x:0, y:-1] or [x:0, y:5] or [x:-1, y:0] or [x:7, y:0]
you will notice that your script crashes.

_Python is a bit weird and allows negative indexes, so `world[0][-1]`
will count back 1 step from `world[0][0]` and thus end up being
`world[0][6]`. So the bounds above are not exactly correct but
that doesn't matter for our fix_

# 1.4 - Fixing the boundary issue
To fix the crashing issue with our world, we first need to
understand why it crashes.

The error is
```
IndexError: list index out of range
```
which means that we are trying to access an item from the
`world` list (array) with an index that doesn't exist.

Our (upper) array has 5 items (the inner arrays).
5 items means an index range of 0..4 (index 0 = row 1, index 1 = row 2, etc)
So if we try to access `world[5]`, it would crash because there
is no index 5. (this also applies to the inner arrays)

The fix is rather simple, we update our `move()` function
with the following code:
```python
def move(_direction):
    global current_pos_x, current_pos_y

    if _direction == "up":
        if (current_pos_x - 1) < 0:
            print("Oops! You can't go that way")
        else:
            current_pos_x -= 1
    elif _direction == "down":
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
        if (current_pos_y + 1) > (len(world[current_pos_x]) - 1):
            print("Oops! You can't go that way")
        else:
            current_pos_y += 1
```
What we changed is that we first check if the coordinate we 
are going to change, ends up being a "valid" coordinate.

The `up` and `left` direction are pretty simple to understand,
they should not be lower than the lowest index (_duhh_).

The `down` and `right` directions are a little harder.
What we want to achieve is the inverse of the above, we want
to prevent the coordinate being "larger than the largest index".

So how do we know what the "largest index" is?
We can use the `len()` function.
This function returns the length of an array.

Cool, so `len(world)` returns 5 (amount of items in the upper array),
but we said that the highest index was 4, not 5 ...
This is because `len()` returns the **amount** of items in an array.
And there are indeed 5 items. So to convert this to the largest index
we can just subtract 1 from it.

`len(world) - 1` will give us the index for the last item in the
array.

Now we can say "if the new x-coordinate is larger than the largest
x-coordinate" show an error to the user.

The same can be done for the y-coordinate, but we need to get the
largest index of the inner array the user is currently in.

Because we have multiple inner arrays, we use the `current_pos_x`
to get us the right inner array (remember, that `current_pos_x` holds
our current index for the upper array).

After we use that index we can then use the `len()` command like
we did for the x-coordinate.

Now the user cannot break the boundary because we do not actually
change the coordinate when he tries to go further.

# 1.5 - Inventory and items
Let's spice things up and give our user the ability to pickup
items in the world.

## Needed variables
First we need to define some items that should be available
in our world.

Create a new variable:
```python
items = [
    ("Sword", 1, "You found a brand new sword!"),
    ("Coins", 30, "You found a stack of coins!")
]
```
This array will hold all items that we can put in our world.
Each item has a name, amount and action message.
These properties will make more sense later on.

Now lets put these items in our world.
To do this we can make up a new tile to put in our world.

Let's make it "iX", where X is the index of the item inside
the `items` array. ("i0" is the "Sword" and "i1" is the "Coins" item)

Lets update our world and put these items in there:
```python
world = [
    ('x', 'x', 'x', 'y', 'x', 'x', 'x'),
    ('x', 'x', 'x', 'y', 'x', 'x', 'x'),
    ('x', 'y', 'i1', 'y', 'y', 'i0', 'y'),
    ('x', 'x', 'x', 'y', 'x', 'y', 'y'),
    ('x', 'x', 'x', 'x', 'x', 'x', 'x'),
]
```

## CheckTile()
Now we should make a function that allows the user to pickup the items.

Add the following function:
```python
def checkTile():
    tile = world[current_pos_x][current_pos_y]
    if tile.startswith('i'):
        item = items[int(tile.strip('i'))]
        print(item[2])
        addToInventory(item[0], item[1])
```
What this does is first store the tile, we are standing on, inside
a variable.

Next check if the tile(/string) starts with a "i".
If it does we now it is an "item tile".

If it does, we will first remove the "i" from the tile(/string),
by calling `tile.strip("i")` (strip() will remove a character from a string)

After `strip()` we are left with just the index number "0" instead of
"i0", but we cannot use this index number as it is, because it needs
to be an integer (now it is still a string, because `strip()` returns
a string).

To convert the string to an integer we use the `int()` method.
This will convert `"0"` (string) into `0` (integer).

Now we can use the result from `int()` as an index number
to get the right item from our `items` array and store it
inside a variable called `item`.

Because `items` is a 2 dimensional array, every item in the
upper array contains an array (inner array). So `item` is also
an array. It holds the name, amount and actions message.

We want to print out the action message by calling `print(item[2])`.
Index number 2 is the third item in the `item` array, which
points to the action message we defined.

Next we call a function that not yet exists called `addToInventory`.
We give the item name and item amount to it.

## AddToInventory()
Let's create that missing function:
```python
def addToInventory(item_name, item_amount):
    for i in range(0, item_amount):
        inventory.append(item_name)
    print("{}x {} have been added to your inventory!".format(item_amount, item_name))
```
This function expects an item name (string) and an item amount (integer).
What it does is, it adds the `item_name` to your `inventory` X amount of times.
Where X is the `item_amount`.

The `range()` function allows you to run the for-loop for a specified
amount of times. Each time the `i` variable increases with 1 (and starts
at 0). So you can use that variable inside the for-loop body. (we don't
use it here)

The `append()` function adds something to the end of an array.
We add the `item_name` to it.

Next, outside the for-loop, we tell the user how many of an item
he got added to his inventory.

## Game loop
To finish things off, we need to call our `checkTile()` function
to our game loop after the user has chosen a direction:
```python
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
```

This will make sure that AFTER we have moved, we will check on
what kind of tile we landed and execute the specifc action for
that tile.

Try it out, walk towards an item inside your world and see what
happens.

## Delay
It all happens kinda fast so lets add some delay after we got
the item's action message.

To do this add the following code at the top of your script:
```python
import time
```
This will import a python "package" (or library). It is just
a set of functions you can use in your code. This one is installed
with python so you can always use it. You can also use 3rd party
packages but you will have to download them first (this is outside
of the scope of this tutorial)

Now let's update our `addToInventory()` function:
```python
def addToInventory(item_name, item_amount):
    for i in range(0, item_amount):
        inventory.append(item_name)
    print("{}x {} have been added to your inventory!".format(item_amount, item_name))
    time.sleep(1)
```
We can call `time.sleep(X)` to wait for X seconds.
After the wait is over, the rest of the program continues.

Now if you walk onto an item tile, you will see the action message
and the other messages will appear a second later.

This is the end of part-1
