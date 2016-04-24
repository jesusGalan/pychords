# -*- coding: utf-8 -*-


from expects import *
from pychords.functions import scales


with description('Generating scales'):

        with context("escala englimatic"):

            with it('escala_englimatic_primer_grado'):
                note = "C"
                scale = "escala_englimatic_primer_grado"

                expect(scales(scale, note)).to(equal(['C', 'Db', 'E', 'F#', 'G#', 'A#', 'B']))

            with it('escala_englimatic_segundo_grado'):
                note = "C#"
                scale = "escala_englimatic_segundo_grado"

                expect(scales(scale, note)).to(equal(['Db', 'E', 'F#', 'G#', 'A#', 'B', 'C']))

            with it('escala_englimatic_tercer_grado'):
                note = "E"
                scale = "escala_englimatic_tercer_grado"

                expect(scales(scale, note)).to(equal(['E', 'F#', 'G#', 'A#', 'B', 'C', 'Db']))

            with it('escala_englimatic_cuarto_grado'):
                note = "F#"
                scale = "escala_englimatic_cuarto_grado"

                expect(scales(scale, note)).to(equal(['F#', 'G#', 'A#', 'B', 'C', 'Db', 'E']))

            with it('escala_englimatic_quinto_grado'):
                note = "G#"
                scale = "escala_englimatic_quinto_grado"

                expect(scales(scale, note)).to(equal(['G#', 'A#', 'B', 'C', 'Db', 'E', 'F#']))

            with it('escala_englimatic_sexto_grado'):
                note = "A#"
                scale = "escala_englimatic_sexto_grado"

                expect(scales(scale, note)).to(equal(['A#', 'B', 'C', 'Db', 'E', 'F#', 'G#']))

            with it('escala_englimatic_septimo_grado'):
                note = "B"
                scale = "escala_englimatic_septimo_grado"

                expect(scales(scale, note)).to(equal(['B', 'C', 'Db', 'E', 'F#', 'G#', 'A#']))
