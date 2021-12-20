import bs4  # Needed to parse a web page
import requests  # Needed to get a webpage

# Set global variables
all_h1_tags = []  # Makes an empty list.
seventh_p_text = ""  # Make empty string

# Make a request
page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")

# Check it's ok
page.raise_for_status()

# Parse the webpage as HTML using BS
soup = bs4.BeautifulSoup(page.content, "html.parser")

"""Grab all the <h1> tags from the HTML"""

all_h1_tag_list = soup.select("h1")
# print(all_h1_tags)

for tag in range(len(all_h1_tag_list)):
    all_h1_tags.append(all_h1_tag_list[tag].text)

# print(all_h1_tags)  # Uncomment to print out the list of h1 tags

""" Grab all the 'p' elements"""

all_p_elements = soup.select("p")
seventh_p_text = all_p_elements[6].text

print(seventh_p_text)
