import requests


class ParseAddress:
    google_key = 'AIzaSyAbf29zOJlsk1Obzmq7zswPpEnS1dPBfJY'

    @classmethod
    def prepare_url(cls, address):
        address = address.replace(" ", "+")
        url = "https://maps.googleapis.com/maps/api/geocode/json?"
        params = "components=" \
                 "&language=" \
                 "&region=" \
                 "&bounds=" \
                 f"&key={cls.google_key}" \
                 f"&address={address}"
        return url + params

    @classmethod
    def send_request(cls, address):
        url = cls.prepare_url(address)
        return requests.get(url).json()

    @classmethod
    def get_address_from_string(cls, address):
        result = {
            "state": None,
            "city": None,
            "street": None,
            "zipcode": None
        }
        data = cls.send_request(address)
        for i in data['results']:
            for j in i['address_components']:
                if j['types'][0] == 'postal_code':
                    result['zipcode'] = j['long_name']
                if j['types'][0] == 'administrative_area_level_1':
                    result['state'] = j['long_name']
                if j['types'][0] == 'route':
                    result['street'] = j['long_name']
                if j['types'][0] == 'locality':
                    result['city'] = j['long_name']
        return result
