from pdf2image import convert_from_path
import cv2
from PIL import Image
import numpy as np
from util import preprocess_image
import pytesseract


POPPLER_PATH = r"C:\poppler-22.04.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files\Tesseract-OCR\tesseract.exe"


def extract(file_path, file_format):
    # extracting text from pdf file

    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)


    document_text = ''
    for page in pages:
        processed_image = preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text

    return document_text

    # if file_format == 'prescripton':
    #     pass # extracting data from prescription
    #
    # elif file_format == 'patient_details':
    #     pass # extracting data from patient details


if __name__ == '__main__':
    data = extract('backend/resources/patient_details/pd_2.pdf', 'prescription')
    print(data)