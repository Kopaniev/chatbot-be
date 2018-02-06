import json

from chatbot.use_cases.TopicsHandler import TopicsHandler


def messages_processing_data():

    allow_topics = [
        'person_data',
        'vehicle_data',
        'geo_data'
    ]
    messages = [
        {
          "topic": "person_data",
          "parameters": {
            "name": "John Snow"
          }
        },
        {
          "topic": "vehicle_data",
          "parameters": {
            "make": "Audi",
            "model": "100",
            "year": "1991"
          }
        },
        {
          "topic": "geo_data",
          "parameters": {
            "postal_code": "78759"
          }
        }
    ]
    th = TopicsHandler(allow_topics, 1)

    action = 'add_new_data'
    customer_data = {
        'person_data': {'name': 'John Snow'},
        'vehicle_data': {'make': 'Audi', 'model': '100', 'year': '1991'},
        'geo_data': {'postal_code': '78759'}
    }

    r = th.handle_incoming_messages(messages)

    assert r == (action, customer_data)


def messages_processing_go_back():

    messages = [
        {
          "topic": "go_back",
          "parameters": {}
        }
    ]
    th = TopicsHandler([], 1)

    action = 'go_back'
    customer_data = None

    r = th.handle_incoming_messages(messages)
    assert r == (action, customer_data)


def messages_processing_clear_all():

    messages = [
        {
          "topic": "clear_all",
          "parameters": {}
        }
    ]
    th = TopicsHandler([], 1)

    action = 'clear_all'
    customer_data = None

    r = th.handle_incoming_messages(messages)
    assert r == (action, customer_data)


if __name__ == '__main__':
    messages_processing_data()
    messages_processing_go_back()
    messages_processing_clear_all()
