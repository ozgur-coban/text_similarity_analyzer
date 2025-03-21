from extract_ops import HtmlParser
from preprocessing import PreProcessor


def main():
    parser = HtmlParser(
        file_path="../data/eng/anamnesis.html",
        output_path="../data/outputs/output.json",
    )
    # text = parser.extract_text()
    parser.run()


if __name__ == "__main__":
    main()
