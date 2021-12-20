import bs4
import requests

# Make a request
page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
page.raise_for_status()  # Check the URL is good.

soup = bs4.BeautifulSoup(page.content, "html.parser")

# Extract the 1st <h1>(....)</h1> text
h1 = soup.select("h1")  # Returns a list of all elements with h1 tag
print(h1)

print(h1[0])  # Print just the 1st one in the list

print(h1[0].text)  # Print just the text without the <h1> tags
