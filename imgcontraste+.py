from PIL import Image
import random
img = Image.open("avantages-quil-y-a-a-grandir-dans-un-petit-village.jpg")
pixels = img.load()
nb=int(input())
for i in range(img.width):
    for j in range(img.height):
        r, g, b = pixels[i, j]
        some=random.randint(-nb, nb)
        r +=some
        b +=some
        g +=some

        if r > 255:
            r = 255
        if g > 255:
            g = 255
        if b > 255:
            a = 255
        if r < 0:
            r=0
        if g < 0:
            g=0
        if b < 0:
            b=0
        pixels[i, j]=(r, g, b)
img.show()   
       
        
