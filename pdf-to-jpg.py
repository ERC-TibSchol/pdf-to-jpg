import os
from pdf2image import convert_from_path

def pdf_to_jpg(pdf_path, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Convert PDF pages to images
    images = convert_from_path(pdf_path, poppler_path="path/to/poppler/bin")

    print("Converting PDF to JPG...")

    # Save images as JPG files
    for i, image in enumerate(images):
        image.save(os.path.join(output_folder, f"page_{i+1}.jpg"), "JPEG")

    print("Conversion complete!")

# Specify the path to your PDF and the output folder
pdf_path = "path/to/your/pdf/file.pdf"
output_folder = "path/to/your/output/folder"
# Convert the PDF to JPG
pdf_to_jpg(pdf_path, output_folder)

