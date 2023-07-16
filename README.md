# PDF to JPG Converter

A simple script that converts a PDF file into a series of JPG images. It utilises the `pdf2image` library to perform the conversion.

The script was created for the ERC project The Dawn of Tibetan Buddhist Scholasticism (11th-13th c.) (TibSchol). Cf. https://www.oeaw.ac.at/ikga/tibschol for more information.

This project has received funding from the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (grant agreement No. 101001002). See https://cordis.europa.eu/project/id/101001002.

# Prerequisites

- `pdf2image` library

This script relies on the `pdf2image` library, which is built on top of Poppler for PDF rendering. Install Poppler on your system and provide the correct path to `poppler_path` parameter in the `convert_from_path` function.

For more information on the library, see [pdf2image documentation](https://github.com/Belval/pdf2image).

# Usage

1. Specify the path to your PDF file by modifying the `pdf_path` variable in the script
2. Specify the output folder where the converted JPG images will be saved by modifying the `output_folder` variable in the script
3. The script will create the output folder if it doesn't exist already
4. The JPG images will be named as `page_1.jpg`, `page_2.jpg`, and so on, corresponding to the page numbers in the PDF
