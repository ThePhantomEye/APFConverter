
print('Enter amount of skipped lines:')
skipamount = int(input())

color1 = 1
color2 = 0

data = "APERTURE IMAGE FORMAT (c) 1985\n" + str(skipamount) + "\n"

while True:
    length = 0
    for a in range(94):
        pixel = int(input())
        if pixel == color2:
            # print('same')
            length += 1
        elif pixel == color1:
            color1 ^= 1
            color2 ^= 1
            # print('different')
            break
        else:
            print(data)

            with open("output.apf", "w") as text_file:
                text_file.write(data)

    data += chr(length + 32)
