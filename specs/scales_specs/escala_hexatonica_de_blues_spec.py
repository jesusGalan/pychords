# -*- coding: utf-8 -*-


from expects import *
from pychords.scales import get_notes_of


with description('Generating get_notes_of'):

        with context('escala hexatonica de blues'):

            with it('escala_hexatonica_de_blues_primer_grado'):
                note = "C"
                scale = "escala_hexatonica_de_blues_primer_grado"

                expect(get_notes_of(scale, note)).to(equal(['C', 'D#', 'F', 'F#', 'G', 'A#']))

            with it('escala_hexatonica_de_blues_primer_grado'):
                note = "B"
                scale = "escala_hexatonica_de_blues_primer_grado"

                expect(get_notes_of(scale, note)).to(equal(['B', 'D', 'E', 'F', 'Gb', 'A']))

            with it('escala_hexatonica_de_blues_segundo_grado'):
                note = "D"
                scale = "escala_hexatonica_de_blues_segundo_grado"

                expect(get_notes_of(scale, note)).to(equal(['D', 'E', 'F', 'Gb', 'A', 'B']))

            with it('escala_hexatonica_de_blues_tercer_grado'):
                note = "E"
                scale = "escala_hexatonica_de_blues_tercer_grado"

                expect(get_notes_of(scale, note)).to(equal(['E', 'F', 'Gb', 'A', 'B', 'D']))

            with it('escala_hexatonica_de_blues_cuarto_grado'):
                note = "F"
                scale = "escala_hexatonica_de_blues_cuarto_grado"

                expect(get_notes_of(scale, note)).to(equal(['F', 'Gb', 'A', 'B', 'D', 'E']))

            with it('escala_hexatonica_de_blues_quinto_grado'):
                note = "Gb"
                scale = "escala_hexatonica_de_blues_quinto_grado"

                expect(get_notes_of(scale, note)).to(equal(['Gb', 'A', 'B', 'D', 'E', 'F']))

            with it('escala_hexatonica_de_blues_sexto_grado'):
                note = "A"
                scale = "escala_hexatonica_de_blues_sexto_grado"

                expect(get_notes_of(scale, note)).to(equal(['A', 'B', 'D', 'E', 'F', 'Gb']))
