# -*- coding: utf-8 -*-


from expects import *
from pychords.scales import get_notes_of


with description('Generating get_notes_of'):

        with context('escalas simétricas'):

            with it('escala_tono_a_tono'):
                note = "B"
                scale = "escala_tono_a_tono"

                expect(get_notes_of(scale, note)).to(equal(['B', 'C#', 'D#', 'F', 'G', 'A']))

            with it("escala_semitono_a_tono"):
                note = "E"
                scale = "escala_semitono_a_tono"

                expect(get_notes_of(scale, note)).to(equal(
                    ['E', 'F', 'G', 'Ab', 'Bb', 'B', 'C#', 'D']))

            with it("escala_semitono_a_tono"):
                note = "E"
                scale = "escala_semitono_a_tono"

                expect(get_notes_of(scale, note)).to(equal(
                    ['E', 'F', 'G', 'Ab', 'Bb', 'B', 'C#', 'D']))

            with it("escala_cromatica"):
                note = "C"
                scale = "escala_cromatica"

                expect(get_notes_of(scale, note)).to(equal(
                    ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']))
