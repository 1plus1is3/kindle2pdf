"""
    kindle2pdf 2022
"""
from capture import Capture
from pdf_writer import PDFWriter

class Main:
    """
    Main class for executing kindle2pdf
    """

    capture = Capture()
    pdf_writer = PDFWriter()

    # Get coordinates for taking screenshots
    x_1, y_1, x_2, y_2 = capture.window_manager()

    # Take a screenshot of one Kindle book using the acquired coordinates
    # Output in png format
    capture.window_capture(x_1, y_1, x_2, y_2)

    # Convert images ONE to pdf
    pdf_writer.image_to_pdf()
