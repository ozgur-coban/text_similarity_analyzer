from extract_ops import HtmlParser
from preprocessing import PreProcessor
from similarity_calculation import TextSimilarity


def main():
    # parser = HtmlParser(
    #     input_folder="../data/eng", output_folder="../data/parsed_outputs"
    # )
    # parser.run()
    # preprocessor = PreProcessor(
    #     input_folder="../data/parsed_outputs",
    #     output_folder="../data/preprocessing_outputs",
    #     do_lema=True,
    # )
    # preprocessor.run()
    similarity_calculator = TextSimilarity(
        input_folder="../data/preprocessing_outputs",
        output_file_path="../data/outputs",
        method="tfidf",
    )
    similarity_calculator.process_all_files()


if __name__ == "__main__":
    main()
