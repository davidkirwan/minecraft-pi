# David Kirwan https://github.com/davidkirwan/minecraft-pi
#
# Tutorial 1
#
# Print out 'Hello World!' to the Chat Window

import minecraft

# Create the minecraft object
mc = minecraft.Minecraft.create()

# Prints Hello World! to the Chat Window
mc.postToChat("Hello World!")
