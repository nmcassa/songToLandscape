from mido import MidiFile
from PIL import Image
from math import floor, sqrt, sin

file = 'Backstreet Boys - I Want It That Way.mid'

#open file
mid = MidiFile('midi/' + file)

notes = []

#the only message types that I want to represent
allowed = ['control_change', 'note_on', 'pitchwheel']

#goes through all messages in file
for msg in mid:
    if msg.type in allowed:
        notes.append(msg.bytes())

#get the length and width of box
size = int(floor(sqrt(len(notes))))

im = Image.new("RGB", (size, size), "white")

#go through all spaces in an image 
for i in range(size):
   for j in range(size):
       note = notes[i * size + j]
       im.putpixel((i, j), tuple(note))

im = im.resize((1000, 1000), resample = Image.Dither.NONE)

im.save('images/%s' % file.replace('.mid', '.png'), 'PNG')
