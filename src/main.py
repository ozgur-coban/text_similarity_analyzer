from extract_ops import HtmlParser
from preprocessing import PreProcessor
from similarity_calculation import TextSimilarity


def main():
    # parser = HtmlParser(
    #     input_folder="../data/en", output_folder="../data/parsed_outputs"
    # )
    # parser.run()
    # preprocessor = PreProcessor(
    #     input_folder="../data/parsed_outputs",
    #     output_folder="../data/preprocessing_outputs_lemmatized_en",
    #     do_lema=True,
    #     language="en",
    # )
    # preprocessor.run()
    similarity_calculator = TextSimilarity(
        input_folder="../data/preprocessing_outputs_lemmatized",
        output_file_path="../data/outputs",
    )
    similarity_calculator.compute_all_similarities()


if __name__ == "__main__":
    main()
