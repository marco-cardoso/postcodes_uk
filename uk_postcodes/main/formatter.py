import re

from .validator import *
from .exceptions import *


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

    @staticmethod
    def from_string(postcode: str):
        validate_postcode(postcode)

        area = None
        district = None
        sector = None
        unit = None

        return Postcode(area, district, sector, unit)
