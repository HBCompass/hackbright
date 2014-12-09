import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
######################


##set the size of the game board

GAME_WIDTH = 10
GAME_HEIGHT = 10

#### Put class definitions here ####

#create a class, and then add an image. check engine.py to see if image is in dictionary
class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False

#allows player to interact with gem, picks it up when it touches it.
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a gem! You have %d items." %(len(player.inventory)))

class Wall(GameElement):
    IMAGE = "Wall"
    SOLID = True

#change this
class Ramp(GameElement):
    IMAGE = "pikachu"
    SOLID = True

#prototype for an element that does not interact and doesn't allow player to move
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

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

                existing_el = self.board.get_el(next_x, next_y)

                if existing_el:
                    existing_el.interact(self)

                if existing_el and existing_el.SOLID:
                    self.board.draw_msg("There is something in my way!")

                elif existing_el is None or not existing_el.SOLID:
                    self.board.del_el(self.x, self.y)
                    self.board.set_el(next_x, next_y, self)

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []


####   End class definitions    ####

def initialize():
    """Put game initialization code here"""

#make a list of tuples and decide where rocks will live    
    rock_positions = [
        (2, 1),
        (1, 2),
        (3, 2),
        (2, 3)
        ]
#create a list with rock postions. can then access individual rocks from the list.
    rocks = []
#for loop iterating over the rocks and actually placing them
    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

#example of interacting with a rock and making it edible
    rocks[-1].SOLID = False

#instantiating player
    player = Character()
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(2, 2, player)
    
#instantiating gem
    GAME_BOARD.draw_msg("This game is wicked awesome.")
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3,1,gem)
#same deal as with rocks, but this time with a wall
    wall_positions = [
        (5, 1),
        (5, 2),
        (5, 3),
        (5, 4),
        (5, 6),
        (5, 7),
        (5, 8),
        (5, 9)
        ]

    walls = []
    for position in wall_positions:
        wall = Wall()
        GAME_BOARD.register(wall)
        GAME_BOARD.set_el(position[0],position[1],wall)
        walls.append(wall)

#make a water ramp
    rampwest = Ramp()
    GAME_BOARD.register(rampwest)
    GAME_BOARD.set_el(4,5,rampwest)