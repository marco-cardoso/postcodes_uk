import pytest

from postcodes_uk import Postcode
from postcodes_uk.main.exceptions import *


def test_postcode_from_string():
    assert Postcode(area="EC", district="1A", sector=1, unit="BB") == Postcode.from_string("EC1A 1BB")
    assert Postcode(area="EC", district="1A", sector=1, unit="BB") != Postcode.from_string("EC1B 1BB")
    assert Postcode(area="EC", district="1A", sector=1, unit="BB") != Postcode.from_string("EC1B  1BB")
    assert Postcode(area="EC", district="1A", sector=1, unit="BB") != Postcode.from_string(" EC1B 1BB")
    assert Postcode(area="EC", district="1A", sector=1, unit="BB") != Postcode.from_string("EC1B 1BB ")

    with pytest.raises(InvalidPostcode):
        Postcode.from_string("1234ABCD")


def test_postcode_init():

    with pytest.raises(InvalidArea):
        Postcode(area="1C", district="1A", sector=1, unit="BB")

    with pytest.raises(InvalidArea):
        Postcode(area="2", district="1A", sector=1, unit="BB")

    with pytest.raises(InvalidArea):
        Postcode(area="", district="1A", sector=1, unit="BB")

    with pytest.raises(InvalidUnit):
        Postcode(area="EC", district="1A", sector=1, unit="1B")

    with pytest.raises(InvalidUnit):
        Postcode(area="EC", district="1A", sector=1, unit="12")

    with pytest.raises(InvalidUnit):
        Postcode(area="EC", district="1A", sector=1, unit="B2")

    with pytest.raises(InvalidUnit):
        Postcode(area="EC", district="1A", sector=1, unit="")

    with pytest.raises(InvalidSector):
        Postcode(area="EC", district="1A", sector=-1, unit="BB")

    with pytest.raises(InvalidSector):
        Postcode(area="EC", district="1A", sector=10, unit="BB")

    with pytest.raises(InvalidDistrict):
        Postcode(area="EC", district="A", sector=1, unit="BB")

    with pytest.raises(InvalidDistrict):
        Postcode(area="EC", district="", sector=1, unit="BB")
