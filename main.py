from mido import MidiFile
from PIL import Image
from math import floor, sqrt, sin
import os

for filename in os.listdir('midi'):
    if filename.endswith('.mid'):
        mid = MidiFile('midi/' + filename)

        messages = []
        notes = []
        
        #the only message types that I want to represent
        allowed = ['note_on']

        #goes through all messages in file
        for msg in mid:
            if msg.type in allowed:
                messages.append(msg)
                notes.append(msg.note)

        #get the length and width of box
        size = int(floor(sqrt(len(messages))))

        im = Image.new("RGB", (size, size), "white")

        color = []

        note_max = max(notes)

        for note in messages:
            green = min(sum(note.bytes())/1.5, 255)
            red = note.bytes()[1] + note.bytes()[2]
            blue = max(abs((note.note/note_max)*255-255), (note.note/note_max)*255)
            color.append([int(red), int(green), int(blue)])

        #go through all spaces in an image 
        for i in range(size):
           for j in range(size):
               curr = color[i * size + j]
               im.putpixel((i, j), tuple(curr))

        im = im.resize((1000, 1000), resample = Image.Dither.NONE)

        im.save('images/%s' % filename.replace('.mid', '.png'), 'PNG')
