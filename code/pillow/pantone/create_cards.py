from PIL import Image, ImageFont, ImageDraw, ImageEnhance, ImageOps
import json

hex_value = ''
name = ''
code = ''

#find the code and name in our json
with open('pantone_codes.json') as json_file:
	data = json.load(json_file)
	for pantone in data:
		hex_value = data[pantone]['hex'].replace(',','')
		code = pantone
		name = (data[pantone]['name'])
		
		# Build the name and code
		font = ImageFont.truetype("arial",24)
		code_size = font.getsize(code)
		button_size = (200, code_size[1]+10)
		code_img = Image.new('RGB', button_size, 'white')
		code_draw = ImageDraw.Draw(code_img)
		code_draw.text((10, 5), code, font=font, fill='black')

		font = ImageFont.truetype("arial",20)
		text_size = font.getsize(name)
		button_size = (200, 23+10)
		name_img = Image.new('RGB', button_size, 'white')
		name_draw = ImageDraw.Draw(name_img)
		name_draw.text((10, 5), name, font=font, fill='black')
		
		# Draw the color box
		color_img = Image.new('RGB', (200,200), '#'+hex_value)

		# Draw the card image
		total_height = color_img.size[1] + name_img.size[1]  + code_img.size[1]
		new_im = Image.new('RGB', (200, total_height))
		new_im.paste(color_img, (0,0))
		new_im.paste(code_img, (0,200))
		new_im.paste(name_img, (0,200+code_img.size[1]))
		new_im = ImageOps.expand(new_im,border=2,fill='black')

		# Save the image in a folder called cards
		new_im.save('cards/'+name+".jpg", "JPEG")
