# Text Similarity Project: Turkish and English Document Comparison

This project calculates and compares the similarity between documents in both Turkish and English. The project uses different text similarity techniques such as TF-IDF and Bag-of-Words (BoW) with both lemmatized and non-lemmatized versions of the text. The results for both languages are combined and saved into a final CSV file.

## Features

- **Text Preprocessing:**

  - Clean and normalize text
  - Remove unwanted characters
  - Tokenize, lemmatize (for lemmatized versions), and handle concatenation of camel case words

- **Text Similarity Calculation:**

  - TF-IDF similarity
  - Bag-of-Words similarity
  - For both lemmatized and non-lemmatized texts

- **Languages Supported:**

  - Turkish (using Stanza for tokenization and lemmatization)
  - English (using spaCy for tokenization and lemmatization)

- **Final Output:**
  - A combined CSV file with the similarity results for both Turkish and English documents

## Requirements

Before running the project, install the following dependencies:

pip install spacy stanza pandas scikit-learn
python -m spacy download en_core_web_sm
import stanza
stanza.download('tr')

## How It Works

### Text Preprocessing:

The preprocessing pipeline cleans, normalizes, removes unwanted characters, and lemmatizes the text (if enabled). Tokenization and lemmatization are performed using spaCy for English and Stanza for Turkish.

### Text Similarity Calculation:

The preprocessed text is vectorized using the TF-IDF and Bag-of-Words (BoW) models. Cosine similarity is then computed to determine how similar two documents are.

### Combining Results:

Similarity results for both Turkish and English texts are computed separately and saved into `combined_results_tr.csv` and `combined_results_en.csv`. The two files are then merged into a single file, `final_combined_results.csv`, with results for both languages.

## How to Use

### Prepare Input Files:

Place your input JSON files in the `data/inputs/` directory. Each file should contain a list of documents.

### Run Preprocessing:

Use the `PreProcessor` class to preprocess your input data. You can enable or disable lemmatization using the `do_lema` parameter.

### Calculate Similarities:

Run the `TextSimilarity` class to compute similarity results for both Turkish and English documents. The similarity results are saved in separate files for each language.

### Merge Results:

The final merged CSV file will be saved in the `data/outputs/` directory with similarity results for both Turkish and English documents.
