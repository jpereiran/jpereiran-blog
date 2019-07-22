import json

# Set a hex code to find in the json file
hex_value = '676168'
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

# Show the code and name of the color
print(code)
print(name)
