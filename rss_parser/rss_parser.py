from logging import basicConfig, warning

from bs4 import BeautifulSoup
from requests import get
import colorise

from argument_parser.argument_parser import arg_parser
from pdf_saver.pdf_converter import pdf_convert
from html_saver.html_converter import html_convert
from json_converter.json_converter import json_converter
from news_cache.create_cache import create_cache
from helpers import print_feeds


def main():
    """ This is a main function for our project and contains all logic"""
    # Will return args flags extracted dictionary
    args = arg_parser()

    # Requesting webpage xml source and creating beautifulSoup object
    # When requesting we try to cache request using requests-cache package
    try:
        response = get(args['source'])

        soup = BeautifulSoup(response.content, 'lxml')
        entries = soup.find_all('entry')

        # --limit option specified
        if args['limit'] is not None:
            limit = int(args['limit'])
            entries = entries[:limit]

        # Prints rss-feeds with --dates specified dates
        filtered_query = None
        if args['date_attr']:
            filtered_query = create_cache(entries, args['date_attr'])

        # --verbose option specified
        if args['verbose_attr']:
            basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            warning('is when this event was logged.')

        # --json option specified and converts news to json format
        json_results = {}
        if args['json_attr']:
            json_results = json_converter(entries)

        # --colorize option specified
        if args['colorize']:
            try:
                colorise.set_color(fg=args['colorize'])
            except Exception as exc:
                print(exc)

        # Printing rss-feeds into cmd with usual format in usual mode
        print_feeds(entries, args['json_attr'], json_results, args['date_attr'], filtered_query)

        # --to-pdf option is specified
        if args['to_pdf_attr']:
            pdf_convert(entries, args['to_pdf_attr'])

        # --to-html option is specified
        if args['to_html_attr']:
            html_convert(entries, args['to_html_attr'])

    except Exception as exc:
        print('There was a problem: %s' % exc)


if __name__ == "__main__":
    main()
