from mido import MidiFile
from PIL import Image
from math import floor, sqrt
import os
import methods

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
        im_l = Image.new("RGB", (size, size), "white")

        color = methods.create_color(notes, messages)

        methods.create_images(im, color, size, filename)

        res = methods.pixel_sort(color)

        methods.create_landscapes(im_l, res, filename, size)
