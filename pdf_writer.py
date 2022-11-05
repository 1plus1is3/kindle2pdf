"""
    kindle2pdf 2022
"""
import os
import img2pdf

from PIL import Image


class PDFWriter:
    """
    Class for converting multiple images to PDF
    """

    def image_to_pdf(self) -> None:
        """
        :function:
            - image_to_pdf
        :brief:
            - Convert images convert to PDF file

        :Args:
            - None
        :Return:
            - None
        """
        # Enter pdf name in console and receive
        print("Enter the name of the output pdf")
        output_pdf_name = input()
        output_pdf_name = f'{output_pdf_name}.pdf'

        # Specify the save destination path
        png_folder = "D:/KindlePDF/test/test_png/"

        # Convert all files ending with extension specified by extention to ONE pdf
        extension = ".png"

        with open(output_pdf_name, "wb") as f:
            f.write(img2pdf.convert([Image.open(png_folder+j).filename for j in os.listdir(png_folder)if j.endswith(extension)]))
