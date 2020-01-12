# -*- coding: utf-8 -*-


from expects import *
from scales import get_notes_of


with description('Generating get_notes_of'):

        with context("escala heptatonica de blues"):

            with it('escala_heptatonica_de_blues_primer_grado'):
                note = "C"
                scale = "escala_heptatonica_de_blues_primer_grado"

                expect(get_notes_of(scale, note)).to(equal(['C', 'D#', 'E', 'F', 'Gb', 'G', 'A#']))

            with it('escala_heptatonica_de_blues_segundo_grado'):
                note = "D#"
                scale = "escala_heptatonica_de_blues_segundo_grado"

                expect(get_notes_of(scale, note)).to(equal(['D#', 'E', 'F', 'F#', 'G', 'A#', 'C']))

            with it('escala_heptatonica_de_blues_tercer_grado'):
                note = "E"
                scale = "escala_heptatonica_de_blues_tercer_grado"

                expect(get_notes_of(scale, note)).to(equal(['E', 'F', 'Gb', 'G', 'A#', 'C', 'D#']))

            with it('escala_heptatonica_de_blues_cuarto_grado'):
                note = "F"
                scale = "escala_heptatonica_de_blues_cuarto_grado"

                expect(get_notes_of(scale, note)).to(equal(['F', 'Gb', 'G', 'A#', 'C', 'D#', 'E']))

            with it('escala_heptatonica_de_blues_quinto_grado'):
                note = "Gb"
                scale = "escala_heptatonica_de_blues_quinto_grado"

                expect(get_notes_of(scale, note)).to(equal(['F#', 'G', 'A#', 'C', 'D#', 'E', 'F']))

            with it('escala_heptatonica_de_blues_sexto_grado'):
                note = "G"
                scale = "escala_heptatonica_de_blues_sexto_grado"

                expect(get_notes_of(scale, note)).to(equal(['G', 'A#', 'C', 'D#', 'E', 'F', 'F#']))

            with it('escala_heptatonica_de_blues_septimo_grado'):
                note = "Bb"
                scale = "escala_heptatonica_de_blues_septimo_grado"

                expect(get_notes_of(scale, note)).to(equal(['A#', 'C', 'D#', 'E', 'F', 'Gb', 'G']))
