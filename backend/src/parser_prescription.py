import re
from backend.src.parser_generic import MedicalDocParser


class PrescriptionParser(MedicalDocParser):

    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name': self.get_name(),
            'patient_address': self.get_address(),
            'medicines': self.get_medicines(),
            'direction': self.get_directions(),
            'refill': self.get_refill()
        }

    def get_name(self):
        pattern = 'Name:(.*)Date'
        matches = re.findall(pattern, self.text)

        if len(matches) > 0:
            return matches[0].strip()

    def get_address(self):
        pattern = 'Address:(.*)\n'
        matches = re.findall(pattern, self.text)

        if len(matches) > 0:
            return matches[0].strip()

    def get_medicines(self):
        pattern = "Address:[^\n]*(.*)Direction"
        matches = re.findall(pattern, self.text, flags=re.DOTALL)

        if len(matches) > 0:
            return matches[0].strip()

    def get_directions(self):
        pass

    def get_refill(self):
        pass


if __name__ == '__main__':
    document_text = '''
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

Refill: 2 times'''

    pp = PrescriptionParser(document_text)
    print(pp.parse())
