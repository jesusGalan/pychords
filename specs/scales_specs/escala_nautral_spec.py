# -*- coding: utf-8 -*-


from expects import *
from pychords.scaleNotes import get_notes_of


with description('Generating get_notes_of'):

        with context("escala natural"):

            with it("escala_mayor_natura"):
                note = "C"
                scale = "escala_mayor_natural"

                expect(get_notes_of(scale, note)).to(equal(
                    ['C', 'D', 'E', 'F', 'G', 'A', 'B']))

            with it("escala_ dorica"):
                note = "D"
                dscale = "escala_dorica"

                expect(get_notes_of(dscale, note)).to(equal(
                    ['D', 'E', 'F', 'G', 'A', 'B', 'C']))

            with it("escala_frigia"):
                note = "C#"
                scale = "escala_frigia"

                expect(get_notes_of(scale, note)).to(equal(
                    ['C#', 'D', 'E', 'F#', 'G#', 'A', 'B']))

            with it("escala_lidia"):
                note = "Gb"
                scale = "escala_lidia"

                expect(get_notes_of(scale, note)).to(equal(
                    ['Gb', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F']))

            with it("escala_mixolidia"):
                note = "G"
                scale = "escala_mixolidia"

                expect(get_notes_of(scale, note)).to(equal(
                    ['G', 'A', 'B', 'C', 'D', 'E', 'F']))

            with it("escala_ menor_natural"):
                note = "C"
                scale = "escala_menor_natural"

                expect(get_notes_of(scale, note)).to(equal(
                    ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']))

            with it("escala_menor_natural"):
                note = "C#"
                scale = "escala_menor_natural"

                expect(get_notes_of(scale, note)).to(equal(
                    ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']))

            with it("escala_locria"):
                note = "C#"
                scale = "escala_locria"

                expect(get_notes_of(scale, note)).to(equal(
                    ['C#', 'D', 'E', 'F#', 'G', 'A', 'B']
                ))
