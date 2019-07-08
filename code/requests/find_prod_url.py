import requests
import re

products = ['880969943','880602606','15799133','123554']
search_url= "https://www.falabella.com.pe/falabella-pe/search/?Ntt="

#check for skus
for product in products :
	# Make a head call to the URL
	response = requests.head(search_url+product)

	# We can check the status code to see if we ran into a problem
	if response.status_code != 302:
		print('Error')
		continue

	# Get the final URL shown by the browser and remove a part of it   
	url = response.headers['location'].replace("product/","")
	
	# Check if we have a result for our SKU or not
	if url.find("prod") != -1:
		# Find the code with the help of a regular expression
		group = re.search('prod(.+?)/', url).group(0).replace("/","")
		print("Group", group, product)
	else:
		print("Not in group", product, product)
