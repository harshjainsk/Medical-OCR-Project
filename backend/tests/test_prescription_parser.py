from backend.src.parser_prescription import PrescriptionParser
import pytest


@pytest.fixture()
def doc_1_maria():
    document_text = """
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC


Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times"""

    return PrescriptionParser(document_text)


def test_get_name(doc_1_maria):
    assert doc_1_maria.get_field('patient_name') == 'Marta Sharapova'


def test_get_address(doc_1_maria):
    assert doc_1_maria.get_field('patient_address') == '9 tennis court, new Russia, DC'


def test_get_medicines(doc_1_maria):
    assert doc_1_maria.get_field('medicines') == 'Prednisone 20 mg\nLialda 2.4 gram'


def test_get_directions(doc_1_maria):
    assert doc_1_maria.get_field('directions') == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month'


def test_get_refill(doc_1_maria):
    assert doc_1_maria.get_field('refill') == '2'
