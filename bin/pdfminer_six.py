# Here's a mock-up of what the modified code would look like:
import argparse
from pdfminer.high_level import extract_text


def extract_pdf_content(pdf_path: str) -> str:
    """
    Extracts text content from the specified PDF.

    Args:
    - pdf_path (str): Path to the input PDF file.

    Returns:
    - str: Extracted text content.
    """
    return extract_text(pdf_path)


def parse_arguments():
    """
    Set up and parse command-line arguments.

    Returns:
    - argparse.Namespace: Parsed arguments.
    """

    # Initialize argparse
    parser = argparse.ArgumentParser(description="Extract text from a PDF.")
    parser.add_argument("pdf_path", type=str, help="Path to the input PDF file.")

    return parser.parse_args()


def main():
    # Parse arguments
    args = parse_arguments()

    # Extract text and print
    text = extract_pdf_content(args.pdf_path)
    print(text)

# Ensure the main function is only executed when this script is run directly
if __name__ == "__main__":
    main()