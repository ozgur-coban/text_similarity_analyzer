import re
import json


class PreProcessor:
    def __init__(self, output_path):
        self.output_path = output_path

    def save_text_to_file(self, text):
        with open(self.output_path, "w", encoding="utf-8") as file:
            json.dump(text, file, ensure_ascii=False, indent=4)

    def normalize_text(self, text):
        lowered_text = text.lower()
        # Replace multiple spaces with a single space
        lowered_text = re.sub(r"\s+", " ", text)
        return lowered_text

    def remove_unwanted_characters(self, text):
        text = re.sub(r"[^\w\s:?.!,-]", "", text)
        return text

    def clean_placeholders(self, text):
        """Removes Handlebars-like placeholders and ensures proper spacing."""
        # Capture the 'Yes' and 'No' values inside {{#if ...}} and insert a space between them
        text = re.sub(
            r"\{\{#if.*?\}\}(.*?)\{\{else\}\}(.*?)\{\{\/if\}\}",
            r"\1 \2",
            flags=re.DOTALL,
            string=text,
        )

        # Remove any remaining {{ }} placeholders
        text = re.sub(r"\{\{.*?\}\}", "", text)

        # Normalize spaces
        text = re.sub(r"\s+", " ", text).strip()

        return text

    def remove_extra_whitespace(self, text):
        text = text.strip()
        text = re.sub(r"\s+", " ", text)
        return text

    def handle_concatenation(self, text):
        """Dynamically handle concatenation of words like LowHigh or HeartAttack."""

        def split_camel_case(match):
            word = match.group(0)
            # Check if the word is an acronym (all uppercase)
            if word.isupper() and len(word) > 1:
                return word  # Leave acronyms intact
            # Otherwise, split camel case (e.g., LowHigh -> Low High)
            return word[0] + " " + word[1:]

        # Split camel case but keep acronyms intact
        text = re.sub(r"([a-z])([A-Z])", split_camel_case, text)
        return text

    def preprocess(self, text):
        # Combine all preprocessing steps
        text = self.clean_placeholders(text)
        text = self.normalize_text(text)
        text = self.remove_unwanted_characters(text)
        text = self.remove_extra_whitespace(text)
        text = self.handle_concatenation(text)
        return text

    def run(self, text):
        preprocessed_text = self.preprocess(text=text)
        self.save_text_to_file(text=preprocessed_text)
