import bs4  # Needed for pasing HTML
import requests
import logging

logging.disable()

# Configure Error Logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s-  %(message)s')
logging.debug('Start of program')

# Set up global variables
all_links = []  # Creates empty list

# Make the request to the web page
page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")

# Parse the HTML to Beautiful Soup
soup = bs4.BeautifulSoup(page.content, "html.parser")

# Extract all of the hyperlinks - these have the <a> tag
hyperlinks = soup.select("a")

logging.debug(hyperlinks)

# Extract the href and text from each item.

for each_hyperlink in hyperlinks:
    href = each_hyperlink.get("href")  # Grabs each element with <href tag - i.e the link
    if href is not None:  # If the HREF is not empty.
        href = href.strip()  # Remove the whitespace
    else:
        href = ""  # If it is empty then set it to "" as opposed to just NoneType

    text = each_hyperlink.text
    if text is not None:  # If the text is not empty
        text = text.strip()  # Remove the whitespace
    else:
        text = ""  # If it is empty then set it to "" as opposed to just NoneType

    all_links.append({"href": href, "text": text})

print(all_links)
