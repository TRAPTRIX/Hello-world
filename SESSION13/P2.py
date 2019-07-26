import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from pygame import mixer
mixer.init()
mixer.music.load('crowd-cheering.mp3')
mixer.music.play()

while True:
    input("Press any key to stop? ")
    break
