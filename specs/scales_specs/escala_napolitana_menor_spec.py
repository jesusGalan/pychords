# -*- coding: utf-8 -*-


from expects import *
from pychords.functions import scales


with description('Generating scales'):

        with context("escala heptatonica de blues"):

            with it('escala_napolitana_menor_primer_grado'):
                note = "C"
                scale = "escala_napolitana_menor_primer_grado"

                expect(scales(scale, note)).to(equal(['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'B']))

            with it('escala_lidia_#6'):
                note = "Db"
                scale = "escala_lidia_#6"

                expect(scales(scale, note)).to(equal(['Db', 'Eb', 'F', 'G', 'Ab', 'B', 'C']))

            with it('escala_napolitana_menor_tercer_grado'):
                note = "Eb"
                scale = "escala_napolitana_menor_tercer_grado"

                expect(scales(scale, note)).to(equal(['Eb', 'F', 'G', 'Ab', 'B', 'C', 'Db']))

            with it('escala_gipsy'):
                note = "F"
                scale = "escala_gipsy"

                expect(scales(scale, note)).to(equal(['F', 'G', 'Ab', 'B', 'C', 'Db', 'Eb']))

            with it('escala_locria_mayor'):
                note = "G"
                scale = "escala_locria_mayor"

                expect(scales(scale, note)).to(equal(['G', 'Ab', 'B', 'C', 'Db', 'Eb', 'F']))

            with it('escala_napolitana_menor_sexto_grado'):
                note = "Ab"
                scale = "escala_napolitana_menor_sexto_grado"

                expect(scales(scale, note)).to(equal(['Ab', 'B', 'C', 'Db', 'Eb', 'F', 'G']))

            with it('escala_napolitana_menor_septimo_grado'):
                note = "B"
                scale = "escala_napolitana_menor_septimo_grado"

                expect(scales(scale, note)).to(equal(['B', 'C', 'Db', 'Eb', 'F', 'G', 'Ab']))
