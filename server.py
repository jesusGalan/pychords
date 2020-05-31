# -*- coding: utf-8 -*-
import json
import os
import platform
import sys

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from scales import get_scale_name_list, get_grade_name_list_of_scale, get_tone_name_list_of_grade, get_notes_of
from notePosition import get_fretboard_note_positions
from get_chords_by_scale import get_data_by

from tornado.options import define, options

if (platform.system() == 'Windows'):
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

define('port', default=9000, help='Especifica el puerto', type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(os.path.join('web/index.html'))


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
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        note = self.get_argument('note')
        positions = get_fretboard_note_positions(note)

        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(positions))


class NoteAndScaleHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        self.write('some post')

    def get(self):
        note = self.get_argument('note')
        scalename = self.get_argument('scalename')
        chords = get_notes_of(scalename, note)
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps({'response': chords}))

    def options(self):
        self.set_status(200)
        self.finish()

class ChordNotationApiHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        self.write('some post')

    def get(self):
        note = self.get_argument('note')
        scalename = self.get_argument('scalename')
        deep = int(self.get_argument('deep'))
        chords = get_data_by(note.capitalize(), scalename, deep)

        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps({'response': chords}))

    def options(self):
        self.set_status(200)
        self.finish()

if __name__ == '__main__':
    tornado.options.parse_command_line()
    handlers = [
        (r'/', IndexHandler),
        (r'/api/scale/', AllScalesApiHandler),
        (r'/api/grades/', ScaleGradesApiHandler),
        (r'/api/tones/', TonesApiHandler),
        (r'/api/note_positions/', NotePositionsHandler),
        (r'/api/notes/', NoteAndScaleHandler),
        (r'/api/scale_list/', AllScalesApiHandler),
        (r'/api/chord_notation/', ChordNotationApiHandler),
    ]
    static_path = os.path.join(os.path.dirname(__file__), 'web/static')
    app = tornado.web.Application(handlers=handlers, static_path=static_path,
                                  debug=False)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print ('Server listening on port ' + str(options.port))
    tornado.ioloop.IOLoop.instance().start()
