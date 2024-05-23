import pytest
from unittest.mock import patch
from io import StringIO
from src.crawler import WebCrawler


@pytest.fixture
def crawler_instance():
    url = "https://google.com"
    depth = 1
    file_type = ".png"
    verbose = False
    output_path = "test_output.txt"
    return WebCrawler(url, depth, file_type, verbose, output_path)


def test_crawl_output(crawler_instance):
    crawler_instance.verbose = True

    # Mock the output file
    with patch("sys.stdout", new=StringIO()) as mock_stdout:
        # Perform the crawling
        crawler_instance.crawl()

        # Get the output from stdout
        output = mock_stdout.getvalue()

    # Assertions
    assert output.startswith("Job Description:")
    assert "Crawling" in output
    assert "Found image:" in output
    # assert "Found file:" in output


def test_output_file(crawler_instance):
    # Perform the crawling
    crawler_instance.crawl()

    # Read the output file
    with open(crawler_instance.output_path, "r") as output_file:
        output = output_file.read()

    # Assertions
    assert output.startswith("Job Description:")
    assert "Crawling" in output
    assert "Found image:" in output
    # assert "Found file:" in output
