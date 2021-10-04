from PIL import Image
import xlsxwriter

def image_to_pixel_art(image_path, number_of_colors, number_of_pixels, canvas_max_size):

	#Reducing the canvas max size due to some limits/bugs with the xlswriter functions
	canvas_max_size = canvas_max_size - 100

	#Check to a maximun number of pixels to avoid crashing excel
	if number_of_pixels > 256:
		print('The max number of pixels is 256')
		return

	#Find the maximun cell size to be used
	cell_size = (round(canvas_max_size / number_of_pixels))

	#Since the minimun size for a Excel cell is 1px, we round our size to 1 and get the proportion of the rounding
	if cell_size == 0:
		cell_size = 1
	elif cell_size < 1:
		cell_size = 1
	print('Cell size:',cell_size)

	#We get the size of the input image
	img=Image.open(image_path)
	width, height  = img.size

	#Now we resize the width and heigth with our number of pixels to keep the proportion
	if height > width:
		height_f = number_of_pixels
		img_proportion = number_of_pixels/height
		width_f = int(round(width * img_proportion)) 
		print('h,w,prop:',height_f, width_f, img_proportion)
	elif height < width:
		width_f = number_of_pixels
		img_proportion = number_of_pixels/width
		height_f = int(round(height * img_proportion)) 
		print('h,w,prop:',height_f, width_f, img_proportion)
	elif height == width:
		height_f = number_of_pixels
		width_f = number_of_pixels
		print('h,w,prop:',height_f, width_f,img_proportion)

	#Image transformation
	pixel_image = img.quantize(number_of_colors)
	rgb_im = pixel_image.convert('RGB')
	small_img=rgb_im.resize((width_f,height_f),Image.BILINEAR)

	final_image=small_img.resize((width,height),Image.NEAREST)
	final_image.save(image_path.split('.')[0] + '_pixel_' + str(number_of_pixels) + '.' + image_path.split('.')[1]) 

	#Create our .xls file with one sheet
	workbook = xlsxwriter.Workbook(image_path.split('.')[0] + '_pixel_'+ str(number_of_pixels) +'.xlsx')
	worksheet = workbook.add_worksheet('Image')
	worksheet_2 = workbook.add_worksheet('Color Map')

	#Changing the size of our columns 
	worksheet.set_column_pixels(0, width_f, cell_size)

	#Getting the pixel RGB values (colors) of our image
	pixel_values = list(small_img.getdata())

	#Iterating throug the size of our image to draw it
	for x in range(height_f):
		#Changing the size of our rows (also to 10 px)
		worksheet.set_row_pixels(x, cell_size)
		for i in range(width_f):
			#Using a mask to get the HEX value of our RGB since thats the one that Excel uses
			color = '#%02x%02x%02x' % pixel_values[width_f*x+i]
			#Filling the background of our cell
			cell_format = workbook.add_format({'bold':True, 'align':'center', 'bg_color':color})
			worksheet.write(x, i, '', cell_format)
			worksheet_2.write(x, i, str(color))
	workbook.close()
