import pyglet
pyglet.resource.path = ['../resources/shooter/PNG', '../resources/cavern_ruins']
pyglet.resource.reindex()

def center_image(image):
    """ Sets an image's anchor point to its center  """
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

player = pyglet.resource.image('Survivor 1/survivor1_stand.png')

center_image(player)


