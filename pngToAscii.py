from PIL import Image, ImageOps
from darkness import getDict

        
image = Image.open('monalisa.jpg')
image = ImageOps.grayscale(image=image)

#char ratio: width, height = 183, 110 chars = 555, 993 pixels
#each char is about a 2:5 ratio in the vscode terminal

width = min(300, image.width)
height = min((2 * width * image.height) // (image.width * 5), image.height)

print(f'{image.width} {image.height}  Ratio: {image.width / image.height}')
print(f'{width}  {height}  Ratio: {width/height}')

chars = getDict()

    
def getChar(ratio):
    for key in chars:
        if ratio <= float(key):
            return chars[key]
    return ' '


for i in range(height):
    for j in range(width):
        averageColor = 0
        pixels = 0
        for k in range(int(i * image.height / height), int((i + 1) * image.height / height)):
            for l in range(int(j * image.width / width), int((j + 1) * image.width / width)):
                averageColor += image.getpixel((l, k))
                pixels += 1
        averageColor = averageColor / pixels
        ratio = averageColor / 255
        print(getChar(ratio), end='')
    print()