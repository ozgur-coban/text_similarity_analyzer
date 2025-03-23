import json
import pandas as pd

# Load lemmatized similarity results
with open(
    "../../data/outputs/tfidf_bow_results_tr.json", "r", encoding="utf-8"
) as file:
    lemmatized_data = json.load(file)

# Load non-lemmatized similarity results
with open(
    "../../data/outputs/tfidf_bow_non_lematized_results.json", "r", encoding="utf-8"
) as file:
    non_lemmatized_data = json.load(file)

# Convert both JSON lists to DataFrames
df_lemmatized = pd.DataFrame(lemmatized_data)
df_non_lemmatized = pd.DataFrame(non_lemmatized_data)

# Rename TF-IDF and BOW similarity columns before merging
df_lemmatized.rename(
    columns={
        "tfidf_similarity": "tfidf_similarity_lemmatized",
        "bow_similarity": "bow_similarity_lemmatized",
    },
    inplace=True,
)

df_non_lemmatized.rename(
    columns={
        "tfidf_similarity": "tfidf_similarity_non_lemmatized",
        "bow_similarity": "bow_similarity_non_lemmatized",
    },
    inplace=True,
)

# Merge on 'file1' and 'file2'
df_combined = pd.merge(
    df_lemmatized, df_non_lemmatized, on=["file1", "file2"], how="inner"
)

# Save to CSV
df_combined.to_csv(
    "../../data/outputs/combined_results_tr.csv", index=False, encoding="utf-8"
)

print("Combined CSV saved as 'combined_results.csv'")
