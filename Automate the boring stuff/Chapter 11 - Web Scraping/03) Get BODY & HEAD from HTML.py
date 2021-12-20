import bs4
import requests

# Make a request
page = requests.get("https://codedamn.com")  # Grab the URL
page.raise_for_status()  # Check we got the URL ok - hault if not

soup = bs4.BeautifulSoup(page.content, "html.parser")  # Parse the page content as HTML

# Extract title of page
page_title = soup.title.text

# Extract body of page
page_body = soup.body

# Extract head of page
page_head = soup.head

# Print the result
print(page_body, page_head)

