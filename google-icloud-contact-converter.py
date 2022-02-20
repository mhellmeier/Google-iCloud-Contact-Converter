# Google iCloud Contact Converter
#
# Author: Malte Hellmeier
# License: MIT License
# Python Version: 3.X
# GitHub Repository: https://github.com/mhellmeier/Google-iCloud-Contact-Converter

import base64
import re
import requests

AREA_CODE = '+49'
contacts_filename = 'contact-example_google-export'  # without file extension (should be .vcf)

# Read contacts file
with open('data/' + contacts_filename + '.vcf', 'r') as google_file:
    google_data = google_file.readlines()

for i in range(len(google_data)):
    # Remove line breaks
    if google_data[i][0] == ' ':
        google_data[i-1] = google_data[i-1] + google_data[i]
        google_data[i] = ''

# Replacements
google_data = [line.replace('\n ', '') for line in google_data]
google_data = [line.replace('\\:', ':') for line in google_data]

# Convert 0 to local area code
google_data = [line.replace('TEL;TYPE=HOME:0', 'TEL;TYPE=HOME:' + AREA_CODE) for line in google_data]
google_data = [line.replace('TEL;TYPE=CELL:0', 'TEL;TYPE=CELL:' + AREA_CODE) for line in google_data]
google_data = [line.replace('TEL;TYPE=WORK:0', 'TEL;TYPE=WORK:' + AREA_CODE) for line in google_data]

for i in range(len(google_data)):
    # Reformat birthdays without a year
    if google_data[i].startswith('BDAY:--'):
        birthday = re.findall(r'BDAY:--(.*?)\n', google_data[i])[0]
        birthday = birthday[:2] + '-' + birthday[2:]
        google_data[i] = 'BDAY;X-APPLE-OMIT-YEAR=1604:1604-' + str(birthday) + '\n'

    # Reformat birthdays with a year
    if google_data[i].startswith('BDAY:'):
        birthday = re.findall(r'BDAY:(.*?)\n', google_data[i])[0]
        birthday = birthday[:4] + '-' + birthday[4:6] + '-' + birthday[6:]
        google_data[i] = 'BDAY;VALUE=date:' + str(birthday) + '\n'

    # Replace picture URL with Base64 encoded image
    if google_data[i].startswith('PHOTO:http'):
        picture_url = re.findall(r'PHOTO:(.*?)\n', google_data[i])[0]
        picture_base64 = base64.b64encode(requests.get(picture_url).content).decode('utf-8')
        google_data[i] = 'PHOTO;ENCODING=b;TYPE=JPEG:' + str(picture_base64)


# Write export file
with open('data/' + contacts_filename + '_converted.vcf', 'w') as converted:
    for item in google_data:
        converted.write(item)

# Print out
#print(google_data)
