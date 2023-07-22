import os
import argparse
from pdf2image import convert_from_path
from PyPDF2 import PdfReader, PdfWriter
import tempfile
import shutil

def split_pdf(pdf_path, output_folder, chunk_size=20):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the PDF using PyPDF2
    pdf = PdfReader(pdf_path)
    total_pages = len(pdf.pages)

    print("Splitting PDF...")

    # Split the PDF into chunks
    processed_pages = 0
    chunk_pdf_paths = []  # Store the paths of all chunked PDFs
    for chunk_number, chunk_start in enumerate(range(0, total_pages, chunk_size), start=1):
        chunk_end = min(chunk_start + chunk_size, total_pages)

        # Create a new PDF with the current chunk of pages
        writer = PdfWriter()
        for page_num in range(chunk_start, chunk_end):
            writer.add_page(pdf.pages[page_num])

        # Save the new chunk as a separate PDF
        chunk_output_path = os.path.join(output_folder, f"chunk_{chunk_number}.pdf")
        with open(chunk_output_path, "wb") as output_file:
            writer.write(output_file)

        print(f"Saved chunk {chunk_number} with pages {chunk_start + 1} to {chunk_end} as PDF.")

        # Update the total processed pages
        processed_pages += (chunk_end - chunk_start)

        # Add the chunk PDF path to the list
        chunk_pdf_paths.append(chunk_output_path)

    print("PDF splitting complete!")
    return chunk_pdf_paths

def pdf_to_jpg(pdf_path, output_folder, start_page_number=1):
    # Convert PDF pages to images
    images = convert_from_path(pdf_path, poppler_path=r"path/to/poppler/bin")

    print("Converting PDF to JPG...")

    # Save images as JPG files with updated page numbers
    for i, image in enumerate(images):
        original_page_number = i + start_page_number
        image.save(os.path.join(output_folder, f"page_{original_page_number}.jpg"), "JPEG")

        print(f"Processed page {original_page_number}.")

    print("Conversion complete!")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Convert PDF to JPG.")
    parser.add_argument("pdf_path", help="Path to the PDF file.")
    parser.add_argument("output_folder", help="Path to the output folder.")
    parser.add_argument("--split", action="store_true", help="Split the PDF into smaller parts.")
    parser.add_argument("--chunk_size", type=int, default=20, help="Number of pages per chunk (if split is enabled).")
    args = parser.parse_args()

    # Check if the PDF should be split or converted as a whole
    if args.split:
        temp_dir = tempfile.mkdtemp()
        try:
            chunk_pdf_paths = split_pdf(args.pdf_path, temp_dir, chunk_size=args.chunk_size)

            # Process each part and convert to JPG
            processed_pages = 0
            for chunk_pdf_path in chunk_pdf_paths:
                with open(chunk_pdf_path, "rb") as chunk_file:
                    pdf_to_jpg(chunk_pdf_path, args.output_folder, start_page_number=processed_pages + 1)
                    processed_pages += len(PdfReader(chunk_file).pages)
        finally:
            # Delete the temporary directory and its contents (chunks)
            shutil.rmtree(temp_dir)

    else:
        pdf_to_jpg(args.pdf_path, args.output_folder)

if __name__ == "__main__":
    main()
