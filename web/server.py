# -*- coding: utf-8 -*-


import os
import json

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from pychords.functions import get_scale_name_list
from pychords.functions import get_grade_name_list_of_scale
from pychords.functions import get_tone_name_list_of_grade
from pychords.notePosition import get_fretboard_note_positions

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


class TonesApiHandler(tornado.web.RequestHandler):
    def get(self):
        grade = self.get_argument('grade')
        tone_list = get_tone_name_list_of_grade(grade)

        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(tone_list))

class NotePositionsHandler(tornado.web.RequestHandler):
    def get(self):
        note = self.get_argument('note')
        positions = get_fretboard_note_positions(note)

        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(positions))


if __name__ == '__main__':
    tornado.options.parse_command_line()
    handlers = [
        (r'/', IndexHandler),
        (r'/api/scale/', AllScalesApiHandler),
        (r'/api/grades/', ScaleGradesApiHandler),
        (r'/api/tones/', TonesApiHandler),
        (r'/api/note_positions/', NotePositionsHandler),
    ]
    static_path = os.path.join(os.path.dirname(__file__), 'static')
    app = tornado.web.Application(handlers=handlers, static_path=static_path,
                                  debug=True)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
