import bs4
import requests
import logging

# Configure Error Logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s-  %(message)s')
logging.debug('Start of program')

# Make a request
page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")

# Parse the request

soup = bs4.BeautifulSoup(page.content, "html.parser")

# Create top_items as an empty list
image_data = []

# Extract and store in top_items according to instructions on the left.

images = soup.select("img")  # This will select all elements with the tag <img> & put them in a result set.

print(type(images))

for image in images:  # Loop through each item in the list.
    src = image.get("src")
    alt = image.get("alt")
    image_data.append({"src:": src, "alt": alt})

print(image_data)


