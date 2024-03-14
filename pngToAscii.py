from PIL import Image, ImageOps
from darkness import getDict

        
image = Image.open('monalisa.jpg')
image = ImageOps.grayscale(image=image)


width = min(199, image.width)
height = min((6 * width * image.height) // (image.width * 20), image.height)
# height = min((1090 * 84 * width * image.height) // (image.width * 183 * 925), image.height)
print(width, height)
print(image.width, image.height)

pixelsPerWidth = max(image.width // width, 1)
pixelsPerHeight = max(image.height // height, 1)

chars = getDict()

    
def getChar(ratio):
    for key in chars:
        if ratio <= float(key):
            return chars[key]
    return ' '


for i in range(height):
    for j in range(width):
        averageColor = 0
        for l in range(pixelsPerHeight):
            for k in range(pixelsPerWidth):
                averageColor += image.getpixel((k + j * pixelsPerWidth, l + i * pixelsPerHeight))
        averageColor = averageColor / (pixelsPerHeight * pixelsPerWidth)
        ratio = averageColor / 255
        print(getChar(ratio), end='')
    print()