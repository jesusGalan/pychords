# -*- coding: utf-8 -*-


from expects import *
from pychords.scales import get_notes_of


with description('Generating get_notes_of'):

        with context("escala hungara mayor"):

            with it("escala_hungara_mayor_primer_grado"):

                note = 'C'
                scale = 'escala_hungara_mayor_primer_grado'

                expect(get_notes_of(scale, note)).to(equal(["C", "D#", "E", "F#", "G", "A", "Bb"]))

            with it("escala_hungara_mayor_segundo_grado"):

                note = 'D#'
                scale = 'escala_hungara_mayor_segundo_grado'

                expect(get_notes_of(scale, note)).to(equal(["D#", "E", "F#", "G", "A", "Bb", "C"]))

            with it("escala_hungara_mayor_tercer_grado"):

                note = 'E'
                scale = 'escala_hungara_mayor_tercer_grado'

                expect(get_notes_of(scale, note)).to(equal(["E", "F#", "G", "A", "Bb", "C", "D#"]))

            with it("escala_hungara_mayor_cuarto_grado"):

                note = 'F#'
                scale = 'escala_hungara_mayor_cuarto_grado'

                expect(get_notes_of(scale, note)).to(equal(["F#", "G", "A", "Bb", "C", "D#", "E"]))

            with it("escala_hungara_mayor_quinto_grado"):

                note = 'G'
                scale = 'escala_hungara_mayor_quinto_grado'

                expect(get_notes_of(scale, note)).to(equal(["G", "A", "Bb", "C", "D#", "E", "F#"]))

            with it("escala_hungara_mayor_sexto_grado"):

                note = 'A'
                scale = 'escala_hungara_mayor_sexto_grado'

                expect(get_notes_of(scale, note)).to(equal(["A", "Bb", "C", "D#", "E", "F#", "G"]))
