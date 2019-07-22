from PIL import Image, ImageFont, ImageDraw, ImageEnhance, ImageOps
import json

# Set a hex code to find in the json file
hex_value = '6f3c56'
name = ''
code = ''

# Read our json file and find a HEX value
with open('pantone_codes.json') as json_file:
	data = json.load(json_file)
	for pantone in data:
		if data[pantone]['hex'] == hex_value:
			code = pantone
			name = (data[pantone]['name'])
			break

# Set a font to write the code in the card
font = ImageFont.truetype("arial",24)
# Get the size of the text
code_size = font.getsize(code)
# Set button size + 5px height margins
button_size = (200, code_size[1]+10)
# Create an image with the button size and white background
code_img = Image.new('RGB', button_size, 'white')
# Draw the text on the image 10px margins
code_draw = ImageDraw.Draw(code_img)
code_draw.text((10, 5), code, font=font, fill='black')

# Repeat for the name
font = ImageFont.truetype("arial",20)
# You can also set a fixed size to avoid different letters sizes
button_size = (200, 23+10)
name_img = Image.new('RGB', button_size, 'white')
name_draw = ImageDraw.Draw(name_img)
name_draw.text((10, 5), name, font=font, fill='black')

# Create an image with the Pantone color
color_img = Image.new('RGB', (200,200), '#'+hex_value)

# Get the height of our Pantone card
total_height = color_img.size[1] + name_img.size[1]  + code_img.size[1]

# Create the Pantone card
new_im = Image.new('RGB', (200, total_height))
# Paste every part in it
new_im.paste(color_img, (0,0))
new_im.paste(code_img, (0,200))
new_im.paste(name_img, (0,200+code_img.size[1]))
#Draw a black border around
new_im = ImageOps.expand(new_im,border=2,fill='black')

# Show the Pantone card
new_im.show()
