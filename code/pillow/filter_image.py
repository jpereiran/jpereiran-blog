from PIL import Image, ImageFilter, ImageChops, ImageEnhance, ImageOps

# Open an image
im = Image.open("test_image.png")

# Invert colors
invert_image = ImageChops.invert(im)
invert_image.show()

# Grayscale
gray_image = ImageOps.grayscale(im)
gray_image.show()

# Mirroring
mirror_image = ImageOps.mirror(im)
mirror_image.show()

# Enhance the image (brightness, contrast, sharpness) a +/- value
bri_image = ImageEnhance.Brightness(im).enhance(5)
bri_image.show()

con_image = ImageEnhance.Contrast(im).enhance(5)
con_image.show()

shp_image = ImageEnhance.Sharpness(im).enhance(-5)
shp_image.show()

# Apply some filters (blur, contour, sharpen, detail)
blur_image = im.filter(ImageFilter.BLUR)
blur_image.show()

cont_image = im.filter(ImageFilter.CONTOUR)
cont_image.show()

sharp_image = im.filter(ImageFilter.SHARPEN)
sharp_image.show()

det_image = im.filter(ImageFilter.DETAIL)
det_image.show()
