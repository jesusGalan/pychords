# -*- coding: utf-8 -*-


from expects import *
from scales import get_notes_of


with description('Generating get_notes_of'):

        with context('escala menor melodica'):

            with it("menor_melodica"):
                note = 'Bb'
                scale = 'escala_menor_melodica'

                expect(get_notes_of(scale, note)).to(equal(
                    ['Bb', 'C', 'Db', 'Eb', 'F', 'G', 'A']))

            with it("escala_java"):
                note = 'A#'
                scale = 'escala_java'

                expect(get_notes_of(scale, note)).to(equal(
                    ['A#', 'B', 'C#', 'D#', 'F', 'G', 'Ab']))

            with it("escala_lidia_#5"):
                note = 'Bb'
                scale = 'escala_lidia_#5'

                expect(get_notes_of(scale, note)).to(equal(
                    ['Bb', 'C', 'D', 'E', 'F#', 'G', 'A']))

            with it("escala_lidia_#5"):
                note = 'A#'
                scale = 'escala_lidia_#5'

                expect(get_notes_of(scale, note)).to(equal(
                    ['Bb', 'C', 'D', 'E', 'F#', 'G', 'A']))

            with it("escala_lidia_b7"):
                note = 'Bb'
                scale = 'escala_lidia_b7'

                expect(get_notes_of(scale, note)).to(equal(
                    ['Bb', 'C', 'D', 'E', 'F', 'G', 'Ab']))

            with it("escala_lidia_b7"):
                note = 'A#'
                scale = 'escala_lidia_b7'

                expect(get_notes_of(scale, note)).to(equal(
                    ['Bb', 'C', 'D', 'E', 'F', 'G', 'Ab']))

            with it("escala_mixolidia_b6"):
                note = 'Bb'
                scale = 'escala_mixolidia_b6'

                expect(get_notes_of(scale, note)).to(equal(
                    ['Bb', 'C', 'D', 'Eb', 'F', 'Gb', 'Ab']))

            with it("escala_mixolidia_b6"):
                note = 'A#'
                scale = 'escala_mixolidia_b6'

                expect(get_notes_of(scale, note)).to(equal(
                    ['Bb', 'C', 'D', 'Eb', 'F', 'Gb', 'Ab']))

            with it("escala_locria_natural_2"):
                note = 'Bb'
                scale = 'escala_locria_natural_2'

                expect(get_notes_of(scale, note)).to(equal(
                    ['A#', 'C', 'Db', 'D#', 'E', 'F#', 'G#']))

            with it("escala_locria_natural_2"):
                note = 'A#'
                scale = 'escala_locria_natural_2'

                expect(get_notes_of(scale, note)).to(equal(
                    ['A#', 'C', 'Db', 'D#', 'E', 'F#', 'G#']))

            with it("escala_alterada"):
                note = 'C'
                scale = 'escala_alterada'

                expect(get_notes_of(scale, note)).to(equal(
                    ['C', 'Db', 'Eb', 'E', 'F#', 'G#', 'A#']))
