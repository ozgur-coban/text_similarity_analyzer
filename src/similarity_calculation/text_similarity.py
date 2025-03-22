import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
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

    def calculate_similarity_tdidf(self, n=1):
        """Calculate similarity percentage using TF-IDF and Cosine Similarity."""
        # Initialize the TF-IDF Vectorizer
        vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(n, n))

        # Transform the texts into TF-IDF vectors
        tfidf_matrix = vectorizer.fit_transform(
            [self.first_file_text, self.second_file_text]
        )
        # vocabulary = vectorizer.get_feature_names_out()
        # print(vocabulary)
        # df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=vocabulary)
        # df_tfidf.to_csv("../data/outputs/tfidf_output.csv", index=False)
        similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        similarity_percentage = similarity_matrix[0][0] * 100

        return similarity_percentage

    def calculate_similarity_bow(self, n=1):
        vectorizer = CountVectorizer(stop_words="english", ngram_range=(n, n))
        bow_matrix = vectorizer.fit_transform(
            [self.first_file_text, self.second_file_text]
        )
        # vocabulary = vectorizer.get_feature_names_out()
        # df_bow = pd.DataFrame(bow_matrix.toarray(), columns=vocabulary)
        # df_bow.to_csv("../data/outputs/bow_output.csv", index=False)
        similarity_matrix = cosine_similarity(bow_matrix[0:1], bow_matrix[1:2])
        similarity_percentage = similarity_matrix[0][0] * 100
        return similarity_percentage

    def display_similarity(self):
        """Display the calculated similarity."""
        similarity_percentage = self.calculate_similarity_tdidf()
        # similarity_percentage = self.calculate_similarity_bow()
        print(f"Text1, Text2: similarity percentage = {similarity_percentage:.2f}%")
