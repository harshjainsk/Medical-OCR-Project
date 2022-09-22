# Medical Document Parser To Extract Useful Information

> This project was built to automate the process of extracting text from a prescription or patient details pdf(Portable Document Format).<br/>


## Preview 📺

### Patient Details Parser

<table>
  <tr>
    <td align="center"><h3><b>Before Pre-processing</b></h3></td>
    <td align="center"><h3><b>After Pre-processing</b></h3></td>
  </tr>
  <tr>
    <td><img src="https://github.com/harshjainsk/Medical-OCR-Project/blob/main/images/patient-details-before-preprocessing.png" width=500 height=600></td>
    <td><img src="https://github.com/harshjainsk/Medical-OCR-Project/blob/main/images/patient-details-after-preprocessing.png" width=500 height=600></td>
  </tr>
 </table>


The <a href="https://github.com/harshjainsk/Medical-OCR-Project/blob/main/backend/src/parser_patient_details.py">parser_patient_details.py script</a> converts <a href="https://github.com/harshjainsk/Medical-OCR-Project/tree/main/backend/resources/patient_details">patient details pdf</a> into an image. Once converted, pytesseract engine is used to extract text from the image. When text is extracted without any pre-processing on the image, we get <a href="https://github.com/harshjainsk/Medical-OCR-Project/blob/main/images/patient-details-text-before-preprocessing.txt">random noise</a>. Hence, OpenCV-python is used for preprocessing and once applied, there's <a href="https://github.com/harshjainsk/Medical-OCR-Project/blob/main/images/patient-details-text-before-preprocessing.txt">negligible noise</a>.

<hr>

### Prescription Parser

<table>
  <tr>
    <td align="center"><h3><b>Before Pre-processing</b></h3></td>
    <td align="center"><h3><b>After Pre-processing</b></h3></td>
  </tr>
  <tr>
    <td><img src="https://github.com/harshjainsk/Medical-OCR-Project/blob/main/images/prescription-details-before-preprocessing.PNG" width=500 height=600></td>
    <td><img src="https://github.com/harshjainsk/Medical-OCR-Project/blob/main/images/prescription-details-after-preprocessing.PNG" width=500 height=600></td>
  </tr>
 </table>
 
The <a href="https://github.com/harshjainsk/Medical-OCR-Project/blob/main/backend/src/parser_prescription.py">parser_prescription_details.py script</a> converts <a href="https://github.com/harshjainsk/Medical-OCR-Project/tree/main/backend/resources/prescription">prescriptions pdf</a> into an image. Once converted, pytesseract engine is used to extract text from the image. When text is extracted without any pre-processing on the image, we get <a href="https://github.com/harshjainsk/Medical-OCR-Project/blob/main/images/prescription-text-before-preprocessing.txt">random noise</a>. Hence, OpenCV-python is used for preprocessing and once applied, there's <a href="https://github.com/harshjainsk/Medical-OCR-Project/blob/main/images/prescription-text-after-preprocessing.txt">negligible noise</a>.

<hr>

# About the project

This project extracts useful information from prescription or patient details pdf. It can extract the following fields:
- <b>Patient name</b>
- <b>Patient address</b>
- <b>Medicines</b>
- <b>Direction of use</b>
- <b>Phone number</b>
- <b>Medical problems</b>
- <b>Vaccination details</b>

<hr>

# API endpoints
The <a href="https://github.com/harshjainsk/Medical-OCR-Project/blob/main/backend/src/parser_patient_details.py">main.py</a> file contains the API end-points for this application. Provided the document type and document, the script will return a json object of the extracted fields.

<div align="center"> 
<img width="90%" height="90%" src="https://github.com/harshjainsk/Medical-OCR-Project/blob/main/images/Medical-OCR-API-Demo.gif" hspace="10">
</div>
