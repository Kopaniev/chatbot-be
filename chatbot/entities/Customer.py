from chatbot.entities.PersonalData import PersonalData
from chatbot.entities.VehicleData import VehicleData
from chatbot.entities.GeoData import GeoData


class Customer:

    def __init__(self, person_data, vehicle_data, geo_data):
        if person_data:
            if not isinstance(person_data, PersonalData):
                raise TypeError("person_data should be "
                                "instance of PersonalData")
            self.person_data = person_data

        if vehicle_data:
            if not isinstance(vehicle_data, VehicleData):
                raise TypeError("vehicle_data should be "
                                "instance of VehicleData")
            self.vehicle_data = vehicle_data

        if geo_data:
            if not isinstance(geo_data, GeoData):
                raise TypeError("geo_data should "
                                "be instance of GeoData")
            self.geo_data = geo_data

    @classmethod
    def from_dict(cls, adict):
        return Customer(
            person_data=PersonalData.from_dict(
                adict.get('person_data', None)
            ),
            vehicle_data=VehicleData.from_dict(
                adict.get('vehicle_data', None)
            ),
            geo_data=GeoData.from_dict(
                adict.get('geo_data', None)
            )
        )

    def count_empty(self):
        empty_amount = 0
        for obj in self.__dict__.values():
            if obj:
                for field in obj.__dict__.values():
                    if not field:
                        empty_amount += 1
        return empty_amount

    def get_dict(self):
        return {
            obj_k: obj.__dict__
            for obj_k, obj in self.__dict__.items()
            if obj
        }
