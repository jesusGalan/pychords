# -*- coding: utf-8 -*-


from expects import *
from pychords.functions import scales


with description('Generating scales'):

        with context('escalas simétricas'):

            with it('escala_tono_a_tono'):
                note = "B"
                scale = "escala_tono_a_tono"

                expect(scales(scale, note)).to(equal(['B', 'C#', 'D#', 'F', 'G', 'A']))

            with it("escala_semitono_a_tono"):
                note = "E"
                scale = "escala_semitono_a_tono"

                expect(scales(scale, note)).to(equal(
                    ['E', 'F', 'G', 'Ab', 'Bb', 'B', 'C#', 'D']))

            with it("escala_semitono_a_tono"):
                note = "E"
                scale = "escala_semitono_a_tono"

                expect(scales(scale, note)).to(equal(
                    ['E', 'F', 'G', 'Ab', 'Bb', 'B', 'C#', 'D']))

            with it("escala_cromatica"):
                note = "C"
                scale = "escala_cromatica"

                expect(scales(scale, note)).to(equal(
                    ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']))
