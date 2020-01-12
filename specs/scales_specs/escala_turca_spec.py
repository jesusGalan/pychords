# -*- coding: utf-8 -*-


from expects import *
from scales import get_notes_of


with description('Generating get_notes_of'):

        with context("escala natural"):

            with it("escala_turca_primer_grado"):
                note = "C"
                scale = "escala_turca_primer_grado"

                expect(get_notes_of(scale, note)).to(equal(
                    ['C', 'Db', 'Eb', 'F', 'G', 'A', 'B']))

            with it("escala_turca_segundo_grado"):
                note = 'Db'
                dscale = "escala_turca_segundo_grado"

                expect(get_notes_of(dscale, note)).to(equal(
                    ['Db', 'Eb', 'F', 'G', 'A', 'B', 'C']))

            with it("escala_turca_tercer_grado"):
                note = "Eb"
                scale = "escala_turca_tercer_grado"

                expect(get_notes_of(scale, note)).to(equal(
                    ['Eb', 'F', 'G', 'A', 'B', 'C', 'Db']))

            with it("escala_turca_cuarto_grado"):
                note = "F"
                scale = "escala_turca_cuarto_grado"

                expect(get_notes_of(scale, note)).to(equal(
                    ['F', 'G', 'A', 'B', 'C', 'Db', 'Eb']))

            with it("escala_turca_quinto_grado"):
                note = "G"
                scale = "escala_turca_quinto_grado"

                expect(get_notes_of(scale, note)).to(equal(
                    ['G', 'A', 'B', 'C', 'Db', 'Eb', 'F']))

            with it("escala_turca_sexto_grado"):
                note = "A"
                scale = "escala_turca_sexto_grado"

                expect(get_notes_of(scale, note)).to(equal(
                    ['A', 'B', 'C', 'Db', 'Eb', 'F', 'G']))

            with it("escala_turca_septimo_grado"):
                note = "B"
                scale = "escala_turca_septimo_grado"

                expect(get_notes_of(scale, note)).to(equal(
                    ['B', 'C', 'Db', 'Eb', 'F', 'G', 'A']))
