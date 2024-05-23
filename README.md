# webCrawler
This is a simple web crawler written in Python. It is a command line tool that can be used to crawl web sites. The tool supports crawling web sites with depth and filter features. The results of the crawl can be written to a file and verbose output can be enabled to see the progress of the crawl.

## Installation

To install the web crawler, 

1. Copy the repository to your local machine and navigate to the directory where the `main.py` is located.

```bash
cd webCrawler
```

2. Highly recommended to create a virtual environment and activate it using the following commands:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Install the dependencies:

```bash
make install
```

## Usage

To use the web crawler, run the following command:

```bash
python main.py --url <url> --depth <depth> --filter <filter> --output <output> --verbose
```

## Help

To get help on the command line arguments, run the following command:

```bash
python main.py --help
or
python main.py -h
```

The following options are available:

- `--url`: The URL to scrape
- `--depth`: The depth to scrape
- `--filter`: The filter to apply (file extension, for example: pdf, jpg, etc.)
- `--output`: The path of the file to write the results to (e.g., output/results.txt)
- `--verbose`: Print verbose output (True/False)


## Example

To crawl the `https://www.example.com` web site with a depth of 2 and write the results to the `output/results.txt` file, run the following command:

```bash
python main.py --url https://www.example.com --depth 2 --output output/results.txt
```

## For Developers

To run the tests, run the following command:

```bash
make test
```

To run the linter, run the following command:

```bash
make lint
```

To run the formatter, run the following command:

```bash
make format
```

## Docker version

To build the docker image, run the following command:

```bash
docker build -t web-crawler .
```

To run the docker image, run the following command:

```bash
docker run -it web-crawler main.py --url <url> --depth <depth> --filter <filter> --output <output> --verbose <verbose>
```

For example:

```bash
docker run -it web-crawler main.py --url https://www.example.com --depth 2 --filter .png --verbose True
```

make sure to add `--verbose=True` to see the output