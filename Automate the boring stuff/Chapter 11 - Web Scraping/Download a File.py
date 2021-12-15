#! python3
# Function to download a file from a URL that is passed to the function.

import requests  # Needed to download things form the web

def download_file(url):
    local_filename = url.split('/')[-1]

    """ Splits the URL string up via the / delimeter, producing a list of strings
    Each item in this list has an index position, -1 referecnes the LAST item in the list
    So this splits the URL up into a list, grabs the last item on the list and assigns it to our variable
    e.g if the url was https://www.gutenberg.org/cache/epub/66944/pg66944.txt
    then the list of strings would be:
    ['https:', '', 'www.gutenberg.org', 'cache', 'epub', '66944', 'pg66944.txt']
    So the LAST item in the list would be pg6944.txt which is the filename we want"""

    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        """requests.get makes a REQUEST to a webpage and GETS a response back.
        The 'stream = True' parameter says that the response we get back should be downloaded
        We assign the whole thing to the variable 'r'"""

        r.raise_for_status()  # This will halt the code IF the URL we passed is bad.

        with open(local_filename, 'wb') as f:
            """Opens a file, makes it if it does not exist.
            The wb paramenter stands for write binary to maintain the unicode encoding of the text"""

            for chunk in r.iter_content(chunk_size=8192):
                """ The iter_content returns chunks of the file, here we've told it to use chunks of 8192 bytes
                this for loop will then do the same thing for ech chunk that's obtained"""
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)  # Write the chunk to the file.
    return local_filename  # Returns the filename as a string should we wish to use it.

download_file("https://www.gutenberg.org/cache/epub/66944/pg66944.txt")
