from PIL import Image

im=Image.open("images.jpg")
#im.show()

for i in range(im.size[0]):
    im.putpixel((i,430),(250,10,10))

im.save("images_modified.jpg")
im.show()
    
    