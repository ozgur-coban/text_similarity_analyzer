import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TextSimilarity:
    def __init__(self, input_folder, output_file_path, method="tfidf"):
        self.input_folder = input_folder
        self.method = method
        self.output_file_path = output_file_path + "/" + f"{self.method}_results.json"
        self.files = self.load_all_json_files()

    def load_all_json_files(self):
        """Load text content from all JSON files in the input folder."""
        files_content = {}

        for filename in os.listdir(self.input_folder):
            if filename.endswith(".json"):
                file_path = os.path.join(self.input_folder, filename)
                with open(file_path, "r", encoding="utf-8") as file:
                    files_content[filename] = json.load(file)

        return files_content  # { "file1.json": "text", "file2.json": "text", ... }

    def calculate_similarity(self, text1, text2, n=1):
        """Calculate similarity using TF-IDF or BOW."""
        if self.method == "tfidf":
            vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(n, n))
        else:
            vectorizer = CountVectorizer(stop_words="english", ngram_range=(n, n))

        matrix = vectorizer.fit_transform([text1, text2])
        similarity_matrix = cosine_similarity(matrix[0:1], matrix[1:2])
        similarity_percentage = similarity_matrix[0][0] * 100

        return similarity_percentage

    def process_all_files(self, n=1):
        """Compare each file to every other file and store the similarity results."""
        results = []

        file_names = list(self.files.keys())

        for i in range(len(file_names)):
            for j in range(i + 1, len(file_names)):
                file1, file2 = file_names[i], file_names[j]
                text1, text2 = self.files[file1], self.files[file2]

                similarity = self.calculate_similarity(text1, text2, n)

                results.append(
                    {
                        "file1": file1,
                        "file2": file2,
                        "similarity_percentage": round(similarity, 2),
                    }
                )
                print(f"done with {file1, file2}")

        # Save results to a JSON file
        with open(self.output_file_path, "w", encoding="utf-8") as file:
            json.dump(results, file, ensure_ascii=False, indent=4)

        print(f"Similarity results saved to: {self.output_file_path}")
