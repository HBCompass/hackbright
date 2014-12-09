import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys
import random

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
######################


##set the size of the game board

GAME_WIDTH = 7
GAME_HEIGHT = 7

#### Put class definitions here ####

class ShortTree(GameElement):
    IMAGE = "ShortTree"
    SOLID = True

class Piece(GameElement):
    is_placed = False
    def __init__(self, piece_type):
        #pick which piece type
        # self.piece_type = random.choice(["Rock","GreenGem","Star"])
        # IMAGE = self.piece_type
        self.piece_type = piece_type
        GAME_BOARD.draw_msg("You just acquired a %s! Move your piece with the arrow keys and place with spacebar" % self.piece_type)
        print(self.piece_type)

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        elif direction == "putdown":
            return (self.x, self.y)
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
        elif symbol == key.SPACE:
            direction = "putdown"

        
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

        if direction == "putdown":
            #turn on flag
            self.is_placed = True


            #determine how to update matrix
            if self.piece_type == "Rock":
                the_type = 1
            elif self.piece_type == "GreenGem":
                the_type = 2
            elif self.piece_type == "Star":
                the_type = 3
            else:
                the_type = 0

            #update matrix
            self.board.placed_pieces[self.y][self.x] = the_type

            #check our matrix horizontally
            horizontal_check = []
            for j in range((self.x - 2),(self.x + 3)):
                horizontal_check.append(self.board.placed_pieces[self.y][j])

            hc_str = ''.join(str(e) for e in horizontal_check)

            vertical_check = []
            for i in range((self.y - 2),(self.y + 3)):
                vertical_check.append(self.board.placed_pieces[i][self.x])
                
            vc_str = ''.join(str(e) for e in vertical_check)





            #print self.board.placed_pieces


            # #need to put that piece down there forever:
            # self.board.set_el(self.next_pos(direction)[0],self.next_pos(direction)[1],self)

            # #supposed to create a new random piece
            # new_piece = make_random_piece()
            # GAME_BOARD.register(new_piece)
            # new_piece_position = self.next_pos(direction)
            # new_x = new_piece_position[0] + 1
            # new_y = new_piece_position[1]
            # GAME_BOARD.set_el(new_x,new_y,new_piece)


            # print("gets here?")
            # direction = None
            

            # new_piece = [next_x, next_y, self.piece_type]
            # x,y, piece_type = new_piece



class Rock(Piece):
    IMAGE = "Rock"
    def __init__(self):
        self.piece_type = "Rock"
        return super(Rock, self).__init__("Rock")

class GreenGem(Piece):
    IMAGE = "GreenGem"
    def __init__(self):
        self.piece_type = "GreenGem"
        return super(GreenGem, self).__init__("GreenGem")

class Star(Piece):
    IMAGE = "Star"
    def __init__(self):
        self.piece_type = "Star"
        return super(Star, self).__init__("Star")


####   End class definitions    ####
def make_random_piece():
    first_piece_class = random.choice(["Rock","Star","GreenGem"])

    if first_piece_class == "Rock":
        first_piece = Rock()
    elif first_piece_class == "GreenGem":
        first_piece = GreenGem()
    else:
        first_piece = Star()
    return(first_piece)



def initialize():
    """Put game initialization code here"""

    tree_positions = []

    for i in range(7):
        tree_positions.append([0,i])
    for i in range(1,7):
        tree_positions.append([i,0])
    for i in range(1,7):
        tree_positions.append([6,i])
    for i in range(1,6):
        tree_positions.append([i,6])



    trees = []
    for pos in tree_positions:
        tree = ShortTree()
        GAME_BOARD.register(tree)
        GAME_BOARD.set_el(pos[0], pos[1], tree)
        trees.append(tree)

    a_piece = make_random_piece()
    GAME_BOARD.register(a_piece)
    first_x = random.randint(1,5)
    first_y = random.randint(1,5)
    GAME_BOARD.set_el(first_x,first_y,a_piece)

    GAME_BOARD.placed_pieces = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]


    print ("this is the game board init")
    print GAME_BOARD.placed_pieces

         #   GAME_BOARD.placed_pieces[i].append([0,0,0,0])


    #get some sort of method from the piece class
    #to then modify board matrix

    


