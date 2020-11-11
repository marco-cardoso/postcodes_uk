import re


def valid_postcode(postcode: str) -> bool:
    """
    Validate a british postcode
    For more information, please read : https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
    :param postcode: A string with the UK postcode
    :return: A boolean result with whether the postcode is valid or not
    """

    result = bool(re.match(
        "^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"
        , postcode
    ))
    return result


def valid_postcode_area(area: str):
    """
    Validate a british postcode area
    :param area: A string with the UK postcode area
    :return: A boolean result with whether the postcode area is valid or not
    """
    result = bool(re.match(
        "[A-Z]{1,2}",
        area
    ))
    return result


def valid_postcode_district(district: str):
    """
   Validate a british postcode district
   :param district: A string with the UK postcode district
   :return: A boolean result with whether the postcode district is valid or not
   """
    result = bool(re.match(
        "[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA",
        district
    ))
    return result


def valid_postcode_sector(sector: int):
    """
   Validate a british postcode sector
   :param sector: A string with the UK postcode sector
   :return: A boolean result with whether the postcode sector is valid or not
   """
    result = True if (sector >= 0) & (sector <= 9) else False
    return result


def valid_postcode_unit(unit: str):
    """
   Validate a british postcode unit
   :param unit: A string with the UK postcode unit
   :return: A boolean result with whether the postcode unit is valid or not
   """
    result = bool(re.match(
        "[A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1",
        unit
    ))
    return result
