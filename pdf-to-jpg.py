import os
import argparse
from pdf2image import convert_from_path
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(pdf_path, output_folder, chunk_size=10):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the PDF using PyPDF2
    pdf = PdfReader(pdf_path)
    total_pages = len(pdf.pages)

    print("Splitting PDF...")

    # Split the PDF into chunks
    processed_pages = 0
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

    print("PDF splitting complete!")

def pdf_to_jpg(pdf_path, output_folder, start_page_number=1):
    # Convert PDF pages to images
    images = convert_from_path(pdf_path, poppler_path=r"C:\Users\Racha\OneDrive\Documents\poppler-0.68.0_x86\poppler-0.68.0\bin")

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
        split_pdf(args.pdf_path, args.output_folder, chunk_size=args.chunk_size)

        # Process each part and convert to JPG
        processed_pages = 0
        for chunk_number, file in enumerate(os.listdir(args.output_folder), start=1):
            if file.endswith(".pdf"):
                chunk_pdf_path = os.path.join(args.output_folder, file)
                pdf_to_jpg(chunk_pdf_path, args.output_folder, start_page_number=processed_pages + 1)

                # Update the total processed pages after each chunk
                with open(chunk_pdf_path, "rb") as chunk_file:
                    chunk_pdf = PdfReader(chunk_file)
                    processed_pages += len(chunk_pdf.pages)

    else:
        pdf_to_jpg(args.pdf_path, args.output_folder)

if __name__ == "__main__":
    main()
