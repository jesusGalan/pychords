# -*- coding: utf-8 -*-


from expects import *
from pychords.functions import scales


with description('Generating scales'):

        with context('escalas simétricas'):

            with it('must return escala tono a tono'):
                note = "B"
                scale = "escala_tono_a_tono"

                expect(scales(scale, note)).to(equal(['B', 'C#', 'D#', 'F', 'G', 'A']))

            with it("must return E semitone a tone scale"):
                note = "E"
                scale = "escala_semitono_a_tono"

                expect(scales(scale, note)).to(equal(
                    ['E', 'F', 'G', 'Ab', 'Bb', 'B', 'C#', 'D']))

            with it("must return E semitone a tone scale"):
                note = "E"
                scale = "escala_semitono_a_tono"

                expect(scales(scale, note)).to(equal(
                    ['E', 'F', 'G', 'Ab', 'Bb', 'B', 'C#', 'D']))

            with it("must return C cromatic scale"):
                note = "C"
                scale = "escala_cromatica"

                expect(scales(scale, note)).to(equal(
                    ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']))
