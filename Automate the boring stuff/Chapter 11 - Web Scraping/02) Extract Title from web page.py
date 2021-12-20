import requests  # Allows us to request web pages form the internet
import bs4  # Allows us to parse web pages


"""Example 2 - Using Beautiful Soup to extract the header from a web page"""

page = requests.get("https://codedamn.com")  # Access the given URL
page.raise_for_status()  # Check the page is found, halt if not
soup = bs4.BeautifulSoup(page.content, "html.parser")  # Uses Beautiful Soup to parse the HTML
title = soup.title.text

print(soup)
print(title)