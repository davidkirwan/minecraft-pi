# David Kirwan https://github.com/davidkirwan/minecraft-pi
#
# Tutorial 1
#
# Delete a cube of earth

import minecraft
import block
import time

# Create the minecraft object
mc = minecraft.Minecraft.create()


# Clear a cube of earth
for x in range(10, 10):
    for y in range(-10, 10):
        for x in range(-10, 10):
	    mc.setBlock(x, y, z, block.AIR)

