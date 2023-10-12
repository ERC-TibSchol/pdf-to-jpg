# PDF to JPG Converter

A script that converts a PDF file into a series of JPG images. It utilises `pdf2image` library to perform the conversion and `PyPDF2` library for splitting PDFs for processing.

The script was created for the ERC project *The Dawn of Tibetan Buddhist Scholasticism (11th-13th c.) (TibSchol)*. Cf. [https://www.oeaw.ac.at/projects/tibschol](https://www.oeaw.ac.at/projects/tibschol) for more information.

This project has received funding from the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (grant agreement No. 101001002). See https://cordis.europa.eu/project/id/101001002.

# Prerequisites

- `pdf2image` library

This script relies on the `pdf2image` library, which is built on top of [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) for PDF rendering. Install Poppler on your system and provide the correct path to `poppler_path` parameter in the `convert_from_path` function.

For more information on the library, see [pdf2image documentation](https://github.com/Belval/pdf2image).

- `PyPDF2` library

For more information on the library, see [PyPDF2 documentation](https://github.com/mstamy2/PyPDF2).

# Usage

Run the script with the following command:

   ```bash
   python pdf_to_jpg_converter.py "C:\path\to\your\pdf\file.pdf" "C:\path\to\your\output\folder" [--split] [--chunk_size CHUNK_SIZE]
   ```

   Replace `"C:\path\to\your\pdf\file.pdf"` with the path to the PDF file you want to convert, and `"C:\path\to\your\output\folder"` with the path to the folder where you want to save the JPG images.

   Optional arguments:

   - `--split`: Enable this option to split large PDFs into smaller chunks before converting to JPG. This option has been added as large PDFs can use up memory and cause the process to be killed. If this option is not provided, the entire PDF will be converted as one unit.

   - `--chunk_size CHUNK_SIZE`: Set the number of pages per chunk when splitting the PDF (default is 20). This argument is only effective when `--split` is enabled.

## Examples

- Convert the entire PDF to JPG:

   ```bash
   python pdf_to_jpg_converter.py /path/to/your/pdf/file.pdf /path/to/output/folder
   ```

- Split large PDFs into smaller chunks and convert to JPG:

   ```bash
   python pdf_to_jpg_converter.py /path/to/your/pdf/file.pdf /path/to/output/folder --split --chunk_size 20
   ```

   This will split the PDF into chunks of 20 pages each and convert each chunk to JPG images. The `processed_pages` variable will keep track of the total processed pages, ensuring that the page numbers are incremented appropriately. 

The chunks are removed once the program finishes executing.
