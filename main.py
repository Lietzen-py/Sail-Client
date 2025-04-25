#    Sail client and any of its modules are covered under the GNU Public usage licence, see License.MD for more info
#    Copyright (C) 2025  Lietzen (gameyoshis@gmail.com)
# global vars
global currentsource
global downloadstats

# init stuff


from logger import *
logger("debug", "finding sources...")
from getsrc import *

sourceamt = getsource(2)
logger("debug", f"{sourceamt} Sources found.")
import pyglet # type: ignore

logger("debug", "spawning window")
window = pyglet.window.Window()
label = pyglet.text.Label(f'{sourceamt}',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
# future drop down code
def listsrc():
    label = pyglet.text.Label(f'{sourcenames()}',
                          font_name='Times New Roman',
                          font_size=36,
                          x=0, y=0,
                          anchor_x='center', anchor_y='center')
# more poc than anything
print(f'sources {sourcenames()} loaded')
listsrc()
@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()