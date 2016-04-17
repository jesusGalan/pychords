# -*- coding: utf-8 -*-


import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options

import os

from pyChords import scale_to_json

from tornado.options import define, options
define('port', default=8000, help='Especifica el puerto', type=int)


class ApiHandler(tornado.web.RequestHandler):
    def get(self):
        argument = self.get_argument('escala')

        self.write(scale_to_json(argument))


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('static/index.html')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    handlers = [(r'/api', ApiHandler), (r'/', IndexHandler)]
    static_path = os.path.join(os.path.dirname(__file__), 'static')
    app = tornado.web.Application(handlers=handlers, static_path=static_path)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
