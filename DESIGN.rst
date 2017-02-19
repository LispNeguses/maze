===========
Maze Design
===========

Generating the Map
------------------
The map should be generated one line at a time and the generation function should be called with the previous line so that the maze exits will line up. A path should be generated at random from this condition and blockers should also be randomly placed.

::
   ## #### #
   #  #### #
   # ##    #
   #    ####         
   #s#######
   #########

The next line generated would then have to start with the same gaps and then extra blocks by the side could be generated. e.g.

::
   ##  ##  #
   ## #### #
   #  #### #
   # ##    #
   #    ####         
   #########

The starting line also falls off the bottom at this point. These paths can then continue from either of the blank spaces at each gap. There must always be at least two free spaces.
