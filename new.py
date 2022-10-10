from PIL import Image
import math

BLOCK_HEIGHT = 3
START_CHAR = ord(" ")
END_CHAR = ord("~")


def encodeImage(image_path, text_path):
    image = Image.open(image_path)
    image = image.convert("1")

    width = image.size[0]
    height = image.size[1]
    block_count = math.ceil(height / BLOCK_HEIGHT)

    cursor_color = False
    cursor_value = 0

    output = f"{width};{height};{BLOCK_HEIGHT};{chr(START_CHAR)};{chr(END_CHAR)}\n"

    for block_y in range(BLOCK_HEIGHT):
        for block_index in range(block_count):
            for x in range(width):
                y = block_index * BLOCK_HEIGHT + block_y
                if y >= height:
                    break
                if x == 0 and y == 0:
                    pass

                color = bool(image.getpixel((x, y)) / 255)

                if color == cursor_color and cursor_value < END_CHAR - START_CHAR:
                    cursor_value += 1
                else:
                    output += chr(START_CHAR + cursor_value)
                    cursor_color = not cursor_color
                    cursor_value = 0

    image.close()

    output += chr(START_CHAR + cursor_value)

    text_file = open(text_path, "w")
    text_file.write(output)
    text_file.close()


def decodeText(text_path, image_path):
    text_file = open(text_path, "r")
    text = text_file.read()
    text_file.close()

    header = text.split("\n")[0].split(";")

    content = text.split("\n")[1]

    width = int(header[0])
    height = int(header[1])
    block_height = int(header[2])
    start_char = ord(header[3])
    end_char = ord(header[4])

    cursor_color = False

    pixel_index = 0

    image = Image.new("1", (width, height))

    for char in content:
        for count in range(ord(char) - start_char + 1):
            x = pixel_index % width
            y = int((pixel_index - x) / width)  # to fix

            if pixel_index >= width * height:
                break

            image.putpixel((x, y), cursor_color * 255)

            pixel_index += 1
        cursor_color = not cursor_color

    image.save(image_path)
    image.close()


encodeImage("test1.png", "test.txt")
# decodeText("test.txt", "test_bis.png")

print("\033[31;1m\033[38:5:4mOK\033[0m")  # Prints "OK" in bold blue font (see https://en.wikipedia.org/wiki/ANSI_escape_code)
