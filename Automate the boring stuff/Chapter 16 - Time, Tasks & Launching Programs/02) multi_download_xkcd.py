#! python3
# multi_download_xkcd.py - Downloads comics from XKCD using multiple threads

import bs4
import os
import requests
import threading

xkcd_url = "https://xkcd.com/"

os.makedirs("xkcd", exist_ok=True)  # Make the folder xkcd - it's ok if the folder already exists.


def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):  # Loop through the url numbers start -> stop.

        # Download the page
        page_url = "{}{}".format(xkcd_url, url_number)  # Build the URL of the specific page
        print("Downloading page{}".format(page_url))  # Tell user what age is being downloaded.

        res = requests.get(page_url)  # Grab the URL

        res.raise_for_status()  # Check it's ok - exit code if URL bad.

        soup = bs4.BeautifulSoup(res.text, "html.parser")  # Parse the text as a beautiful soup object.

        # Find the URL of the comic image

        comic_element = soup.select("#comic.img")

        if not comic_element:
            print("No comic element found!")
        else:
            comic_url = comic_element[0].get("src")  # Get the VALUE of SRC, which is the URL of the comic.

            # Download the image
            print("downloading image {}...".format(comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()

            # Save the image to ./xkcd
            file_path = os.path.join("xkcd", os.path.basename(comic_url))

            with open(file_path, "wb") as image_file:
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)


# Create and start the thread objects

download_threads = []  # A list of the thread objects

for i in range(0, 1400, 100):  # Loops 14 times, making 14 threads
    download_thread = threading.Thread(target=download_xkcd, args=(i, i + 99))  # Call the download ftn.
    download_threads.append(download_thread)  # Add the output of the function to a list?
    download_thread.start()  # Start the thread.

# Wait for all the threads to end.

for download_thread in download_threads:
    """Each of the running threads is in the "download_threads list.
    Here we loop though each of the running threads, calling JOIN on each one
    This will no run the next line of code until the individual thread in question is complete
    So by looping over all of them, we halt the main thread until ALL of the other download threads are done."""
    download_thread.join()

print ("Done")
