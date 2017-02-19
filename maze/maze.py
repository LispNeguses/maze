import pyglet
import resources
from player import Player
from pyglet.window import key

game_window = pyglet.window.Window(1200, 800)

@game_window.event
def on_draw():
    game_window.clear()
    player.draw()

batch = pyglet.graphics.Batch()
player = Player(game_window, batch=batch)

game_objects = [player]
def update(dt):
    for obj in game_objects:
        obj.update(dt)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
