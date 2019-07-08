import requests

# Set the SKUs to find and the URL where we will be looking up
products = ['880969943','881212428','15799133','123554']
search_url= "https://www.falabella.com.pe/falabella-pe/search/?Ntt="

for product in products :
	# Make a get call to the URL
	response = requests.get(search_url+product)	
	# Get the html of the website   
	html_text = response.text
	
	# Check if we have a result for our SKU or not
	if html_text.find("Código del producto:"+product) != -1:
	  	print(product,'Published')
	else:
	   	print(product,'Not Published')
