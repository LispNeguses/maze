import physicalobject, resources
from pyglet.window import key

class Player(physicalobject.PhysicalObject):
    def __init__(self, window, *args, **kwargs):
        super(Player, self).__init__(img=resources.player, *args, **kwargs)
        window.push_handlers(self.on_key_press)
        window.push_handlers(self.on_key_release)
    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.rotation = 180
            self.velocity_x = -500
            self.velocity_y = 0
        elif symbol == key.RIGHT:
            self.rotation = 0
            self.velocity_x = 500
            self.velocity_y = 0
        elif symbol == key.UP:
            self.rotation = 270
            self.velocity_x = 0
            self.velocity_y = 500
        elif symbol == key.DOWN:
            self.rotation = 90
            self.velocity_x = 0
            self.velocity_y = -500
    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.velocity_x = 0
            self.velocity_y = 0
        elif symbol == key.RIGHT:
            self.velocity_x = 0
            self.velocity_y = 0
        elif symbol == key.UP:
            self.velocity_x = 0
            self.velocity_y = 0
        elif symbol == key.DOWN:
            self.velocity_x = 0
            self.velocity_y = 0

