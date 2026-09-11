from PIL import Image

im=Image.open("images.jpg")
#im.show()
alpha = 0.25
for i in range(im.size[0]):
    for j in range(im.size[1]//2, im.size[1]):
        r, g, b = im.getpixel((i,j))
        im.putpixel((i,j),(int(138*(1-alpha)+r*alpha), int(16*(1-alpha)+g*alpha), int(30*(1-alpha)+b*alpha)))

im.save("images_modified.jpg")
im.show()
    
    