import bs4  # Needed for parsing the web page
import logging  # For error logging
import requests  # Needed for getting a webpage

# Configure Error Logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s-  %(message)s')
logging.debug('Start of program')

# Make a request
page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")

# Check it is ok
page.raise_for_status()

# Parse the HTML
soup = bs4.BeautifulSoup(page.content, "html.parser")

# Create the top items as an empty list
top_items = []

# Extract & store in top_items according to instructions on the left products = soup.select("div.thumbnail")
products = soup.select("div.thumbnail")

for elem in products:  # Loop through each item in the list.
    title = elem.select("h4 > a.title")[0].text
    # The "h4 > a" bit says, find an <a> tag whose parent is the <h4> tag
    # The .title bit then says, find the TITLE class that is under the a element
    # As there will only be 1 result, the title we want we can then use [0] to extract the value
    # And .text grabs just the text.

    review_label = elem.select("div.ratings")[0].text
    # This will find the RATINGS class within the DIV element

    # Now we make a dictionary to store the results
    # .strip() removes the whitespace characters

    info = {
        "title": title.strip(),
        "review": review_label.strip()
    }

    top_items.append(info)  # Add our dictionary as an entry to the list.

    print(top_items)




