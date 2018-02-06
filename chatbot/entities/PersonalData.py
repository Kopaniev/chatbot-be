
class PersonalData:

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    @classmethod
    def from_dict(cls, adict):
        return PersonalData(
            name=adict.get('name', None),
            dob=adict.get('dob', None)
        ) if adict is not None else None
