oop_lesson: Hints!
==================

Here's some ideas and code snipits for some ways you can add some additional functionality to your game.  You're in no way limited to just these ideas.  Explore and have fun!

Change Class Image
------------------
Want to change the color of a gem?  Open a door or chest?  Then you want to change which image is used to represent the class.

The .IMAGE attribute on a class is just a text string.  Changing that after the class has been been registered on the board will not have any affect on the display of the game board.  In order to change the image, you need to call the ```.change_image(i)``` method and pass the name of the new image you would like displayed.

For example:

	class Door(GameElement):
	    IMAGE = "DoorClosed"
	    SOLID = True

	    def interact(self, player):
	        if self.IMAGE == "DoorOpen":
	            self.SOLID = False

	        if self.IMAGE == "DoorClosed":
	            self.change_image("DoorOpen")


Moving NPC
----------
Lots of games of this style have AI or Non-Player Character (NPC) objects or enemies that moves automatically.  You should be able to create a class for your enemy character, but how do you make them move on their own?  Where would you put that code?

Something needs to happen to tell the NPC it's time to move.  So far, one of the places we've seen that we can put this type of logic has been in the ```keyboard_handler``` class we created on the Character.  Nothing stopping us from creating our ```BadGuy``` class with its own ```keyboard_handler```.  For the NPC, we don't necessarily need to care which key was pressed, only the action of pressing a key is enough to trigger movement.

If you want a turn-based game (player makes a move, enemy takes a move), the ```keyboard_handler``` is the perfect place for that type of game logic to go.

Automaticly Moving NPC
--------------------
Suppose you wanted the NPC to move on their own, without requiring input from the user?

You might think of writing something like this:

	# DON'T DO THIS
	class BadGuy(GameElement):
		IMAGE = 'Cat'

		def __init__(self):
			GameElement.__init__(self)
			self.direction = 1
			while True:
				next_x = self.x + self.direction

				if next_x < 0 or next_x >= self.board.width:
					self.direction *= -1
					next_x = self.x

				self.board.del_el(self.x, self.y)
				self.board.set_el(next_x, next.y, self)

We've said with OOP that same game object has it's own "life", so the idea that we could create a while loop on the BadGuy and just say keep moving back and forth along the x-axis isn't necessarily a bad one.  However, Python is still single-threaded.  That means it can only do one thing at a time.  If you create an infinite loop like above, Python will only be able to move the BadGuy and no other game logic can happen.

What we need is something like a game clock, telling us that it's time for our NPC to move.  (You don't want to be constantly moving anyway, you'd move to fast for anyone to see!)  Lucky for us, the game engine has a clock built in that calls the ```.update()``` function of every GameElement registered to the board.  It's called every 1/10 of a second.

So we can re-write our NPC movement logic as follows:

	class BadGuy(GameElement):
	    IMAGE = "Cat"
	    direction = 1

	    def update(self, dt):

	        next_x = self.x + self.direction

	        if next_x < 0 or next_x >= self.board.width:
	            self.direction *= -1
	            next_x = self.x

	        self.board.del_el(self.x, self.y)
	        self.board.set_el(next_x, self.y, self)

If you try this code out, you may notice the NPC still moves kind of fast (remember, update() gets called every 1/10 second).  How would you slow it down?

Try moving your Character in the path of the NPC.  What happens?  What would you want to have happen?


Changing the Board Tiles
------------------------
The game board is a grid of tiles.  ```board.width``` and ```board.height``` define the size of the nested (2D) lists that are used to store the tiles in ```board.base_board```.

So for example, if the tile in (3, 2) is a GrassBlock, ```board.base_board[2][3] == 'GrassBlock'```.

If you'd like to change the background tiles displayed, update the values in ```board.base_board[y][x]``` with the names of the new tiles and then called the ```board.draw_game_map()``` function.

Note: if you're inside a GameElement, you can access the game board using ```self.board```.

