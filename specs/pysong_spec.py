# -*- coding: utf-8 -*-


from mamba import *
from expects import *
from pychords.pysong import *


with description("App pySongs"):
    with context('prepare notes for pysynth'):

        with it('must return well oriented octaves of notes'):

            expect(prepare_for_pysynth(['B', 'C', 'D'])).to(equal(tuple((('b4', 4), ('c5', 4), ('d5', 4)))))
