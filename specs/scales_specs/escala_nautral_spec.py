# -*- coding: utf-8 -*-


from expects import *
from pychords.functions import scales


with description('Generating scales'):

        with context("escala natural"):

            with it("must return major scale"):
                note = "C"
                scale = "escala_mayor_natural"

                expect(scales(scale, note)).to(equal(
                    ['C', 'D', 'E', 'F', 'G', 'A', 'B']))

            with it("must return D dorian scale"):
                note = "D"
                dscale = "escala_dorica"

                expect(scales(dscale, note)).to(equal(
                    ['D', 'E', 'F', 'G', 'A', 'B', 'C']))

            with it("must return C# frigian scale"):
                note = "C#"
                scale = "escala_frigia"

                expect(scales(scale, note)).to(equal(
                    ['C#', 'D', 'E', 'F#', 'G#', 'A', 'B']))

            with it("must return Gb lidian scale"):
                note = "Gb"
                scale = "escala_lidia"

                expect(scales(scale, note)).to(equal(
                    ['Gb', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F']))

            with it("must return Gb mixolidian scale"):
                note = "G"
                scale = "escala_mixolidia"

                expect(scales(scale, note)).to(equal(
                    ['G', 'A', 'B', 'C', 'D', 'E', 'F']))

            with it("must return C minor scale"):
                note = "C"
                scale = "escala_menor_natural"

                expect(scales(scale, note)).to(equal(
                    ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']))

            with it("must return C# minor scale"):
                note = "C#"
                scale = "escala_menor_natural"

                expect(scales(scale, note)).to(equal(
                    ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']))

            with it("escala_locria"):
                note = "C#"
                scale = "escala_locria"

                expect(scales(scale, note)).to(equal(
                    ['C#', 'D', 'E', 'F#', 'G', 'A', 'B']
                ))
