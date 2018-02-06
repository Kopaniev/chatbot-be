import json
import logging

import tornado.web
import tornado.ioloop
import tornado.escape
import motor

from chatbot.use_cases.Scenarios import Scenario1
from chatbot.use_cases.Scenarios import Scenario2
from chatbot.use_cases.Scenarios import Scenario3
from chatbot.adapters.CustomersDB import CustomersDB


class ScenarioOneHandler(tornado.web.RequestHandler):
    async def post(self):
        data = tornado.escape.json_decode(self.request.body)
        await Scenario1.processing_data(data, self.settings['db'])
        res = await Scenario1.prepare_response(self.settings['db'])
        self.write(json.dumps({"not_filled": res}))


class ScenarioTwoHandler(tornado.web.RequestHandler):
    async def post(self):
        data = tornado.escape.json_decode(self.request.body)
        await Scenario2.processing_data(data, self.settings['db'])
        res = await Scenario2.prepare_response(self.settings['db'])
        self.write(json.dumps({"not_filled": res}))


class ScenarioThreeHandler(tornado.web.RequestHandler):
    async def post(self):
        data = tornado.escape.json_decode(self.request.body)
        await Scenario3.processing_data(data, self.settings['db'])
        res = await Scenario3.prepare_response(self.settings['db'])
        self.write(json.dumps({"not_filled": res}))


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(levelname)s - %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.INFO
    )
    mongo_connector = motor.motor_tornado.MotorClient().test
    application = tornado.web.Application(
        [
            (r'/scenario1', ScenarioOneHandler),
            (r'/scenario2', ScenarioTwoHandler),
            (r'/scenario3', ScenarioThreeHandler)
        ],
        db=CustomersDB(mongo_connector)
    )
    application.listen(8881)
    tornado.ioloop.IOLoop.instance().start()
