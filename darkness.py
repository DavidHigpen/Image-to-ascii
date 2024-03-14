from PIL import Image, ImageDraw, ImageFont

def getDict():
    white = (255, 255, 255)

    chars = [chr(i) for i in range(32, 127)]
    font = ImageFont.truetype("./Consolas.ttf", size=140)

    charsPercents = {}

    for char in chars:
        image = Image.new("RGB", (80, 130), white)
        draw = ImageDraw.Draw(image)
        draw.text((-5,-6), char, fill="black", font=font)
        totalBlack = 0
        for i in range(image.width):
            for j in range(image.height):
                if image.getpixel((i, j)) == (0, 0, 0):
                    totalBlack += 1
        charsPercents[char] = totalBlack / image.width / image.height

    ratio = 1 / max(charsPercents.values())

    for pair in charsPercents:
        charsPercents[pair] *= ratio
        
    charsPercents = dict(sorted(charsPercents.items(), key=lambda item: item[1]))

    charsPercents = {v:k for k, v in charsPercents.items()}


    # for pair in charsPercents:
    #     print(f'{pair} {charsPercents[pair]}')
    return charsPercents