from uk_postcodes.main.validator import *


def test_validate_postcode():
    assert valid_postcode("EC1A 1BB") is True
    assert valid_postcode("E1A 1BB") is True
    assert valid_postcode("W1A 0AX") is True
    assert valid_postcode("M1 1AE") is True
    assert valid_postcode("B33 8TH") is True
    assert valid_postcode("CR2 6XH") is True
    assert valid_postcode("DN55 1PT") is True

    assert valid_postcode("SADAKMxa da") is False
    assert valid_postcode("") is False
    assert valid_postcode("1C1A 1BB") is False
    assert valid_postcode("E122A 1BB") is False
    assert valid_postcode("EC1A 100") is False


def test_validate_postcode_area():
    assert valid_postcode_area("EC") is True
    assert valid_postcode_area("A") is True
    assert valid_postcode_area("a") is False
    assert valid_postcode_area("212") is False
    assert valid_postcode_area("") is False


def test_validate_postcode_district():
    assert valid_postcode_district("2") is True
    assert valid_postcode_district("21") is True
    assert valid_postcode_district("2A") is True
    assert valid_postcode_district("3B") is True

    assert valid_postcode_district("AB") is False
    assert valid_postcode_district("A2") is False
    assert valid_postcode_district("") is False


def test_validate_postcode_sector():
    assert valid_postcode_sector(2) is True
    assert valid_postcode_sector(0) is True
    assert valid_postcode_sector(9) is True

    assert valid_postcode_sector(-9) is False
    assert valid_postcode_sector(10) is False


def test_validate_postcode_unit():
    assert valid_postcode_unit("HF") is True
    assert valid_postcode_unit("AB") is True

    assert valid_postcode_unit("ab") is False
    assert valid_postcode_unit("") is False

