# David Kirwan https://github.com/davidkirwan/minecraft-pi
#
# Tutorial 2
#
# Create a square, then delete it in an infinite loop

import minecraft
import block
import time

# Create the minecraft object
mc = minecraft.Minecraft.create()


while True:
    for x in range(0, 10):
        mc.setBlock(-5, x, 0, block.STONE)
	time.sleep(0.0.5)

    for x in range(-5, 5):
        mc.setBlock(x, 10, 0, block.STONE)
	time.sleep(0.0.5)

    for x in range(10, 0, -1):
        mc.setBlock(5, x, 0, block.STONE)
	time.sleep(0.0.5)

    for x in range(5, -5, -1):
        mc.setBlock(x, 0, 0, block.STONE)
	time.sleep(0.0.5)

    for x in range(0, 10):
        mc.setBlock(-5, x, 0, block.AIR)
	time.sleep(0.0.5)

    for x in range(-5, 5):
        mc.setBlock(x, 10, 0, block.AIR)
	time.sleep(0.0.5)

    for x in range(10, 0, -1):
        mc.setBlock(5, x, 0, block.AIR)
	time.sleep(0.0.5)

    for x in range(5, -5, -1):
        mc.setBlock(x, 0, 0, block.AIR)
	time.sleep(0.0.5)
