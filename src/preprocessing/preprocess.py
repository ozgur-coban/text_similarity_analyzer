import re
import json
import spacy
import os
import stanza


class PreProcessor:
    def __init__(self, input_folder, output_folder, language="en", do_lema=True):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.language = language
        self.lema = do_lema

        if language == "en":
            self.nlp = spacy.load("en_core_web_sm")
        elif language == "tr":
            stanza.download("tr")  # Ensure the Turkish model is available
            self.nlp = stanza.Pipeline("tr")  # Use Stanza for Turkish
        else:
            raise ValueError("Unsupported language! Choose 'en' or 'tr'.")

    def load_json_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    def save_text_to_file(self, text, output_filename):
        output_path = os.path.join(self.output_folder, output_filename)
        with open(output_path, "w", encoding="utf-8") as file:
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

    def tokenize_text(self, text):
        """Tokenizes text and removes stop words and punctuation."""
        if self.language == "en":
            doc = self.nlp(text)  # spaCy processing
            tokens = [
                token.text for token in doc if not token.is_stop and not token.is_punct
            ]

        elif self.language == "tr":
            doc = self.nlp(text)  # Stanza processing
            tokens = [
                word.text for sent in doc.sentences for word in sent.words
            ]  # Extract words from sentences

        return tokens

    def lemmatize_text(self, text):
        """Lemmatizes text based on the selected language."""
        if self.language == "en":
            doc = self.nlp(text)
            lemmatized_text = " ".join(
                [
                    token.lemma_
                    for token in doc
                    if not token.is_stop and not token.is_punct
                ]
            )

        elif self.language == "tr":
            doc = self.nlp(text)
            lemmatized_text = " ".join(
                [
                    word.lemma if word.lemma is not None else word.text
                    for sent in doc.sentences
                    for word in sent.words
                ]
            )

        return lemmatized_text

    def preprocess(self, text):
        # Combine all preprocessing steps
        text = self.clean_placeholders(text)
        text = self.normalize_text(text)
        text = self.remove_unwanted_characters(text)
        text = self.remove_extra_whitespace(text)
        text = self.handle_concatenation(text)
        if self.lema:
            tokens = self.tokenize_text(text=text)
            text_to_process = " ".join(tokens)  # Join the tokens into a string
            text = self.lemmatize_text(text=text_to_process)
        return text

    def process_folder(self):
        # Process each JSON file in the provided folder
        for filename in os.listdir(self.input_folder):
            if filename.endswith(".json"):  # Only process .json files
                file_path = os.path.join(self.input_folder, filename)
                output_file_name = os.path.splitext(filename)[0] + ".json"

                # Load raw content from JSON
                raw_content = self.load_json_file(file_path)

                # Preprocess raw content (since there's no 'key' like 'text', it's directly the content)
                preprocessed_content = self.preprocess(raw_content)

                # Save the preprocessed content into the output file
                self.save_text_to_file(
                    preprocessed_content, output_filename=output_file_name
                )

    def run(self):
        self.process_folder()
