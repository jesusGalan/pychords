# -*- coding: utf-8 -*-


from mamba import *
from expects import *
from pychords.pysong import *


with description("App pySongs"):
    with context('prepare notes for pysynth'):

        with it('must return well oriented octaves of notes'):

            expect(prepare_for_pysynth(['B', 'C', 'D'])).to(equal(((('b4', 4), ('c5', 4), ('d5', 4), ('b5', 4)))))

        with it('must return well oriented octaves of notes'):

            expect(prepare_for_pysynth(['A', 'B', 'C', 'D', 'E', 'F', 'G'])).to(equal(((('a4', 4), ('b4', 4), ('c5', 4), ('d5', 4), ('e5', 4), ('f5', 4), ('g5', 4), ('a5', 4)))))

        with it('must return well oriented octaves of notes'):

            expect(prepare_for_pysynth(['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'])).to(equal(((('e4', 4), ('f#4', 4), ('g#4', 4), ('a4', 4), ('b4', 4), ('c#5', 4), ('d#5', 4), ('e5', 4)))))

    with context('Searching C position'):

        with it('must return an easy position'):

            expect(search_c_position(['A', 'B', 'C', 'D', 'E', 'F', 'G'])).to(equal(2))

        with it('must return an hard position'):

            expect(search_c_position(['A', 'A#', 'B', 'D#', 'E', 'F', 'G'])).to(equal(3))

        with it('must return an hard position'):

            expect(search_c_position(['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'])).to(equal(5))
