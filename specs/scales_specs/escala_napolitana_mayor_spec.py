# -*- coding: utf-8 -*-


from expects import *
from pychords.functions import scales


with description('Generating scales'):

        with context("escala menor armonica"):

            with it("escala_persa"):
                note = 'F#'
                scale = 'escala_persa'

                expect(scales(scale, note)).to(equal(
                    ['F#', 'G', 'A#', 'B', 'C#', 'D', 'F']))

            with it("escala_lidia_#2_#6"):
                note = 'G'
                scale = 'escala_lidia_#2_#6'

                expect(scales(scale, note)).to(equal(
                    ['G', 'A#', 'B', 'C#', 'D', 'F', 'F#']))

            with it("escala_frigia_b4_bb7"):
                note = 'A#'
                scale = 'escala_frigia_b4_bb7'

                expect(scales(scale, note)).to(equal(
                    ['A#', 'B', 'C#', 'D', 'F', 'Gb', 'G']))

            with it('escala_doble_armonica_menor'):

                note = "B"
                scale = "escala_doble_armonica_menor"

                expect(scales(scale, note)).to(equal(
                    ['B', 'C#', 'D', 'F', 'Gb', 'G', 'A#']))

            with it('escala_oriental'):
                note = "C#"
                scale = "escala_oriental"

                expect(scales(scale, note)).to(equal(
                    ['C#', 'D', 'F', 'F#', 'G', 'A#', 'B']))

            with it('escala_jonica_aumentada_#2'):
                note = "D"
                scale = "escala_jonica_aumentada_#2"

                expect(scales(scale, note)).to(equal(
                    ['D', 'F', 'Gb', 'G', 'A#', 'B', 'C#']))

            with it("escala_locria_bb3_bb7"):
                note = 'F'
                scale = 'escala_locria_bb3_bb7'

                expect(scales(scale, note)).to(equal(
                    ['F', 'Gb', 'G', 'A#', 'B', 'C#', 'D']))
