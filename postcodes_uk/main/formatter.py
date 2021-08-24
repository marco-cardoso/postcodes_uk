import re

from postcodes_uk.main.exceptions import *
from postcodes_uk.main.validator import *


class Postcode:

    def __init__(self, area: str, district: str, sector: int, unit: str) -> None:
        if not valid_postcode_area(area):
            raise InvalidArea

        if not valid_postcode_district(district):
            raise InvalidDistrict

        if not valid_postcode_sector(sector):
            raise InvalidSector

        if not valid_postcode_unit(unit):
            raise InvalidUnit

        self.area = area
        self.district = district
        self.sector = sector
        self.unit = unit

        self.outward_code = area + district
        self.inward_code = str(sector) + unit

    def __str__(self):
        string = self.outward_code + " " + self.inward_code
        return string

    def __eq__(self, other):
        if (self.area == other.area) and (self.district == other.district) and (self.sector == other.sector) and (self.unit == other.unit):
            return True
        return False

    @staticmethod
    def from_string(postcode: str):
        """
        Create a Postcode object from a string
        :param postcode: A string with the postcode
        :return: A postcode object
        """

        match = re.search(
            "^ *?(("
            "(?P<area>[A-Z]{1,2})"
            "(?P<district>[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA))"
            " *?"
            "(?P<sector>[0-9])"
            "(?P<unit>[A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1"
            ")) *?$",
            postcode
        )

        area = match.group("area")
        district = match.group("district")
        sector = int(match.group("sector"))
        unit = match.group("unit")

        return Postcode(area, district, sector, unit)

