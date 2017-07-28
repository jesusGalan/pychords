# -*- coding: utf-8 -*-


from mamba import *
from expects import *
from pychords.functions import *
from pychords.notePosition import *


with description("App pyChords"):
    with context('function for take required notes must do it'):

        with it('must return required scale notes'):

            scale = ['A#.Bb', 'B', 'C', 'C#.Db', 'D#.Eb', 'E', 'F', 'F#.Gb', 'G', 'G#.Ab', 'A']
            sure = 'C'
            next_sure = 'E'

            expect(get_short_list_of_notes(sure, next_sure, scale)).to(equal(['C', 'C#.Db', 'D#.Eb', 'E']))

        with it('must return required scale notes'):

            scale = ['A#.Bb', 'C', 'D', 'E', 'F#.Gb', 'G', 'A', 'A#.Bb', 'C', 'D', 'E', 'F#.Gb', 'G', 'A']
            sure = 'E'
            next_sure = 'G'

            expect(get_short_list_of_notes(sure, next_sure, scale)).to(equal(['E', 'F#.Gb', 'G']))

    with context('function for take all notes must do it'):

        with it('must return a list from Bb'):

            note = 'Bb'

            expect(take_all_notes_from(note)).to(equal(
                ['A#.Bb', 'B', 'C', 'C#.Db', 'D', 'D#.Eb', 'E', 'F', 'F#.Gb', 'G', 'G#.Ab', 'A']))

        with it('must return a list from B'):

            note = 'B'

            expect(take_all_notes_from(note)).to(equal(
                ['B', 'C', 'C#.Db', 'D', 'D#.Eb', 'E', 'F', 'F#.Gb', 'G', 'G#.Ab', 'A', 'A#.Bb']))

    with context('must return good notes'):

        with it("must return good notes with a short list"):

            short_list = ['C', 'C#.Db', 'D#.Eb', 'F#.Gb', 'G']

            expect(return_good_notes(short_list)).to(equal(['C', 'Db', 'Eb', 'F#', 'G']))

        with it("must return good notes with a short list"):

            short_list = ['C', 'D#.Eb', 'F#.Gb', 'A']

            expect(return_good_notes(short_list)).to(equal(['C', 'D#', 'F#', 'A']))

        with it("must return good notes with a short list"):

            short_list = ['C', 'C#.Db', 'D#.Eb', 'F#.Gb', 'A']

            expect(return_good_notes(short_list)).to(equal(['C', 'Db', 'Eb', 'Gb', 'A']))

        with it("must return good notes with a short list"):

            short_list = ['C', 'D#.Eb', 'F#.Gb', 'G#.Ab', 'A']

            expect(return_good_notes(short_list)).to(equal(['C', 'D#', 'F#', 'G#', 'A']))

        with it("must return good notes with a short list"):

            short_list = ['F', 'F#.Gb', 'G#.Ab', 'A']

            expect(return_good_notes(short_list)).to(equal(['F', 'Gb', 'G#', 'A']))

    with context('mapping fretboard notes position'):
        # [{"cuerda": 1, "traste": 2}, {"cuerda": 3, "traste": 4}]
        # ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb','G', 'G#', Ab,'A', 'A#', 'Bb', 'B']
        with before.all:
            self.fretboard_position = get_fretboard_note_positions('foo')
            self.first_position = self.fretboard_position[0]

        with it('must return a list'):
            expect(self.fretboard_position).to(be_an(list))

        with it('must contain a positions'):
            expect(self.fretboard_position).not_to(be_empty)

        with it('position must be an a dict'):
            expect(self.first_position).to(be_an(dict))

        with it('returns cord position'):
            expect(self.first_position).to(have_key('cord'))

        with it('returns fret position'):
            expect(self.first_position).to(have_key('fret'))

        with it('returns a correct positions for a C note'):
            fretboard_position = get_fretboard_note_positions('C')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 8}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 8}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 1}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 5}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 10}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 3}))

        with it('returns a correct positions for a C# note'):
            fretboard_position = get_fretboard_note_positions('C#')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 9}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 9}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 2}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 6}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 11}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 4}))

        with it('returns a correct positions for a Db note'):
            fretboard_position = get_fretboard_note_positions('Db')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 9}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 9}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 2}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 6}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 11}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 4}))

        with it('returns a correct positions for a D note'):
            fretboard_position = get_fretboard_note_positions('D')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 10}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 10}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 3}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 7}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 0}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 5}))

        with it('returns a correct positions for a D# note'):
            fretboard_position = get_fretboard_note_positions('D#')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 11}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 11}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 4}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 8}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 1}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 6}))

        with it('returns a correct positions for a Eb note'):
            fretboard_position = get_fretboard_note_positions('Eb')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 11}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 11}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 4}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 8}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 1}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 6}))

        with it('returns a correct positions for a E note'):
            fretboard_position = get_fretboard_note_positions('E')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 0}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 0}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 5}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 9}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 2}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 7}))

        with it('returns a correct positions for a F note'):
            fretboard_position = get_fretboard_note_positions('F')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 1}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 1}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 6}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 10}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 3}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 8}))

        with it('returns a correct positions for a F# note'):
            fretboard_position = get_fretboard_note_positions('F#')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 2}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 2}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 7}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 11}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 4}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 9}))

        with it('returns a correct positions for a Gb note'):
            fretboard_position = get_fretboard_note_positions('Gb')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 2}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 2}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 7}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 11}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 4}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 9}))

        with it('returns a correct positions for a G note'):
            fretboard_position = get_fretboard_note_positions('G')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 3}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 3}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 8}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 0}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 5}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 10}))

        with it('returns a correct positions for a G# note'):
            fretboard_position = get_fretboard_note_positions('G#')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 4}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 4}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 9}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 1}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 6}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 11}))

        with it('returns a correct positions for a Ab note'):
            fretboard_position = get_fretboard_note_positions('Ab')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 4}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 4}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 9}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 1}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 6}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 11}))

        with it('returns a correct positions for a A note'):
            fretboard_position = get_fretboard_note_positions('A')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 5}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 5}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 10}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 2}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 7}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 0}))

        with it('returns a correct positions for a A# note'):
            fretboard_position = get_fretboard_note_positions('A#')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 6}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 6}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 11}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 3}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 8}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 1}))

        with it('returns a correct positions for a Bb note'):
            fretboard_position = get_fretboard_note_positions('Bb')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 6}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 6}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 11}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 3}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 8}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 1}))

        with it('returns a correct positions for a B note'):
            fretboard_position = get_fretboard_note_positions('B')

            expect(fretboard_position).to(contain({'cord': 1, 'fret': 7}))
            expect(fretboard_position).to(contain({'cord': 6, 'fret': 7}))
            expect(fretboard_position).to(contain({'cord': 2, 'fret': 0}))
            expect(fretboard_position).to(contain({'cord': 3, 'fret': 4}))
            expect(fretboard_position).to(contain({'cord': 4, 'fret': 9}))
            expect(fretboard_position).to(contain({'cord': 5, 'fret': 2}))
