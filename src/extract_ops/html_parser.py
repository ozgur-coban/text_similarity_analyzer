import re
import json
from bs4 import BeautifulSoup


class HtmlParser:
    def __init__(self, file_path, output_path):
        self.tags = ["script", "style", "meta", "link"]
        self.file_content = self.load_file(file_path=file_path)
        self.output_path = output_path
        self.soup = BeautifulSoup(self.file_content, "html.parser")

    def load_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def save_text_to_file(self, text):
        with open(self.output_path, "w", encoding="utf-8") as file:
            json.dump(text, file, ensure_ascii=False, indent=4)

    def remove_tags(self):
        for tag in self.soup(self.tags):
            tag.decompose()

    def clean_placeholders(self, text):
        """Removes Handlebars-like placeholders and ensures proper spacing."""
        # Capture the 'Yes' and 'No' values inside {{#if ...}} and insert a space between them
        text = re.sub(
            r"\{\{#if.*?\}\}(.*?)\{\{else\}\}(.*?)\{\{\/if\}\}",
            r"\1 \2",
            text,
            flags=re.DOTALL,
        )

        # Remove any remaining {{ }} placeholders
        text = re.sub(r"\{\{.*?\}\}", "", text)

        # Normalize spaces
        text = re.sub(r"\s+", " ", text).strip()

        return text

    def extract_text(self):
        self.remove_tags()
        raw_text = self.soup.get_text(separator=" ", strip=True)
        cleaned_text = self.clean_placeholders(raw_text)
        return cleaned_text

    def run(self):
        cleaned_text = self.extract_text()
        self.save_text_to_file(text=cleaned_text)
