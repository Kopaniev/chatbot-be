from chatbot.use_cases.TopicsHandler import TopicsHandler


class Scenario1:
    scenario_id = 1
    allow_topics = [
        'person_data',
        'vehicle_data',
        'geo_data',
    ]

    @classmethod
    async def processing_data(cls, messages, db):
        th = TopicsHandler(
            cls.allow_topics,
            cls.scenario_id
        )
        await th.processing_data(messages, db)

    @classmethod
    async def prepare_response(cls, db):
        data = await db.get_first_not_filled(cls.scenario_id)
        if data:
            for k, v in data['entities'].items():
                for k1, j in v.items():
                    if not j:
                        return k1
        return None


class Scenario2:
    scenario_id = 2
    allow_topics = [
        'person_data',
        'vehicle_data',
        'geo_data',
    ]

    @classmethod
    async def processing_data(cls, messages, db):
        th = TopicsHandler(
            cls.allow_topics,
            cls.scenario_id
        )
        await th.processing_data(messages, db)

    @classmethod
    async def prepare_response(cls, db):
        data = await db.get_latest_edited_not_filled(cls.scenario_id)
        if data:
            for k, v in data['entities'].items():
                for k1, j in v.items():
                    if not j:
                        return k1
        return None


class Scenario3:
    scenario_id = 3
    allow_topics = [
        'person_data',
        'vehicle_data'
    ]

    @classmethod
    async def processing_data(cls, messages, db):
        th = TopicsHandler(
            cls.allow_topics,
            cls.scenario_id
        )
        await th.processing_data(messages[:1], db)

    @classmethod
    async def prepare_response(cls, db):
        data = await db.get_least_of_empty(cls.scenario_id)
        if data:
            for k, v in data['entities'].items():
                for k1, j in v.items():
                    if not j:
                        return k1
        return None
