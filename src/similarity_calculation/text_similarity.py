import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TextSimilarity:
    # TODO implement it so that it would get every file from 1 directory path and compare each of them to each other
    def __init__(self, first_file_path, second_file_path, output_file_path):
        self.first_file_path = first_file_path
        self.second_file_path = second_file_path
        self.output_file_path = output_file_path
        self.first_file_text = self.load_text_from_json(first_file_path)
        self.second_file_text = self.load_text_from_json(second_file_path)

    def load_text_from_json(self, json_file_path):
        """Load JSON file and extract text data."""
        with open(json_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def calculate_similarity(self):
        """Calculate similarity percentage using TF-IDF and Cosine Similarity."""
        # Initialize the TF-IDF Vectorizer
        vectorizer = TfidfVectorizer(stop_words="english")

        # Transform the texts into TF-IDF vectors
        tfidf_matrix = vectorizer.fit_transform(
            [self.first_file_text, self.second_file_text]
        )

        # Calculate cosine similarity between the two texts
        similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

        # Get similarity percentage (cosine similarity score between 0 and 1)
        similarity_percentage = similarity_matrix[0][0] * 100

        return similarity_percentage

    def display_similarity(self):
        """Display the calculated similarity."""
        similarity_percentage = self.calculate_similarity()
        print(f"Text1, Text2: similarity percentage = {similarity_percentage:.2f}%")
