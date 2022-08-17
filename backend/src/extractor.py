from pdf2image import convert_from_path
from util import preprocess_image
import pytesseract
from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailsParser

POPPLER_PATH = r"C:\poppler-22.04.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files\Tesseract-OCR\tesseract.exe"


def extract(file_path, file_format):
    # extracting text from pdf file

    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)

    document_text = ''
    if len(pages) > 0:
        page = pages[0]
        processed_image = preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text

    if file_format == 'prescription':
        # extracting data from prescription
        extracted_data = PrescriptionParser(document_text).parse()

    elif file_format == 'patient_details':
        # extracting data from patient details
        extracted_data = PatientDetailsParser(document_text).parse()

    else:
        raise Exception(f"Invalid document format: {file_format}")

    return extracted_data


if __name__ == '__main__':
    data = extract('backend/resources/patient_details/pd_2.pdf', 'patient_details')
    print(data)
