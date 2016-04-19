# -*- coding: utf-8 -*-


import os
import json

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from pychords.functions import get_scale_name_list
from pychords.functions import get_grade_name_list_of_scale

from tornado.options import define, options
define('port', default=8000, help='Especifica el puerto', type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(os.path.join('index.html'))


class AllScalesApiHandler(tornado.web.RequestHandler):
    def get(self):
        scale_list = json.dumps(get_scale_name_list())

        self.set_header('Content-Type', 'application/json')
        self.write(scale_list)


class ScaleGradesApiHandler(tornado.web.RequestHandler):
    def get(self):
        scale = self.get_argument('scale')
        grade_list = get_grade_name_list_of_scale(scale)

        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(grade_list))


if __name__ == '__main__':
    tornado.options.parse_command_line()
    handlers = [
        (r'/', IndexHandler),
        (r'/api/scale/', AllScalesApiHandler),
        (r'/api/grades/', ScaleGradesApiHandler),
    ]
    static_path = os.path.join(os.path.dirname(__file__), 'static')
    app = tornado.web.Application(handlers=handlers, static_path=static_path,
                                  debug=True)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
