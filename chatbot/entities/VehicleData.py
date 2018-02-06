
class VehicleData:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @classmethod
    def from_dict(cls, adict):
        return VehicleData(
            make=adict.get('make', None),
            model=adict.get('model', None),
            year=adict.get('year', None)
        ) if adict is not None else None
