import argparse
import os
import datetime
from urllib.parse import urlparse
from src.crawler import WebCrawler


def main():
    parser = argparse.ArgumentParser(description="Webcrawler")
    parser.add_argument("--url", help="URL to scrape", metavar="url", required=True)
    parser.add_argument(
        "--depth",
        help="Depth to scrape",
        metavar="depth",
        required=False,
        default=1,
        type=int,
    )
    parser.add_argument(
        "--filter",
        help="Filter to apply",
        metavar="filter",
        required=False,
        default=None,
    )
    parser.add_argument(
        "--output",
        help="The path of the file to write the results to",
        metavar="file path",
        required=False,
        default=None,
    )
    parser.add_argument(
        "--verbose",
        help="Print verbose output",
        metavar="verbose",
        required=False,
        default=False,
    )

    args = parser.parse_args()

    url = args.url
    depth = args.depth
    file_type = args.filter
    output_path = args.output
    verbose = args.verbose

    if not output_path:
        # Ensure the 'output' directory exists
        if not os.path.exists("output"):
            os.makedirs("output")

        # Create a filename based on the URL and current timestamp
        parsed_url = urlparse(url)
        url_path = parsed_url.netloc + parsed_url.path
        url_path = url_path.replace("/", "_").replace(":", "_")
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        output_path = f"output/{url_path}_{timestamp}.txt"

    crawler = WebCrawler(url, depth, file_type, verbose, output_path)
    crawler.crawl()


if __name__ == "__main__":
    main()
