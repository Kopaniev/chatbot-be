from chatbot.adapters.ParseAddress import ParseAddress


def parse_address_from_string():
    ad1 = "Spear St, San Francisco, CA 94105, USA"
    re1 = {'state': 'California', 'city': 'San Francisco',
           'street': 'Spear Street', 'zipcode': '94105'}
    ad2 = "94105 Spear Street calfironia, " \
          "SF United states; spear str apt 41 SF"
    re2 = {'state': 'California', 'city': 'San Francisco',
           'street': 'Spear Street', 'zipcode': '94105'}

    assert ParseAddress.get_address_from_string(ad1) == re1
    assert ParseAddress.get_address_from_string(ad2) == re2


if __name__ == '__main__':
    parse_address_from_string()
