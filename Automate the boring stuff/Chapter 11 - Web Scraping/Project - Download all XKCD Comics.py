#! python3
# downloadxkcd.py - Downloads every XKCD comic

import bs4
import requests
import os

url = "http://xkcd.com"  # The URL we are going to start at

os.makedirs("xkcd", exist_ok=True)
# Makes a directory to store the comics in, the exist_ok=True flag tells python not to flag an error
# if the directory already exists.

while not url.endswith("#"):  # Provided the URL does not end with # then...
    # Download the page
    print("Downloading page %s..." % url)
    page = requests.get(url)  # Request the HTML page.
    page.raise_for_status()  # Check the request is ok
    soup = bs4.BeautifulSoup(page.text, "html.parser")  # Grab the HTML of the page and return the text.

    # Todo: Find the URL of the comic image
    comic_elem = soup.select("#comic img")
    # Finds all the elements named <img> WITHIN an element with id attribute "comic"

    if not comic_elem:  # If the soup list is empty
        print("Could not find comic image")

    else:
        comic_url = "https:" + comic_elem[0].get("src")  # Grab the value of SRC, which is the URL of the comic.

    # Download the comic image
        print("Downloading image %s..." % comic_url)
        res = requests.get(comic_url)  # Get the Comic image
        res.raise_for_status()  # Check it is ok

        # Save the image in the XKCD dir we made
        with open(os.path.join("xkcd", os.path.basename(comic_url)), 'wb') as image_file:
            for chunk in res.iter_content(chunk_size=8192):
                image_file.write(chunk)

    # Todo: Get the the Prev button's URL
    prev_link = soup.select("a[rel='prev']")[0]
    url = "http://xkcd.com" + prev_link.get("href")

print("Done")
