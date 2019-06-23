from PIL import Image

# Open an image
im = Image.open("test_image.png")

# Get the size of the image
width, height = im.size
print(width, height)

#Rotate the image x degrees without changing its size
x = 90
im = im.rotate(x,expand=False) 
width, height = im.size
print(width, height)

#Rotate the image x degrees changing its size
x = 90
im = im.rotate(x,expand=True)
width, height = im.size
print(width, height)

#Resize the image to a new size in integers
img = img.resize((125, 240)) 

#Transpose/Mirror the image
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img = img.transpose(Image.FLIP_TOP_BOTTOM)

#Create a thumbnail of the image (keeping the size ratio)
img.thumbnail((50, 50)) 
img.show()
