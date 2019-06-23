from PIL import Image, ImageOps

# Open an image 
im = Image.open("test_image_2.png")
im.load()

# Get its attributes
imageSize = im.size
imageBox = im.getbbox()
imageComponents = im.split()

# Check the components of the image to see if it is RGB
if len(imageComponents) == 4:
	# Make a RGB version
	rgbImage = Image.new("RGB", imageSize, (0,0,0))
	rgbImage.paste(im, mask=imageComponents[3])
	croppedBox = rgbImage.getbbox()
# In case it is already a RGB image
else: 
	croppedBox = im.getbbox()

# Get the dimensions I wanna change (4-tuple with the left, upper, right, and lower pixel)
croppedBox = croppedBox[:1] + (0,) + croppedBox[2:]

# Crop and save the new image
cropped=im.crop(croppedBox)
cropped.save("cropped_image.png") 
