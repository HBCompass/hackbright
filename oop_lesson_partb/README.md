Object Oriented Programming
===========================
This game requires python2.6 or greater and pyglet 1.1.4, as of the time of writing.

This tutorial walks you through building a game using [Danc's Miraculously Flexible Game Prototyping Graphics for Small Worlds](http://www.lostgarden.com/2007/05/dancs-miraculously-flexible-game.html). We've built a (relatively brittle) game engine on top of the [Pyglet game library](http://www.pyglet.org/), a small OpenGL-based game library for python.

Here's a small sample of what the output could look like when you're done.

![Screenshot](http://i.imgur.com/M1cV3eT.jpg)

Step 0: Getting started
-------------------------
To get all the files you need to be able to run the game, clone this repository to your local machine. Creating a new repo on GitHub to save your game is an exercise left to the reader.

We'll be editing **only** the code in ```game.py```. To run the game type ```python engine.py``` at the command line. After every step, run and experiment with the program to see how each addition changes it.

**Read through each section before you type anything and NO COPY/PASTE.**

Step 1: Let's add something to the game
----------------------------------------
The first thing we're going to do is add boulders to our game. First, we need to _define_ what a boulder is. We create a class definition in ```game.py``` as follows:

    class Rock(GameElement):
        IMAGE = "Rock"

What this says is that we're creating a new data type called 'Rock'. It's derived from an existing data type called GameElement. 'GameElement' objects have certain behaviors we have pre-defined that are required for the game to run, but you don't have to concern yourself with them here.

The second line of the class definition says that the Rock element has a **class attribute** called 'IMAGE', currently set to rock. A class attribute is an attribute that is shared between all instances of a class. This is distinct from regular attributes, which are distinct per instance. We'll explore this idea later.

The next thing we need to do is to actually create a single rock and place it on the board. The code to create an instance of a class looks like this:

    rock = Rock()

Simply calling the class as if it were a function creates a new rock for us to use. Here, we assign it to the variable 'rock'.

As a quirk of this particular game engine we've written, we have to register this rock with the game board so that it displays. We do that by calling ```GAME_BOARD.register()```. After that, the rock can then be placed on the board with the ```GAME_BOARD.set_el()``` method. For the purposes of this exercise, when we place objects on our game board, we put the code in the ```initialize()``` function. The full code for that looks like this. 

**DO NOT COPY/PASTE PLZ**

    def initialize():
        """Put game initialization code here"""
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(1, 1, rock)
        print "The rock is at", (rock.x, rock.y)

The ```set_el``` function takes in three elements, the x position, the y position, and the element you're placing at that position. If you imagine the game board as a grid, the top-left position is 0,0, and the bottom right is 2,2.

Try changing the position and see how the rock moves around. Notice the ouput of the print statement here.  You never set ```rock.x```, can you figure how it got set?

Step 2: Increase the board size
-------------------------------
We need a little more room to do something interesting with our game. Let's increase the board size to a 4x4 grid. We do this by updating the ```GAME_WIDTH``` and ```GAME_HEIGHT``` variables. The top left is still 0,0, but the bottom right is now 3,3.

Step 3: Put more stuff on the board
-----------------------------------
Let's look at how to add a couple more boulders to the game. Each rock needs to be registered and set on the ```GAME_BOARD``` independently. Each rock also needs its own variable. Change your initialize function to look like the following.

**>:[ SRSLY NO COPY/PASTE**

    def initialize():
        """Put game initialization code here"""

        # Initialize and register rock 1
        rock1 = Rock()
        GAME_BOARD.register(rock1)
        GAME_BOARD.set_el(1, 1, rock1)

        # Initialize and register rock 2
        rock2 = Rock()
        GAME_BOARD.register(rock2)
        GAME_BOARD.set_el(2, 2, rock2)

        print "The first rock is at", (rock1.x, rock1.y)
        print "The second rock is at", (rock2.x, rock2.y)
        print "Rock 1 image", rock1.IMAGE
        print "Rock 2 image", rock2.IMAGE

Try adding more rocks and playing around with placement. See what happens when you try to place a rock outside the bounds of the game grid.

Note the .x and .y attributes of rock1 and rock2. These are 'instance' attributes (usually just 'attributes'). Notice how they are different for each rock. On the other hand, both rocks share the same IMAGE class attribute we described in step 1.

Again, class attributes are shared between all instances of the class. If we had a class called Human, we might correctly add a class attribute NUM\_OF\_EYES = 2, whereas each instance of Human would have an attribute called .name, which would be distinct between each human.

Step 4: More expansion
----------------------
We're going to expand the game board to 5x5, once again by modifying the ```GAME_WIDTH``` and ```GAME_HEIGHT``` variables.

    GAME_WIDTH = 5
    GAME_HEIGHT = 5

We're also going to place four rocks in a cross pattern in the center of the board. It will look something like this:

    Stars represent rocks, dots represent empty spaces

    +---+
    |.*.|
    |*.*|
    |.*.|
    +---+

In our grid, this means a rock at (2, 1), (1,2), (3, 2), and (2, 3)

This time, instead of making four separate variables for each rock, we're going to instantiate each rock in a list. First, we'll make a list of the rock positions, and an empty list for all of our rock instances/objects:

    rock_positions = [
            (2, 1),
            (1, 2),
            (3, 2),
            (2, 3) 
        ]
    rocks = []

Then, we're going to loop through our list of positions, and for each position, we'll create and register a new rock object with our ```GAME_BOARD```.

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

Put all together, our ```initialize``` function looks like this:

    def initialize():
        """Put game initialization code here"""
        rock_positions = [
                (2, 1),
                (1, 2),
                (3, 2),
                (2, 3) 
            ]

        rocks = []
        for pos in rock_positions:
            rock = Rock()
            GAME_BOARD.register(rock)
            GAME_BOARD.set_el(pos[0], pos[1], rock)
            rocks.append(rock)

        for rock in rocks:
            print rock

Note at the end, we print each individual rock out of the list. Try playing around with the number of rocks on the board, manipulating them just with the list.

Step 5: Adding a Character class
-----------------------------
Rocks are pretty cool, but this game would be way better if we had something else on the board besides rocks. We're going to add a ```Character``` class to our game. We will use this as a base for our player representation in the game (our Player Character, or PC). This class will only be instantiated (created) once, as we only have one player. Later, you might add other game characters that aren't controlled by the player (Non-Player Characters, NPCs).

Once placed on the board, our player object (or really any object we place on the board) will have it's own "life".  That means it will be responsible for responding to events that happen in the world (the game board), how it moves, how it interacts with other objects, how it dies.  One of the advantages of Object Oriented Programming is this idea that each object is responsible for itself.  If you want the object to move, you place the code to handle the movement on the object's class.  We'll explore that idea more as we go on, but lets start by making our Character.

The class definition for Characters look like this:

    class Character(GameElement):
        IMAGE = "Girl"

Note again that just like our ```Rock```, it is derived from a ```GameElement```.  It has a class attribute called ```IMAGE``` that has the value "Girl". This tells the game engine to use the 'Girl' image.

Register it in your ```initialize``` function after you register your rocks. Place it at position (2,2).

    # In the initialize() function
    player = Character()
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(2, 2, player)
    print player

There are a few other images which we can use for our player character. Try one of the following:
    "Boy", "Cat", "Princess", "Horns"


Step 6: And now a message from our sponsors
-------------------------------------------
We need a way to display a message on the screen. Fortunately, you don't have to figure that out, we've added one for your. Add the following line at the end of your ```initialize``` function.

    GAME_BOARD.draw_msg("This game is wicked awesome.")

There's also a related function, ```GAME_BOARD.erase_msg()```.

Step 7: Keyboard interaction
----------------------------
So now we have a ```Rock``` and a ```Character``` that are both themselves ```GameElements``` (that is to say, they inherit from the ```GameElement``` class).  But what does this mean?  Why not just make everything a ```GameElement```?

Our game ```Board``` knows how to draw ```GameElements```, so anything that is a ```GameElement``` can be displayed on our ```Board```.  Our ```Rock``` is just a ```GameElement``` with a default ```IMAGE``` specified, but we could have achived the same effect by doing something like this:

    # Don't actually write this
    rock = GameElement()
    rock.IMAGE = "Rock"
    GAME_BOARD.register(rock)
    GAME_BOARD.set_el(1, 2, rock)

But now we want to create our ```Character```.  Our ```Character``` is a "smarter" ```GameElement```.  It can move.  A ```Rock``` can't move, so no sense in putting code to handle movement in the ```Rock``` class.  It also doesn't make sense to put that code in the ```GameElement``` class, since not every object on our board can move.  Also, what does it mean to move?  For our character it means move one space when an arrow key is pressed.  Maybe we'll want different types of characters, maybe some that can move two spaces.  Our Character will know what it means to move so our code to handle movement should be placed in our ```Character``` class.

Now it's time to make our game interactive by adding keyboard capabilities.

The thing to note about they keyboard here is that we can no longer use the ```raw_input``` function we've been using in previous exercises. When building a game, we can't expect our user to hit enter every time they press a key. Instead, we need to be notified when a key is pressed.

Up until now, we've thought of the keyboard as a source of input that feeds us characters one at a time in a stream. Another way to think of the keyboard is as an "event" that occurs when a key is pressed.

Our game engine activates the keyboard in this second manner, and we just need to write the code that needs to run when that event happens (instead of constantly checking to see if a key has been pressed).

Because our game engine spends a lot of time dealing with graphics, we have to give it control of our main loop. Otherwise, we'd have to draw everything ourselves.  Any object that is on our board can be made aware that an event (like a key being pressed) has happened, but only objects that actually care about that event need to have a handler.

Inside our ```Character``` class, create a function called ```keyboard_handler```.  This function will be called by the ```Board``` every time a key is pressed:

    def keyboard_handler(self, symbol, modifier):
        if symbol == key.UP:
            self.board.draw_msg('%s says: "You pressed up!"' % self.IMAGE)
        elif symbol == key.SPACE:
            self.board.erase_msg()

The ```symbol``` argument is the character code of the key that was pressed.  The ```key``` module contains friendly mappings of those codes to the symbol numbers.  (It's much nicer to write ```if symbol == key.UP:``` instead of ```if symbol == 65362:```).  Modifier lets you know if a modifier key (Shift, Ctrl, Alt) was also pressed at the same time at the same time.

Also note that we're using ```self.board``` to refer to the game board instead of the ```GAME_BOARD``` variable.  Every ```GameElement``` has a link to the game board set at ```.board```.  By using that, we avoid using global variables and our code is more portable (say our Class starts to get really big and we want to move it to its own file).

Try adding a message for each direction key on the keyboard, ie: _down_, _left_, _right_.

Step 8: Motion
--------------
The way we simulate motion is by reading a key, figuring out where our character will go, then removing them from the board and setting them at their new position.

When we want to move up, our character's 'y' position decreases by 1. If it moves down, it increases. Left is -1 in the x direction, and right is +1.

The implementation looks like this:

    def keyboard_handler(self, symbol, modifier):
        if symbol == key.UP:
            self.board.draw_msg('%s says: "You pressed up!"' % self.IMAGE)
            next_y = self.y - 1
            self.board.del_el(self.x, self.y)
            self.board.set_el(self.x, next_y, self)

Add conditions for every direction.

Step 9: Instance methods
------------------------
We're going to simplify things by adding behavior to our character object. In theory, our ```Character``` class 'encapsulates' the behavior and data related to characters in our game. In this example, our character knows its own 'x' and 'y' position. Similarly, if we ask it to move in a direction, it should also know what its new position is.

    print (player.x, player.y)
    => (1, 1)
    print player.next_pos("up")
    => (1, 0)
    print (player.x, player.y)
    => (1, 1)

Note that finding out what the next position is does not actually move the player we do that manually.
We add an instance method to our ```Character``` class like so:

    class Character(GameElement):
        IMAGE = "Girl"

        def next_pos(self, direction):
            if direction == "up":
                return (self.x, self.y-1)
            elif direction == "down":
                return (self.x, self.y+1)
            elif direction == "left":
                return (self.x-1, self.y)
            elif direction == "right":
                return (self.x+1, self.y)
            return None

Note the unusual parameter ```self``` that seems to disappear when we call it:

    def next_pos(self, direction):

    # but when we call it later:

    player.next_pos("up")

An instance method can be thought of as being _inside_ a particular instance. From inside that instance, the method needs a variable to refer to the instance it's inside of, thus the ```self``` parameter.

Update your keyboard handler to use the new ```.next_pos()``` method. We first decide which direction the player is trying to move by checking the keyboard with a big ```if``` statement

    direction = None
    if symbol == key.UP:
        direction = "up"
    elif symbol == key.DOWN:
        direction = "down"
    elif symbol == key.LEFT:
        direction = "left"
    elif symbol == key.RIGHT:
        direction = "right"

Then we feed the direction to ```next_pos``` to find out the location the player is trying to move to.

    if direction:
        next_location = self.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

Lastly, we move the player to the new location by deleting them from their old position and re-setting them in their new position:

    self.board.del_el(self.x, self.y)
    self.board.set_el(next_x, next_y, self)

All together, it looks like this:

    class Character(GameElement):
        IMAGE = "Girl"

        def next_pos(self, direction):
            if direction == "up":
                return (self.x, self.y-1)
            elif direction == "down":
                return (self.x, self.y+1)
            elif direction == "left":
                return (self.x-1, self.y)
            elif direction == "right":
                return (self.x+1, self.y)
            return None

        def keyboard_handler(self, symbol, modifier):

            direction = None
            if symbol == key.UP:
                direction = "up"
            elif symbol == key.DOWN:
                direction = "down"
            elif symbol == key.LEFT:
                direction = "left"
            elif symbol == key.RIGHT:
                direction = "right"

            self.board.draw_msg("[%s] moves %s" % (self.IMAGE, direction))

            if direction:
                next_location = self.next_pos(direction)

                if next_location:
                    next_x = next_location[0]
                    next_y = next_location[1]
                    self.board.del_el(self.x, self.y)
                    self.board.set_el(next_x, next_y, self)

Run the program and see how these changes affect the game.

Step 10: Rock Solid
-------------------
Whoah, we just walked through that boulder. Not only that, but we _ate_ it, as well. That's no good. We need some way to interact with the boulder. Or, more specifically, prevent us from interacting with it.

The first thing to do is look before we move. This means, after determining our next position, checking the board to see if there's anything already there. We can use the ```.get_el``` method on our board. In our ```keyboard_handler``` method:

    if direction:
        next_location = self.next_pos(direction)
        if next_location:
            next_x = next_location[0]
            next_y = next_location[1]

            existing_el = self.board.get_el(next_x, next_y)


Now, we could just see if the ```existing_el``` is an object of type ```Rock``` by using the ```isinstance()``` function. But what if there are other things that aren't rocks that we don't want to walk through? We need a more general way to do this.

We can make this 'walkability' an intrinsic property of all ```Rocks``` by adding a new 'class attribute' to the ```Rock``` class.

    class Rock(GameElement):
        IMAGE = "Rock"
        SOLID = True

Now, every instance of ```Rock``` will have the attribute ```SOLID``` set to true. Interestingly, we can have the unusual behavior of setting individual Rocks to not be solid at our discretion.

Instead of checking whether or not the existing element we're about to walk over is a rock, we can just check whether or not it's solid:

    if existing_el and existing_el.SOLID:
        self.board.draw_msg("There's something in my way!")
    elif existing_el is None or not existing_el.SOLID:
        self.board.del_el(self.x, self.y)
        self.board.set_el(next_x, next_y, self)

All together:

    if direction:
        next_location = self.next_pos(direction)
        if next_location:
            next_x = next_location[0]
            next_y = next_location[1]

            existing_el = self.board.get_el(next_x, next_y)

            if existing_el and existing_el.SOLID:
                self.board.draw_msg("There's something in my way!")
            elif existing_el is None or not existing_el.SOLID:
                self.board.del_el(self.x, self.y)
                self.board.set_el(next_x, next_y, self)


Step 11: It's a trap!
---------------------
Uh-oh, we're trapped! We're surrounded by four solid rocks! Remember what we said when we could modify individual rocks and override the class attribute? Let's do that now. We can take a particular rock instance and change its solidity. In our ```initialize``` function, after we create and register our rocks, let's change the bottom-most one to be intangible. We can access the last rock in our list and change the ```.SOLID``` attribute. In our ```initialize``` method:

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    rocks[-1].SOLID = False

Step 12: Freedom! Sweet, boring freedom!
----------------------------------------
Woo, we can move around. That's awesome. But our game is still kinda boring. Let's add a shiny bauble to our game.

    class Gem(GameElement):
        IMAGE = "BlueGem"
        SOLID = False

Register and set the gem at (3,1) in your ```initialize``` function, as before.

    GAME_BOARD.draw_msg("This game is wicked awesome.") 
    # Add these lines
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3, 1, gem)

One thing to remember is that the name of our classes isn't really important. We could have easily written the following instead:

    class ShinyBauble(GameElement):

The important thing about the class definition is that we properly inherit from the ```GameElement``` class so that they behave properly in our game.

Step 13: Remembering things that happened
-----------------------------------------
When we walk over our gem, it simply disappears. We need a way to remember that we've acquired an item, so we add state to our player characters. In game parlance, we can say that our character has an inventory. This is a property of a particular character, our game character. Given that we might have multiple characters later, we make the inventory an instance attribute of our ```Character``` class.

To do this, we need to add an initializer to say that when we create a ```Character```, it starts with an empty inventory. Our inventory can be a simple list of objects our character is carrying.

In the ```Character``` class, add:

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

This is an initializer. It "sets up" our object with initial values. Here, we're telling the character that it must have an empty list as an inventory to start. 

Notice the line, ```GameElement.__init__(self)```. To be a proper game element, there was some behavior defined on the ```GameElement``` class to interact with the board correctly. When we add an initializer to our class, we need to tell our class that it still needs to do those things, so we call the parent class' initializer.

Next, we need a way for our player to 'interact' with an object. In fact, we want the player to interact with pretty much every object on the board. Most of the time, the interactions won't produce anything, but we do it anyway. In the ```keyboard_handler```:

    existing_el = self.board.get_el(next_x, next_y)
    # Add after this line

    if existing_el:
        existing_el.interact(self)

Now, whenever the player tries to bump into an object, our character will try to interact with it first. The default behavior for interaction is to do nothing. This is defined on the ```GameElement``` class. We want to override the behavior when a player interacts with a ```Gem```. We want that gem to be added to the player's inventory. It will take the following format:

    player.inventory.append(gem)

To do that, we modify the ```Gem``` class and add the ```interact``` method. Whenever the gem interacts with a player, it gets added to their inventory and a message displays:

    class Gem(GameElement):
        def interact(self, player):
            player.inventory.append(self)
            GAME_BOARD.draw_msg("You just acquired a gem! You have %d items!"%(len(player.inventory)))

(Our game is getting quite big, if you can't figure out where to add these lines, check the reference implementation in ```game_ref.py```.)

Experiment with adding different gems that have different interaction behaviors. For example, you could print different messages, or maybe touching a certain type of gem resets the user position to the starting point.

Step 14: Get Clever, Have Fun
-----------------------------
Congratulations, you have a game. Sort of. It's not all that interesting, and it definitely could be better. You can spend some time looking at ```engine.py``` to see how it all works (be careful, there be dragons there). You *might* even need to edit ```engine.py``` in order to do some of the fancier things you want to do. Be careful and test as you go!

More interestingly, spend some time playing with object interactions, adding more objects and classes to your game, and fixing some bugs. Here are some ideas:

* Fix the game so it doesn't crash when you go beyond the game board boundaries.
* Add other elements to the game, keys, chests, doors
* Add conditional interactions: a door that won't open unless you have the right colored gem,
chests that won't open unless you have the right key.
* Subclass the Character class to make non-player characters that speak messages when you interact with them.
* Tricky: Add blocks that slide when you push them.

Here's a list of all the sprites (game images) that the game engine understands. Similar to our Rock, Gem, and Character classes, create one and set the IMAGE class property to the appropriate image.

    Wall
    Block
    GrassBlock
    StoneBlock
    ShortTree
    TallTree
    Rock
    Chest
    DoorClosed
    DoorOpen
    BlueGem
    GreenGem
    OrangeGem
    Heart
    Key
    Boy
    Cat
    Horns
    Girl
    Princess

Mostly, be clever with this and have fun! Classes, woo.

### Ok, these ideas sound cool, but I'm still a little stuck...
Ok, have some [hints](HINTS.md).

### Holy wow, this is so awesome, I want to work on it at home!!
Ok, but beware ... it (may or may not be) straightforward. [Here's some tips for getting it set up on Mac OSX.](https://github.com/hackbrightacademy/oop_lesson/wiki)

### Licensing
The material presented here is copyrighted by [Hackbright Academy](http://www.hackbrightacademy.com/), and is part of our fellowship program curriculum. It is currently free for personal use.
