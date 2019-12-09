### Simple web crawler in Python
 
Accepts a single starting URL as its input. 
Downloads the web page available at the input URL and extracts the URLs of other pages (\<a\> tags' href attribute) linked to from the HTML source code. 
   
Downloads each of those URLs in turn to find even more URLs, and then download those, and so on. 

Stops after 100 unique URLs have been discovered and prints them (one URL per line) as its output.

To install the environment, run ```pipenv install```.

To activate the environment, run ```pipenv shell```.

To run the script, run ```python src/crawler.py "https://news.ycombinator.com" 100``` 