from extract_ops import HtmlParser
from preprocessing import PreProcessor
from similarity_calculation import TextSimilarity


def main():
    # parser = HtmlParser(
    #     file_path="../data/eng/endodonticform.html",
    #     output_path="../data/preprocessing_outputs/output.json",
    # )
    # text = parser.extract_text()
    # preprocessor = PreProcessor(
    #     output_path="../data/preprocessing_outputs/output_after_preprocessing_endodonticform.json"
    # )
    # # preprocessed_text = preprocessor.preprocess(text=text)
    # preprocessor.run(text=text)
    similarity_calculator = TextSimilarity(
        first_file_path="../data/preprocessing_outputs/output_after_preprocessing_anamnesis.json",
        second_file_path="../data/preprocessing_outputs/output_after_preprocessing_endodonticform.json",
        output_file_path="../data/outputs/output_of_similarity_calculation",
    )
    similarity_calculator.display_similarity()


if __name__ == "__main__":
    main()
