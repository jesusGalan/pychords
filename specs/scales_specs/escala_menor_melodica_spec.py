# -*- coding: utf-8 -*-


from expects import *
from pychords.functions import scales


with description('Generating scales'):

        with context('escala menor melodica'):

            with it("menor_melodica"):
                note = 'Bb'
                scale = 'escala_menor_melodica'

                expect(scales(scale, note)).to(equal(
                    ['Bb', 'C', 'Db', 'Eb', 'F', 'G', 'A']))

            with it("escala_java"):
                note = 'A#'
                scale = 'escala_java'

                expect(scales(scale, note)).to(equal(
                    ['A#', 'B', 'C#', 'D#', 'F', 'G', 'Ab']))

            with it("escala_lidia_#5"):
                note = 'Bb'
                scale = 'escala_lidia_#5'

                expect(scales(scale, note)).to(equal(
                    ['Bb', 'C', 'D', 'E', 'F#', 'G', 'A']))

            with it("escala_lidia_#5"):
                note = 'A#'
                scale = 'escala_lidia_#5'

                expect(scales(scale, note)).to(equal(
                    ['Bb', 'C', 'D', 'E', 'F#', 'G', 'A']))

            with it("escala_lidia_b7"):
                note = 'Bb'
                scale = 'escala_lidia_b7'

                expect(scales(scale, note)).to(equal(
                    ['Bb', 'C', 'D', 'E', 'F', 'G', 'Ab']))

            with it("escala_lidia_b7"):
                note = 'A#'
                scale = 'escala_lidia_b7'

                expect(scales(scale, note)).to(equal(
                    ['Bb', 'C', 'D', 'E', 'F', 'G', 'Ab']))

            with it("escala_hindustan"):
                note = 'Bb'
                scale = 'escala_hindustan'

                expect(scales(scale, note)).to(equal(
                    ['Bb', 'C', 'D', 'Eb', 'F', 'Gb', 'Ab']))

            with it("escala_hindustan"):
                note = 'A#'
                scale = 'escala_hindustan'

                expect(scales(scale, note)).to(equal(
                    ['Bb', 'C', 'D', 'Eb', 'F', 'Gb', 'Ab']))

            with it("escala_locria_natural_2"):
                note = 'Bb'
                scale = 'escala_locria_natural_2'

                expect(scales(scale, note)).to(equal(
                    ['A#', 'C', 'Db', 'D#', 'E', 'F#', 'G#']))

            with it("escala_locria_natural_2"):
                note = 'A#'
                scale = 'escala_locria_natural_2'

                expect(scales(scale, note)).to(equal(
                    ['A#', 'C', 'Db', 'D#', 'E', 'F#', 'G#']))

            with it("escala_alterada"):
                note = 'C'
                scale = 'escala_alterada'

                expect(scales(scale, note)).to(equal(
                    ['C', 'Db', 'Eb', 'E', 'F#', 'G#', 'A#']))
