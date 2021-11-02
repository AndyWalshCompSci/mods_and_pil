'''
Andy Walsh
Sep. 30
'''

import random
from PIL import Image

def get_file():
    global my_image
    try:
        filename = input("please give file name: ")
        my_image = Image.open(filename)
    except:
        print("Please give file name: ")
        get_file()
get_file()
my_image = Image.open("Ford.jpeg")
im.show()


random_int = random.randint(0,10)
print(random_int)
px = my_image.load()
px[9, 0] = (0, 0, 255)

my_image = Image.new(mode="RGB",size=(10,10),color=(0,0,0))


def my_image():
    rows = my_image.size[0]
    cols = my_image.size[1]
    print(rows, cols)


    for i in range(rows):
        start = random.randint(0, rows)
        end = random.randint(0, cols)
        nub = random.randint(1, 5)

        if i % 2 == 0:
            start = 0
        else:
            start = 1

        for j in range (start, cols, 2):
            red = random.randint(0,0)
            green = random.randint(0, 0)
            blue = random.randint(0, 0)
            px[i,j] = (red, green, blue)
    #to get more of one color, type 255 on one of these red, green, blue


    my_image.show()