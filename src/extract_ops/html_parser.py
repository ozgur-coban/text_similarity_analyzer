import os
import json
from bs4 import BeautifulSoup


class HtmlParser:
    def __init__(self, input_folder, output_folder):
        self.tags = ["script", "style", "meta", "link"]
        self.input_folder = input_folder
        self.output_folder = output_folder

    def load_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def save_text_to_file(self, text, output_filename):
        output_path = os.path.join(self.output_folder, output_filename)
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(text, file, ensure_ascii=False, indent=4)

    def remove_tags(self, soup):
        for tag in self.tags:
            for element in soup.find_all(tag):
                element.decompose()

    def extract_text(self, file_content):
        soup = BeautifulSoup(file_content, "html.parser")
        self.remove_tags(soup)
        raw_text = soup.get_text(separator=" ", strip=True)
        return raw_text

    def process_files(self):
        # Get a list of all HTML files in the input folder
        for filename in os.listdir(self.input_folder):
            if filename.endswith(".html") or filename.endswith(".htm"):
                file_path = os.path.join(self.input_folder, filename)
                file_content = self.load_file(file_path)
                cleaned_text = self.extract_text(file_content)

                # Save the cleaned text with the same filename but as a JSON
                output_filename = os.path.splitext(filename)[0] + "_cleaned.json"
                self.save_text_to_file(cleaned_text, output_filename)

    def run(self):
        self.process_files()
