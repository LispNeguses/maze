import pyglet
import level
from pyglet.gl import *


class Maze():
    def __init__(self, columns, rows, row_getter):
        self._scale = 3
        self.columns = columns
        self.rows = rows
        self._movement_steps = 0
        self._last_row = [' ']
        self._last_row.extend(['#']*(columns-len(self._last_row)))
        self.grid_size = 16
        self._get_row = row_getter
        self._maze = []
        tiles = pyglet.image.ImageGrid(
            pyglet.resource.image('16x16-tiles_0.png'),
            5, 7, row_padding=1, column_padding=1)
        tiles_texture = tiles.texture.target
        glTexParameteri(tiles_texture, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(tiles_texture, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        self._wall = tiles[(4,4)]
        self._ground = tiles[(4,1)]
        self._treasure = tiles[(0,0)]
        self._batch = pyglet.graphics.Batch()
        self._start_maze()

    def _make_row_of_sprites(self, row_index):
        row = []
        column = 0
        self._last_row = self._get_row(self._last_row)
        for cell in self._last_row:
            if cell == "#":
                row.append(pyglet.sprite.Sprite(self._wall, batch=self._batch))
            elif cell == " ":
                row.append(pyglet.sprite.Sprite(self._ground,
                                                batch=self._batch))
            elif cell == "t":
                row.append(pyglet.sprite.Sprite(self._treasure,
                                                batch=self._batch))
            else:
                raise
            row[-1].x = 16 * column * self._scale
            row[-1].y = 16 * row_index * self._scale
            row[-1].scale = self._scale
            column += 1
        return row

    def _start_maze(self):
        self._maze = []
        for row in range(self.rows):
            self._maze.append(self._make_row_of_sprites(row))

    def extend_maze(self):
        self._maze.pop(0)
        self._maze.append(
            self._make_row_of_sprites(self.rows + self._movement_steps))
        self._movement_steps += 1

    def draw(self):
        glPushMatrix()
        glTranslatef(0.0, -self._movement_steps*16*self._scale, 0.0)
        self._batch.draw()
        glPopMatrix()


def main():
    tiles = pyglet.image.ImageGrid(pyglet.resource.image('16x16-tiles_0.png'),
                                   5, 7, row_padding=1, column_padding=1)
    wall = pyglet.sprite.Sprite(tiles[(4,4)])
    wall.x = 100
    wall.y = 100
    wall.scale = 3
    return wall

if __name__ == '__main__':
    def row_getter(columns):
        return '### #' + '#'*(columns-5)
    pyglet.resource.path = ['../resources', 'resources']
    pyglet.resource.reindex()
    w = pyglet.window.Window(width=384, height=384)
    wall = main()
    maze = Maze(8, 8, level.generate_level_line)
    @w.event
    def on_draw():
        w.clear()
        wall.draw()
        maze.draw()
        maze.extend_maze()
    pyglet.app.run()
