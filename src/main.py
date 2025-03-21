from extract_ops import HtmlParser
from preprocessing import PreProcessor


def main():
    parser = HtmlParser(
        file_path="../data/eng/anamnesis.html",
        output_path="../data/outputs/output.json",
    )
    text = parser.extract_text()
    preprocessor = PreProcessor(
        output_path="../data/outputs/output_after_preprocessing.json"
    )
    # preprocessed_text = preprocessor.preprocess(text=text)
    preprocessor.run(text=text)


if __name__ == "__main__":
    main()
