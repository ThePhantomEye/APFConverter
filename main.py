import math
from PIL import Image

block_height = 3


def encodeImage(image_path, text_path):
    image = Image.open(image_path)
    image = image.convert("1")

    width = image.size[0]
    height = image.size[1]
    block_count = math.ceil(height / block_height)

    cursor_color = False
    cursor_value = 0

    x = 0
    min_char = " "
    max_char = "~"

    output = "APERTURE IMAGE FORMAT (c) 1985\n" + str(block_height) + "\n"

    for block_y in range(block_height):
        for block_index in range(block_count):
            x = 0
            while x <= width:
                y = block_index * block_height + block_y
                if y >= height:
                    break
                if x == 0 and y == 0:
                    pass
                if x >= width:
                    break
                color = bool(image.getpixel((x, height - y - 1)) / 255)
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


def decodeImage(text_path, image_path):
    text_file = open(text_path, "r")
    text = text_file.read()
    text_file.close()
    content = text.split("\n")[2]
    width = 320
    height = 200
    block_height = int(text.split("\n")[1])
    min_char = " "
    max_char = "~"
    cursor_color = False
    pixel_index = 0
    image = Image.new("1", (width, height))

    for char in content:
        for count in range(ord(char) - ord(min_char) + 1):
            x = pixel_index % width
            y = int((((pixel_index - x) / width) * block_height) % height)  # fix
            if pixel_index >= width * height:
                break

            image.putpixel((x, y), cursor_color * 255)
            pixel_index += 1
        cursor_color = not cursor_color
    image.save(image_path)
    image.close()


def menu():
    print("Select an option:\n  1) encode\n  2) decode\n  3) exit")
    while True:
        option = input()
        if option == '1':  # chosen the encode option

            print("Please the amount of lines to skip:")  # define block_height
            while True:
                try:
                    block_height = int(input())
                    if 10 > block_height > 0:
                        break
                    else:
                        print("Please enter a value between 1 and 9")
                except ValueError:
                    print("Please enter a valid integer")

            while True:
                print("Enter the file name of the input image:")  # define input_file
                input_file = input()
                print("Enter the desired  name of the output file:")  # define output_file
                output_file = input()
                try:
                    encodeImage(input_file, output_file)  # encode image
                    print("\033[31;1m\033[38:5:4mOK\033[0m")
                    break
                except FileNotFoundError:
                    print("could not find " + input_file + ". Please try again.")

        elif option == '2':  # chosen the decode option
            # decodeImage("image_encoded.apf", "image_decoded.png")
            print("\033[31;1m\033[38:5:4mOK\033[0m")
            break
        elif option == '3':  # chosen the exit option
            print("Terminated script.")
            exit()
        else:
            print("\nInvalid choice. \nPlease choose between:\n  1) encode\n  2) decode\n  3) exit")

# menu()
encodeImage("image_original.png", "image_encoded.apf")
decodeImage("image_encoded.apf", "image_decoded.png")