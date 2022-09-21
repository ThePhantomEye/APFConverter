from PIL import Image

print('Enter amount of skipped lines:')
skipamount = int(input())

print('Enter input file name')
inputfile = input()

color1 = (255, 255, 255, 255)
color2 = (0, 0, 0, 255)

data = "APERTURE IMAGE FORMAT (c) 1985\n" + str(skipamount) + "\n"

im = Image.open(inputfile, "r")

x = 0  #0
y = 9 #199

coordinate = x, y
print (im.getpixel(coordinate));
while x != 320:
    length = 0
    for a in range(94):
        if x < 320:
            coordinate = x, y
            pixel = im.getpixel(coordinate)
            if pixel == color2:
                print('same ' + str(x) + str(coordinate))
                length += 1
                x += 1
            elif pixel == color1:
                color1, color2 = color2, color1
                print('different ' + str(x) + str(coordinate))
                break
            else:
                print('ERROR')
    data += chr(length + 32)

with open("output.apf", "w") as text_file:
    text_file.write(data)
