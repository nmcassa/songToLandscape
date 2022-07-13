from mido import MidiFile
from PIL import Image
from math import floor, sqrt, sin
import os

for filename in os.listdir('midi'):
    if filename.endswith('.mid'):
        mid = MidiFile('midi/' + filename)

        notes = []
        times = []

        #the only message types that I want to represent
        allowed = ['note_on']

        #goes through all messages in file
        for msg in mid:
            if msg.type in allowed:
                notes.append(msg)
                times.append(msg.time)

        #get the length and width of box
        size = int(floor(sqrt(len(notes))))

        im = Image.new("RGB", (size, size), "white")

        color = []

        time_max = max(times)

        for note in notes:
            red = int((note.time/time_max)*255)
            green = note.velocity
            blue = note.note

            color.append([int(red), green, blue])

        #go through all spaces in an image 
        for i in range(size):
           for j in range(size):
               curr = color[i * size + j]
               im.putpixel((i, j), tuple(curr))

        im = im.resize((1000, 1000), resample = Image.Dither.NONE)

        im.save('images/%s' % filename.replace('.mid', '.png'), 'PNG')
