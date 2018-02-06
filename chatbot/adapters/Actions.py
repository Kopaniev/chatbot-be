class Actions:

    action_add_data = 'add_data'
    action_clear_data = 'clear_data'

    def __init__(self, connector):
        self.mongo_connector = connector

    async def add_customer_data(self, timestamp: float, scenario_id: int):
        data = {
            "timestamp": timestamp,
            "scenario_id": scenario_id,
            "type": self.action_add_data,
            'was_rollback': False
        }
        await self.mongo_connector.actions.insert_one(data)

    async def clear_all(self, timestamp: float, scenario_id: int):
        data = {
            "timestamp": timestamp,
            "scenario_id": scenario_id,
            "type": self.action_clear_data,
            'was_rollback': False
        }
        await self.mongo_connector.actions.insert_one(data)

    async def get_latest(self, scenario_id: int):
        coursor = self.mongo_connector.actions.\
            find({"was_rollback": False, 'scenario_id': scenario_id}).\
            sort("timestamp", -1).\
            limit(1)
        async for message in coursor:
            return message

    async def rollback(self, scenario_id: int):
        latest = await self.get_latest(scenario_id)
        await self.mongo_connector.actions.update(
            {'timestamp': latest['timestamp']},
            {'$set': {'was_rollback': True}}
        )
        return latest['type'], latest['timestamp']
