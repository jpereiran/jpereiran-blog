import requests

# Set the SKUs to find and the URL where we will be looking up
products = ['880969943','881212428','15799133','123554']
search_url= "https://www.falabella.com.pe/falabella-pe/search/?Ntt="

for product in products :
	# Make a head call to the URL
	response = requests.head(search_url+product)	
	# Get the final URL shown by the browser   
	url = response.headers['location']
	
	# Check if we have a result for our SKU or not
	if url.find("noSearchResult") != -1:
	  	print(product,'Not Published')
	else:
	   	print(product,'Published')
