from PIL import Image

#creates an array of rgb values that are contained in a tuple.
def create_color(notes, messages):
    color = []

    note_max = max(notes) 

    for note in messages:
        green = min(sum(note.bytes())/1.5, 255)
        red = note.bytes()[1] + note.bytes()[2]
        blue = max(abs((note.note/note_max)*255-255), (note.note/note_max)*255)
        color.append([int(red), int(green), int(blue)])

    return color

#creates the images in the image folder
def create_images(im, color, size, filename):
    #go through all spaces in an image 
    for i in range(size):
       for j in range(size):
            curr = color[i * size + j]
            im.putpixel((i, j), tuple(curr))

    im = im.resize((1000, 1000), resample = Image.Dither.NONE)

    im.save('images/%s' % filename.replace('.mid', '.png'), 'PNG')

#attempts to sort the pixels into a landscape design
def pixel_sort(color):
    #copy array
    order = color[:]

    #order = blue over green ratio * sum of blue green
    for item in range(0, len(order)):
        order[item] = (order[item][1] - order[item][2]) * sum(order[item][1:])

    #parellel sort
    res = sorted(zip(order, color))

    return res

#creates theimages in the landscapes folder
def create_landscapes(im_l, res, filename, size):
    for i in range(size):
        for j in range(size):
            curr = res[i * size + j][1]
            im_l.putpixel((j, i), tuple(curr))

    im_l = im_l.resize((1000, 1000), resample = Image.Dither.NONE)

    im_l.save('landscapes/%s' % filename.replace('.mid', '.png'), 'PNG')
