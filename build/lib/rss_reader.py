"""This is a main file of project."""

# Import Statements
import argparse
import bs4
import requests
import json
import logging


def main():
    """ This is a main function for our project and contains all logic"""
    parser = argparse.ArgumentParser(prog='RSS-Reader',
                                     usage='rss_reader.py [-h] [--version] [--json] [--verbose] '
                                           '[--limit LIMIT]\n\t\t      source',
                                     description='Pure Python command-line RSS reader.',
                                     epilog='This project was created by Elyorbek Hamroyev')
    parser.add_argument('source', type=str, help='RSS URL')

    parser.add_argument('--version', help='Print version info', action='version', version='%(prog)s version is 2.0')
    parser.add_argument('--json', help='Print result as JSON in stdout', action='store_true')
    parser.add_argument('--verbose', help='Outputs verbose status messages', action='store_true')
    parser.add_argument('--limit', help='Limit news topics if this parameter provided')

    # Parsing arguments and extracting attributes of Namespace
    args = parser.parse_args()
    print(args)
    limit = args.limit
    js = args.json
    verb = args.verbose

    # Requesting webpage xml source and creating beautifulSoup object
    url = requests.get(args.source)
    soup = bs4.BeautifulSoup(url.content, 'lxml')
    entries = soup.find_all('entry')

    # --limit option specified
    if limit is not None:
        limit = int(args.limit)
        entries = entries[:limit]
    # --json option specified
    if js:
        my_dict = {}
        for i, en in enumerate(entries):
            inner_dict = {'title': en.title.text, 'link': en.link.get('href'), 'date': en.updated.text,
                          'summary': en.summary.text}
            my_dict[i] = inner_dict
        print(json.dumps(my_dict, indent=2))

    # --verbose option specified
    if verb:
        logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG,
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.warning(args.source + ' was entered by user')

    # Printing rss-feeds into cmd with usual format when --json flag is not specified
    if not js:
        for e in entries:
            title = e.title.text
            link = e.link.get('href')
            date = e.updated.text
            summary = e.summary.text
            print(f"Title : {title} \n\n Link : {link} \n\n Date : "
                  f"{date} \n\n Summary : {summary}\n\n-----------------")


if __name__ == "__main__":
    main()
