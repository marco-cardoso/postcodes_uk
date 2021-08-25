class InvalidArea(Exception):
    def __init__(self, msg='Invalid postcode area', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class InvalidDistrict(Exception):
    def __init__(self, msg='Invalid postcode district', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class InvalidSector(Exception):
    def __init__(self, msg='Invalid postcode sector', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class InvalidUnit(Exception):
    def __init__(self, msg='Invalid postcode unit', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class InvalidPostcode(Exception):
    def __init__(self, msg='Invalid postcode', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
