# Jesus.py

def Jesus(image):
    alpha = 0.25
    for i in range(image.size[0]):
        for j in range(image.size[1]//2, image.size[1]):
            r, g, b = image.getpixel((i,j))
            image.putpixel((i,j),(int(138*(1-alpha)+r*alpha), int(16*(1-alpha)+g*alpha), int(30*(1-alpha)+b*alpha)))
    return image