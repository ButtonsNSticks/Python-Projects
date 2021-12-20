#! python3
# lucky.py - Opens several Google search results

# Import modules

import bs4
import requests
import sys
import webbrowser

print("Googling...")  # Display text while downloading the Google page

# res = requests.get("https://google.co.uk/search?q=" + " ".join(sys.argv[1:]))
res = requests.get("https://duckduckgo.com/html/")
"""
    Makes a request to get the web page from the URL we pass to it.
    The .join(sys.argv[1:]) will take all of the command line arguments passed the the script
    and join them together with spaces - and this then gets stuck onto the end of our Google URL
"""

res.raise_for_status()  # Check to see if the webpage we asked for is found - stops the code running if not.

# Get the top search result links

soup = bs4.BeautifulSoup(res.text, "html.parser")  # Creates a BS object from the HTML of the URL we requested.
# soup = bs4.BeautifulSoup(res.text,'lxml')

# Open a browser tab for each result

linkelems = soup.select(".result__a")
# linkelems = soup.select('div#main > div > div > div > a')

"""
    The SELECT method will create a list of all text which matches the following CSS selector:  
    .r - Get all elements from CSS class 'r'
    a - And from those, pick just the <a> elements 
"""

numopen = min(5, len(linkelems))

""" The min function returns the lowest item in the list of values passed to it
So here it will set numopen to 5 OR less if fewer than 5 results are found."""

for i in range(numopen):  # Repeats the loop for the same number of times that numopen is equal to.
    webbrowser.open("https://google.co.uk" + linkelems[i].get("href"))
    """ linkelems[i] will give the ith value in the list of items
    the .get("href") part says """

