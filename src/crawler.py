"""
Module to crawl given URL and extract all the links from the page upto a given depth and write the results to a file
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
from tqdm import tqdm


class WebCrawler:
    def __init__(self, url, depth=1, file_type=None, verbose=False, output_path=None):
        self.url = url
        self.depth = depth
        self.file_type = file_type
        self.verbose = verbose
        self.output_path = output_path
        self.visited_urls = set()

    def filter_files(self, links):
        links = list(set(links))
        return [link for link in links if link.endswith(self.file_type)]

    def crawl(self):
        with open(self.output_path, "w", encoding="utf-8") as output_file:
            job_description = self.get_job_description()
            output_file.write(job_description)
            if self.verbose:
                print(job_description)

            self.recursive_crawl(self.url, self.depth, output_file)

    def recursive_crawl(self, url, depth, output_file):
        if depth == 0:
            return
        if url in self.visited_urls:
            return
        self.visited_urls.add(url)

        try:
            response = requests.get(url,timeout=50)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            links = [link.get("href") for link in soup.find_all("a", href=True)]
            images = [img.get("src") for img in soup.find_all("img", src=True)]
            files = [
                link
                for link in links
                if link.endswith(
                    (
                        ".pdf",
                        ".doc",
                        ".docx",
                        ".xls",
                        ".xlsx",
                        ".ppt",
                        ".pptx",
                        ".txt",
                        ".csv",
                        ".zip",
                        ".rar",
                        ".tar",
                        ".gz",
                        ".7z",
                        ".exe",
                        ".msi",
                        ".apk",
                        ".dmg",
                        ".iso",
                        ".img",
                        ".bin",
                        ".cue",
                        ".mdf",
                        ".nrg",
                        ".vcd",
                        ".vmdk",
                        ".ova",
                        ".ovf",
                        ".vdi",
                        ".vhd",
                        ".vhdx",
                        ".vmsd",
                        ".vmx",
                        ".vmxf",
                        ".vmsn",
                        ".vmtm",
                        ".vmem",
                        ".nvram",
                    )
                )
            ]

            if self.file_type:
                filtered_images = self.filter_files(images)
                filtered_files = self.filter_files(files)
            else:
                filtered_images = images
                filtered_files = files

            output_line = f"Crawling {url}\n"
            if self.verbose:
                print(output_line, end="")
            output_file.write(output_line)

            for link in tqdm(links, desc="Processing links"):
                absolute_link = urljoin(url, link)
                self.recursive_crawl(absolute_link, depth - 1, output_file)

            if filtered_images:
                for img in filtered_images:
                    absolute_img_url = urljoin(url, img)
                    output_line = f"Found image: {absolute_img_url}\n"
                    if self.verbose:
                        print(output_line, end="")
                    output_file.write(output_line)

            if filtered_files:
                for file in filtered_files:
                    absolute_link = urljoin(url, file)
                    output_line = f"Found file: {absolute_link}\n"
                    if self.verbose:
                        print(output_line, end="")
                    output_file.write(output_line)

        except Exception as e:
            error_message = f"Error crawling {url}: {e}\n"
            if self.verbose:
                print(error_message, end="")
            output_file.write(error_message)

        time.sleep(0.5)

    def get_job_description(self):
        return (
            f"Job Description:\n"
            f"URL: {self.url}\n"
            f"Depth: {self.depth}\n"
            f"Filter: {self.file_type}\n"
            f"Verbose: {self.verbose}\n"
            f"Output Path: {self.output_path}\n"
            f"{'='*20}\n"
        )
