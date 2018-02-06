import logging

from chatbot.entities.Customer import Customer


class ActionTypes:
    add_new_data = "add_new_data"
    go_back = "go_back"
    clear_all = "clear_all"


class TopicsHandler:

    topic_clear_all = "clear_all"
    topic_go_back = "go_back"
    topics_customer_data = None

    def __init__(self, customer_topics, scenario_id):
        self.scenario_id = scenario_id
        self.topics_customer_data = customer_topics

    def check_message(self, msg):
        if 'topic' not in msg:
            raise TypeError("Topic is not exist")
        if not isinstance(msg['topic'], str):
            raise TypeError("Topic is incorrect")
        if 'parameters' not in msg:
            raise TypeError("Parameters are not exists")
        if not isinstance(msg['parameters'], dict):
            raise TypeError("Parameters filed is incorrect")

    async def processing_data(self, messages, db):
        action, params = self.handle_incoming_messages(messages)
        if action == ActionTypes.go_back:
            await db.go_back(self.scenario_id)
        elif action == ActionTypes.clear_all:
            await db.clear_all(self.scenario_id)
        elif action == ActionTypes.add_new_data:
            await db.add_customer(Customer.from_dict(params), self.scenario_id)

    def handle_incoming_messages(self, messages):
        customer_data = {k: {} for k in self.topics_customer_data}
        for msg in messages:
            try:
                self.check_message(msg)
                if msg['topic'] in self.topics_customer_data:
                    customer_data[msg['topic']].update(msg['parameters'])
                elif msg['topic'] == self.topic_clear_all:
                    return ActionTypes.clear_all, None
                elif msg['topic'] == self.topic_go_back:
                    return ActionTypes.go_back, None
                else:
                    raise TypeError("Unknown topic")
            except Exception as e:
                logging.warning("Message %s caused error '%s'" % (msg, e))

        return ActionTypes.add_new_data, customer_data
