#from PIL import Image
import math


HEIGHT = 200
WIDTH = 320
PIXEL_COUNT = WIDTH * HEIGHT

BLOCK_HEIGHT = 5
BLOCK_COUNT = math.ceil(HEIGHT/BLOCK_HEIGHT)

print(PIXEL_COUNT)
print(BLOCK_HEIGHT)
print(BLOCK_COUNT)

"""
for i in range():
    for y in range():
        for x in range(WIDTH):
            image_y = HEIGHT - i * y
            pixel_index = ... + x
            if pixel_index > PIXEL_NUMBER :
                break;

            pixels[]
"""




"""
from PIL import Image

# print('Enter amount of skipped lines:')
# skipamount = int(input())
#
# print('Enter input file name')
# inputfile = input()

skipamount = 3
inputfile = "test1.png"

color1 = (255, 255, 255, 255)
color2 = (0, 0, 0, 255)

data = "APERTURE IMAGE FORMAT (c) 1985\n" + str(skipamount) + "\n"

im = Image.open(inputfile, "r")

x = 0   #Should be 0
y = 199 #Should be 199

run = 0
coordinate = x, y
print(im.getpixel(coordinate))
while x < 320 and run <= skipamount:
    length = 0
    loop = 0
    while loop <= 93:

        if -1 < x < 320 and run <= skipamount:

            coordinate = x, y
            print(coordinate) # remove
            pixel = im.getpixel(coordinate)


            if pixel == color2:
                print('same ' + str(x) + str(coordinate)) # remove
                length += 1
                x += 1
                loop += 1

            elif pixel == color1:
                print("TEST")
                color1, color2 = color2, color1
                print('different ' + str(x) + str(coordinate)) # remove
                print(chr(length + 32)) # remove
                break
            else:
                print('ERROR')


        elif x < -1:
            print('ERROR')

        elif x >= 320:
            if y >= skipamount:
                y -= skipamount
                x = 0

            else:
                run += 1
                y = 199 - run
                x = 0


        elif run > skipamount:
            print('hi')
            break
    if loop == 93:
        color1, color2 = color2, color1
        loop = 0
        print("number" + str(length + 32))

    data += chr(length + 32)

with open("output.apf", "w") as text_file:
    text_file.write(data)

"""
