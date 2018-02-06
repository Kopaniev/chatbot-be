from time import time

from chatbot.entities.Customer import Customer
from chatbot.adapters.Actions import Actions


class CustomersDB:

    actionsdb = None

    def __init__(self, connector):
        self.mongo_connector = connector
        self.actionsdb = Actions(connector)

    async def add_customer(self, c: Customer, scenario_id: int):
        t = time()
        data = {
            "entities": c.get_dict(),
            "not_filled": c.count_empty(),
            "creation_timestamp": t,
            "edit_timestamp": t,
            "scenario_id": scenario_id,
            'is_deleted': False
        }
        await self.mongo_connector.customers.insert_one(data)
        await self.actionsdb.add_customer_data(t, scenario_id)

    async def clear_all(self, scenario_id: int):
        t = time()
        await self.mongo_connector.customers.update_many(
            {'scenario_id': scenario_id, 'is_deleted': False},
            {"$set": {'edit_timestamp': t, 'is_deleted': True}}
        )
        await self.actionsdb.clear_all(t, scenario_id)

    async def go_back(self, scenario_id: int):
        action, timestamp = await self.actionsdb.rollback(scenario_id)
        if action == Actions.action_clear_data:
            await self.mongo_connector.customers.update_many(
                {'scenario_id': scenario_id, 'edit_timestamp': timestamp},
                {"$set": {'edit_timestamp': time(), 'is_deleted': False}}
            )
        if action == Actions.action_add_data:
            await self.mongo_connector.customers.update_many(
                {'scenario_id': scenario_id, 'edit_timestamp': timestamp},
                {"$set": {'is_deleted': True, 'edit_timestamp': time()}}
            )

    async def get_first_not_filled(self, scenario_id: int):
        coursor = self.mongo_connector.customers. \
            find({"not_filled": {"$gt": 0}, 'scenario_id': scenario_id,
                  'is_deleted': False}).limit(1)
        async for message in coursor:
            return message

    async def get_latest_edited_not_filled(self, scenario_id: int):
        coursor = self.mongo_connector.customers. \
            find({"not_filled": {"$gt": 0}, 'scenario_id': scenario_id,
                  'is_deleted': False}).sort("edit_timestamp", -1).limit(1)
        async for message in coursor:
            return message

    async def get_least_of_empty(self, scenario_id: int):
        coursor = self.mongo_connector.customers. \
            find({"not_filled": {"$gt": 0}, 'scenario_id': scenario_id,
                  'is_deleted': False}).sort("not_filled", 1).limit(1)
        async for message in coursor:
            return message
