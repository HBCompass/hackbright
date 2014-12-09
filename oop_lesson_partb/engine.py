#!/usr/bin/env python

import pyglet
from pyglet.window import key
from core import GameElement
from board import Board

SCREEN_X = 800
SCREEN_Y = 700

game_window = pyglet.window.Window(SCREEN_X, SCREEN_Y)
board = None

pyglet.resource.path = ["images/"]
pyglet.resource.reindex()

# Custom student changes
import game

IMAGES = {}
TILE_WIDTH = 0
TILE_HEIGHT = 0

# Setup mapping of images to be used in game
def setup_images():
    filenames = {
            "pikachu" : "pikachu.png",
            "Wall": "Wall Block.png",
            "Block": "Plain Block.png",
            "GrassBlock": "Grass Block.png",
            "StoneBlock": "Stone Block.png",
            "WaterBlock": "Water Block.png",
            "WoodBlock": "Wood Block.png",
            "ShortTree": "Tree Short.png",
            "TallTree": "Tree Tall.png",
            "Rock": "Rock.png",
            "Chest": "Chest Closed.png",
            "DoorClosed": "Door Tall Closed.png",
            "DoorOpen": "Door Tall Open.png",
            "BlueGem": "Gem Blue.png",
            "GreenGem": "Gem Green.png",
            "OrangeGem": "Gem Orange.png",
            "Heart": "Heart.png",
            "Key": "Key.png",
            "Boy": "Character Boy.png",
            "Cat": "Character Cat Girl.png",
            "Horns": "Character Horn Girl.png",
            "Girl": "Character Pink Girl.png",
            "Princess": "Character Princess Girl.png",
            "Star": "Star.png"
            }

    for k,v in filenames.items():
        i = pyglet.resource.image(v)
#        i.anchor_x = i.width/2
        i.anchor_y = i.height
        IMAGES[k] = i

    global TILE_WIDTH, TILE_HEIGHT
    TILE_WIDTH = i.width
    TILE_HEIGHT = i.height


# Called by clock to notify game elements of an update cycle
def update(dt):
    if game.GAME_BOARD:
        for el in game.GAME_BOARD.update_list:
            el.update(dt)

draw_list = []

@game_window.event
def on_draw():
    game_window.clear()
    for el in draw_list:
        el.draw()

# Main Keyboard Handler
# Called when a key is pressed, notifies all registered GameElements
@game_window.event
def on_key_press(symbol, modifiers):
    # Notify all objects registered to the board
    if game.GAME_BOARD:
        for item in game.GAME_BOARD.update_list:
            item.keyboard_handler(symbol, modifiers)

# Start the main game loop
def run():
    # Setup the images
    setup_images()

    # Create the game board
    try:
        board = Board(width=game.GAME_WIDTH, 
                      height=game.GAME_HEIGHT,
                      tile_width=TILE_WIDTH,
                      tile_height=TILE_HEIGHT,
                      screen_width=SCREEN_X,
                      screen_height=SCREEN_Y)

        board.IMAGES = IMAGES
        board.draw_board()

    except (AttributeError) as e:
        board = Board()
        
    game.GAME_BOARD = board


    # Set up an fps display
    try:
        if game.DEBUG == True:
            fps_display = pyglet.clock.ClockDisplay()
            draw_list.append(fps_display)
    except AttributeError:
        pass

    # Add the board and the fps display to the draw list
    draw_list.append(board)

    # Set up the update clock
    pyglet.clock.schedule_interval(update, 1/10.)
    game.initialize()
    pyglet.app.run()
    game.tripletown()
    #some other fucntion that runs things
    #game.tripletown()
    ### store the matrix
    ### get_el() = > tell us what's at x,y

if __name__ == "__main__":
    run()
