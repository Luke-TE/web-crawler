import requests
import regex as re
from ordered_set import OrderedSet
from bs4 import BeautifulSoup


def crawl_from_base(base_link, num_of_links):
    links = OrderedSet()
    link_index = 0

    while len(links) < num_of_links:
        # Get website data and setup parser
        html_data = requests.get(base_link)
        html_parser = BeautifulSoup(html_data.text, 'html.parser')

        # Get <a> tags
        a_tags = html_parser.find_all('a')

        # Get href links that start with "http"
        for a_tag in a_tags:
            if len(links) >= num_of_links:
                return links
            elif a_tag.get('href', '') != '' and re.search("^http", a_tag['href']):
                links.add(a_tag['href'])

        # Update index to check next page
        link_index += 1
        base_link = links[link_index]

    return links


def print_links(links):
    print("\n".join(links))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Gets URLs using input as starting URL.")
    parser.add_argument('starting_link', type=str)  # URL argument
    parser.add_argument('num_of_links', type=int)  # Max num of links argument
    args = parser.parse_args()

    # Scrape links
    scraped_links = crawl_from_base(args.starting_link, args.num_of_links)

    # Print links
    print_links(scraped_links)
