import math
from PIL import Image

def encodeImage(image_path, text_path):
    image = Image.open(image_path)
    image = image.convert("1")
    block_height = 3
    """
    while True:
        try:
            print("Enter the amount of lines to skip:")
            block_height = int(input())
            if 10 > block_height > 0:
                break
            else:
                print("Please enter a value between 1 and 9")
        except ValueError:
            print("Please enter a valid integer")
    """
    width = image.size[0]
    height = image.size[1]
    block_count = math.ceil(height / block_height)

    colour = False
    cursor_color = False
    cursor_value = 0

    x = 0
    min_char = " "
    max_char = "~"

    output = "APERTURE IMAGE FORMAT (c) 1985\n" + str(block_height) + "\n"

    for block_y in range(block_height):
        for block_index in range(block_count):
            for i in range(width):
                y = block_index * block_height + block_y
                if y >= height:
                    break
                if x == 0 and y == 0:
                    pass
                if x >= width:
                    x = 0

                # if x == 0 and block_index == 6:
                #     print("now")

                # print(image.getpixel((x, y)))
                # print(image.getpixel((x, y)) / 255)

                # print(x, height - y + 1)
                color = bool(image.getpixel((x, height - y - 1)) / 255)
                # if colour != color:
                #     cursor_value += 1
                #
                # colour = color
                if color == cursor_color and cursor_value < ord(max_char) - ord(min_char):
                    cursor_value += 1
                    x += 1
                else:
                    output += chr(ord(min_char) + cursor_value)
                    cursor_color = not cursor_color
                    cursor_value = 0

    image.close()

    output += chr(ord(min_char) + cursor_value)

    text_file = open(text_path, "w")
    text_file.write(output)
    text_file.close()

"""
def decodeText(text_path, image_path):
    text_file = open(text_path, "r")
    text = text_file.read()
    text_file.close()

    header = text.split("\n")[0].split(";")

    content = text.split("\n")[1]

    width = int(header[0])
    height = int(header[1])
    block_height = int(header[2])
    min_char = ord(header[3])
    max_char = ord(header[4])

    cursor_color = False

    pixel_index = 0

    image = Image.new("1", (width, height))

    for char in content:
        for count in range(ord(char) - min_char + 1):
            x = pixel_index % width
#           y = int((pixel_index - x) / width)  # to fix
            y = (pixel_index - x) // width
            if pixel_index >= width * height:
                break
 
            image.putpixel((x, y), cursor_color * 255)

            pixel_index += 1
        cursor_color = not cursor_color

    image.save(image_path)
    image.close()
"""

encodeImage("test1.png", "test14.apf")
# decodeText("test2.txt", "test_bis.png")

print(
    "\033[31;1m\033[38:5:4mOK\033[0m")  # Prints "OK" in bold blue font (see https://en.wikipedia.org/wiki/ANSI_escape_code)



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