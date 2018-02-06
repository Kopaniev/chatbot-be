
class GeoData:

    def __init__(self, postal_code):
        self.postal_code = postal_code

    @classmethod
    def from_dict(cls, adict):
        return GeoData(
            postal_code=adict.get('postal_code', None)
        ) if adict is not None else None
