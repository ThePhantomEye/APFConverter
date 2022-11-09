import math
import sys
import os
from PIL import Image


def encode_image(image_path, apf_path):
    image = Image.open(image_path)
    image = image.convert("1")

    width = image.size[0]
    height = image.size[1]
    block_count = math.ceil(height / block_height)  # calculates the amount of blocks that the image is decided into

    cursor_color = False  # defines the first color to scan for as black
    cursor_value = 0

    min_char = " "
    max_char = "~"

    output = "APERTURE IMAGE FORMAT (c) 1985\n" + str(block_height) + "\n"  # defines output

    for block_y in range(block_height):
        for block_index in range(block_count):
            x = 0
            while x <= width:
                y = block_index * block_height + block_y
                if y >= height:  # skip evaluation of pixel until the cursor has moved back to the first block
                    break
                if x == 0 and y == 0:
                    pass  # skip evaluation of the origin pixel
                if x >= width:
                    break  # skip evaluation of pixel until the cursor has moved to the next line
                color = bool(image.getpixel((x, height - y - 1)) / 255)
                if color == cursor_color and cursor_value < ord(max_char) - ord(min_char):
                    cursor_value += 1  # increases the counter value
                    x += 1
                else:
                    output += chr(ord(min_char) + cursor_value)
                    cursor_color = not cursor_color  # flips the cursor color
                    cursor_value = 0  # resets the counter value

    image.close()

    output += chr(ord(min_char) + cursor_value)  # writes the last character

    text_file = open(apf_path, "w")
    text_file.write(output)
    text_file.close()


def decode_image(apf_path, image_path):
    apf_file = open(apf_path, "r")
    apf_content = apf_file.read()
    apf_file.close()

    block_height = int(apf_content.split("\n")[1])  # gets the block height from the file
    data = apf_content.split("\n")[2]  # gets the image data from the file
    width, height = 320, 200

    cursor_color = False  # defines the first color to print as black
    image = Image.new("1", (width, height))

    x, y = 0, 0
    block_index = 0

    for char in data:
        for i in range(ord(char) - 32):
            if x >= width:
                y += block_height  # move y block_height lines up
                if y >= height:
                    block_index += 1  # increases the vertical height within each block
                    y = block_index

            x %= width  # make sure x doesn't surpass the image width
            image.putpixel((x, height - 1 - y), cursor_color * 255)
            x += 1
        cursor_color = not cursor_color  # flips the cursor color

    image.save(image_path)
    image.close()


def menu():
    print("Select an option:\n  1) encode\n  2) decode\n  3) exit")
    while True:
        option = input()
        if option == '1':  # chosen the encode option

            print("Please the amount of vertical lines to skip:")  # define block_height
            while True:
                try:
                    global block_height
                    block_height = int(input())
                    if 10 > block_height > 0:
                        break
                    else:
                        print("Please enter a value between 1 and 9")
                except ValueError:
                    print("Please enter a valid integer")

            while True:
                print("Enter the file name of the image to encode:")  # define input_file
                input_file = os.path.split(os.path.abspath(sys.argv[0]))[0] + "\\images\\" + input()
                print("Enter the desired name of the output file:")  # define output_file
                output_file = os.path.split(os.path.abspath(sys.argv[0]))[0] + "\\images\\" + input()

                if Image.open(input_file).size != (320, 200):
                    print("The input image is not of required size (320x200).\nPlease try again.\n")
                    break
                try:
                    encode_image(input_file, output_file)  # encode image

                    print("\033[31;1m\033[38:5:4mDone\033[0m")
                    break
                except FileNotFoundError:
                    print("could not find " + input_file + ". Please try again.")
            break

        elif option == '2':  # chosen the decode option

            while True:
                print("Enter the file name of the image to decode:")  # define input_file
                input_file = os.path.split(os.path.abspath(sys.argv[0]))[0] + "\\images\\" + input()
                print("Enter the desired name of the output image:")  # define output_file
                output_file = os.path.split(os.path.abspath(sys.argv[0]))[0] + "\\images\\" + input()
                try:
                    decode_image(input_file, output_file)  # decode image

                    print("\033[31;1m\033[38:5:4mDone\033[0m")
                    break
                except FileNotFoundError:
                    print("could not find " + input_file + ". Please try again.")
            break

        elif option == '3':  # chosen the exit option

            print("Terminated script.")  # baked a cake
            exit()
        else:
            print("\nInvalid choice. \nPlease choose between:\n  1) encode\n  2) decode\n  3) exit")


print("\nAPF Converter\n")
while True:
    menu()  # loads the menu in a loop that will only end if the user decides to exit
