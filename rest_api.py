# -*- coding: utf-8 -*-


import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options

from pyChords import scale_to_json

from tornado.options import define, options
define('port', default=8000, help='Especifica el puerto', type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        argument = self.get_argument('escala')

        self.write(scale_to_json(argument))


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
